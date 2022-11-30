from __future__ import annotations

import os
import typing as t

import tomli as toml

from sitri.providers.base import ConfigProvider, PathModeStateProvider


class TomlConfigProvider(PathModeStateProvider, ConfigProvider):
    """Config provider for TOML."""

    provider_code = "toml"

    def __init__(
        self,
        toml_path: str = "./data.toml",
        toml_data: str | None = None,
        default_separator: str = ".",
        found_file_error: bool = True,
        default_path_mode_state: bool = False,
        *args: t.Any,
        **kwargs: t.Any,
    ) -> None:
        """

        :param toml_path: path to toml file
        :param toml_data: toml data in string
        :param default_separator: default value separator for path-mode
        :param found_file_error: if true no file not found error raise on toml.load
        :param default_path_mode_state: default state for path mode on get value by key
        """
        super().__init__(*args, **kwargs)

        if not toml_data:
            self._toml = self._get_toml_from_file(toml_path, found_file_error)
        else:
            self._toml = toml.loads(toml_data)

        self.separator = default_separator
        self._default_path_mode_state = default_path_mode_state

    @staticmethod
    def _get_toml_from_file(toml_path: str, found_file_error: bool) -> t.Dict[str, t.Any]:
        """_get_toml_from_file.

        :param toml_path:
        :type toml_path: str
        :param found_file_error:
        :type found_file_error: bool
        """
        try:
            with open(os.path.abspath(toml_path), "rb") as f:
                data = toml.load(f)

            return data

        except FileNotFoundError:
            if not found_file_error:
                return {}
            else:
                raise

    def _get_by_path(self, path: str, separator: str) -> t.Any:
        """Retrieve value from a dictionary using a list of keys.

        :param path: string with separated keys
        """
        dict_local = self._toml.copy()
        keys = path.split(separator)

        for key in keys:
            try:
                dict_local = dict_local[int(key)] if key.isdigit() else dict_local[key]  # type: ignore
            except Exception:
                if key not in dict_local:
                    return None

                dict_local = dict_local[key]
        return dict_local

    def _get_by_key(self, key: str) -> t.Any:
        """Retrieve value from a dictionary using a key.

        :param key: key from json
        """

        if key in self._toml:
            return self._toml[key]
        else:
            return None

    def get(self, key: str, path_mode: bool | None = None, separator: str = None, **kwargs: t.Any) -> t.Any | None:
        """Get value from json.

        :param key: key or path for search
        :param path_mode: boolean mode switcher
        :param separator: separator for path keys in path mode
        """

        separator = separator if separator else self.separator

        if self._get_path_mode_state(path_mode):
            return self._get_by_path(key, separator=separator)

        return self._get_by_key(key)

    def keys(self, path_mode: bool = False, separator: str = None, **kwargs: t.Any) -> t.List[str]:
        """Keys in json.

        :param path_mode: [future] path mode for keys list
        :param separator: [future] separators for keys in path mode
        """
        # TODO: implemented path-mode for keys list

        if not path_mode:
            return list(self._toml.keys())
        else:
            raise NotImplementedError("Path-mode not implemented!")

    @property
    def data(self) -> t.Dict[str, t.Any]:
        """Retrieve data as dict."""

        return self._toml
