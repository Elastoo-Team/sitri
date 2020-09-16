import json
import os
import typing

from ..config.providers import ConfigProvider
from ..credentials.providers import CredentialProvider


class JsonConfigProvider(ConfigProvider):
    """Config provider for JSON."""

    provider_code = "json"

    def __init__(
        self,
        json_path: str = "./data.json",
        json_data: str = None,
        default_separator: str = ".",
        found_file_error: bool = True,
    ):
        """

        :param json_path: path to json file
        :param json_data: data of json
        :param default_separator: default value separator for path-mode
        :param found_file_error: if true no file not found error raise on json.load
        """
        if not json_data:
            try:
                self._json = json.load(open(os.path.abspath(json_path)))

            except FileNotFoundError:
                if not found_file_error:
                    self._json = {}
                else:
                    raise
        else:
            self._json = json.loads(json_data)

        self.separator = default_separator

    def _get_by_path(self, path: str, separator: str) -> typing.Any:
        """Retrieve value from a dictionary using a list of keys.

        :param path: string with separated keys
        """
        dict_local = self._json.copy()
        keys = path.split(separator)

        for key in keys:
            try:
                dict_local = dict_local[int(key)] if key.isdigit() else dict_local[key]
            except Exception:
                if key not in dict_local:
                    return None

                dict_local = dict_local[key]
        return dict_local

    def _get_by_key(self, key: str) -> typing.Any:
        """Retrieve value from a dictionary using a key.

        :param key: key from json
        """

        if key in self._json:
            return self._json[key]
        else:
            return None

    def get(self, key: str, path_mode: bool = False, separator: str = None) -> typing.Optional[typing.Any]:
        """Get value from json.

        :param key: key or path for search
        :param path_mode: boolean mode switcher
        :param separator: separator for path keys in path mode
        """

        separator = separator if separator else self.separator

        if path_mode:
            return self._get_by_path(key, separator=separator)

        return self._get_by_key(key)

    def keys(self, path_mode: bool = False, separator: str = None) -> typing.List[str]:
        """Keys in json.

        :param path_mode: [future] path mode for keys list
        :param separator: [future] separators for keys in path mode
        """
        # TODO: implemented path-mode for keys list

        if not path_mode:
            return self._json.keys()
        else:
            raise NotImplementedError("Path-mode not implemented!")


class JsonCredentialProvider(CredentialProvider):
    """Credential provider for JSON."""

    provider_code = "json"

    def __init__(
        self,
        json_path: str = "./data.json",
        json_data: str = None,
        default_separator: str = ".",
        found_file_error: bool = True,
    ):
        """

        :param json_path: path to json file
        :param json_data: data of json
        :param default_separator: default value separator for path-mode
        :param found_file_error: if true no file not found error raise on json.load
        """
        if not json_data:
            try:
                self._json = json.load(open(os.path.abspath(json_path)))
            except FileNotFoundError:
                if not found_file_error:
                    self._json = {}
                else:
                    raise
        else:
            self._json = json.loads(json_data)

        self.separator = default_separator

    def _get_by_path(self, path: str, separator: str) -> typing.Any:
        """Retrieve value from a dictionary using a list of keys.

        :param path: string with separated keys
        """
        dict_local = self._json.copy()
        keys = path.split(separator)

        for key in keys:
            try:
                dict_local = dict_local[int(key)] if key.isdigit() else dict_local[key]
            except Exception:
                if key not in dict_local:
                    return None

                dict_local = dict_local[key]
        return dict_local

    def _get_by_key(self, key: str) -> typing.Any:
        """Retrieve value from a dictionary using a key.

        :param key: key from json
        """

        if key in self._json:
            return self._json[key]
        else:
            return None

    def get(self, key: str, path_mode: bool = False, separator: str = None) -> typing.Optional[typing.Any]:
        """Get value from json.

        :param key: key or path for search
        :param path_mode: boolean mode switcher
        :param separator: separator for path keys in path mode
        """

        separator = separator if separator else self.separator

        if path_mode:
            return self._get_by_path(key, separator=separator)

        return self._get_by_key(key)

    def keys(self, path_mode: bool = False, separator: str = None) -> typing.List[str]:
        """Keys in json.

        :param path_mode: [future] path mode for keys list
        :param separator: [future] separators for keys in path mode
        """
        # TODO: implemented path-mode for keys list

        if not path_mode:
            return self._json.keys()
        else:
            raise NotImplementedError("Path-mode not implemented!")
