from __future__ import annotations

import os
import typing as t
from pathlib import Path

try:
    import orjson as json
except ImportError:
    import json  # type: ignore

from sitri.providers.base import ConfigProvider, PathModeStateProvider


class JsonConfigProvider(PathModeStateProvider, ConfigProvider):
    """Config provider for JSON."""

    provider_code = "json"

    def __init__(
        self,
        json_path: str = "./data.json",
        json_data: str | None = None,
        default_separator: str = ".",
        found_file_error: bool = True,
        default_path_mode_state: bool = False,
        *args: t.Any,
        **kwargs: t.Any,
    ) -> None:
        """

        :param json_path: path to json file
        :param json_data: data of json
        :param default_separator: default value separator for path-mode
        :param found_file_error: if true no file not found error raise on json.load
        :param default_path_mode_state: default state for path mode on get value by key
        """
        super().__init__(*args, **kwargs)

        if not json_data:
            self._json = self._get_json_from_file(json_path, found_file_error)
        else:
            self._json = json.loads(json_data)

        self.separator = default_separator
        self._default_path_mode_state = default_path_mode_state

    @staticmethod
    def _get_json_from_file(json_path: str, found_file_error: bool) -> t.Any:
        """_get_json_from_file.

        :param json_path:
        :type json_path: str
        :param found_file_error:
        :type found_file_error: bool
        """
        try:
            data = json.loads(Path(os.path.abspath(json_path)).read_text())

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
        dict_local = self._json.copy()
        keys = path.split(separator)

        for key in keys:
            try:
                dict_local = dict_local[int(key)] if key.isdigit() else dict_local[key]
            except Exception:
                if key not in dict_local.keys():
                    return None

                dict_local = dict_local[key]
        return dict_local

    def _get_by_key(self, key: str) -> t.Any:
        """Retrieve value from a dictionary using a key.

        :param key: key from json
        """

        if key in self._json.keys():
            return self._json[key]
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
            return self._json.keys()
        else:
            raise NotImplementedError("Path-mode not implemented!")

    @property
    def data(self) -> t.Dict[str, t.Any]:
        """Retrieve data as dict."""

        return self._json
