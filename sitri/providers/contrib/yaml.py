from __future__ import annotations

import os
import typing as t

import yaml

from sitri.providers.base import ConfigProvider, PathModeStateProvider

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


class YamlConfigProvider(PathModeStateProvider, ConfigProvider):
    """Config provider for YAML."""

    provider_code = "yaml"

    def __init__(
        self,
        yaml_path: str = "./data.yaml",
        yaml_data: str | None = None,
        default_separator: str = ".",
        found_file_error: bool = True,
        default_path_mode_state: bool = False,
        *args: t.Any,
        **kwargs: t.Any,
    ) -> None:
        """

        :param yaml_path: path to yaml file
        :param yaml_data: yaml data in string
        :param default_separator: default value separator for path-mode
        :param found_file_error: if true no file not found error raise on yaml.load
        :param default_path_mode_state: default state for path mode on get value by key
        """
        super().__init__(*args, **kwargs)

        if not yaml_data:
            self._yaml = self._get_yaml_from_file(yaml_path, found_file_error)
        else:
            yaml_data = StringIO(yaml_data)
            self._yaml = yaml.safe_load(yaml_data)

        self.separator = default_separator
        self._default_path_mode_state = default_path_mode_state

    @staticmethod
    def _get_yaml_from_file(yaml_path: str, found_file_error: bool) -> t.Any:
        """_get_yaml_from_file.

        :param yaml_path:
        :type yaml_path: str
        :param found_file_error:
        :type found_file_error: bool
        """
        try:
            with open(os.path.abspath(yaml_path)) as f:
                data = yaml.safe_load(f)

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
        dict_local = self._yaml.copy()
        keys = path.split(separator)

        for key in keys:
            try:
                dict_local = dict_local[int(key)] if key.isdigit() else dict_local[key]
            except Exception:
                if key not in dict_local:
                    return None

                dict_local = dict_local[key]
        return dict_local

    def _get_by_key(self, key: str) -> t.Any:
        """Retrieve value from a dictionary using a key.

        :param key: key from json
        """

        if key in self._yaml:
            return self._yaml[key]
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
            return self._yaml.keys()
        else:
            raise NotImplementedError("Path-mode not implemented!")

    @property
    def data(self) -> t.Dict[str, t.Any]:
        """Retrieve data as dict."""

        return self._yaml
