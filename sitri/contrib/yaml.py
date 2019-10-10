import os
import typing

import yaml

from ..config.providers import ConfigProvider
from ..credentials.providers import CredentialProvider


class YamlConfigProvider(ConfigProvider):
    """Config provider for YAML"""

    provider_code = "yaml"

    def __init__(self, yaml_path: str = "./data.yaml", default_separator: str = "."):
        """

        :param yaml_path: path to yaml file
        :param default_separator: default value separator for path-mode
        """

        self._yaml = yaml.safe_load(open(os.path.abspath(yaml_path)))

        self.separator = default_separator

    def _get_by_path(self, path: str, separator: str) -> typing.Any:
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

    def _get_by_key(self, key: str) -> typing.Any:
        """Retrieve value from a dictionary using a key.

        :param key: key from json
        """

        if key in self._yaml:
            return self._yaml[key]
        else:
            return None

    def get(self, key: str, path_mode: bool = False, separator: str = None) -> typing.Optional[typing.Any]:
        """Get value from json

        :param key: key or path for search
        :param path_mode: boolean mode switcher
        :param separator: separator for path keys in path mode
        """

        separator = separator if separator else self.separator

        if path_mode:
            return self._get_by_path(key, separator=separator)

        return self._get_by_key(key)

    def keys(self, path_mode: bool = False, separator: str = None) -> typing.List[str]:
        """Keys in json

        :param path_mode: [future] path mode for keys list
        :param separator: [future] separators for keys in path mode
        """
        # TODO: implemented path-mode for keys list

        if not path_mode:
            return self._yaml.keys()
        else:
            raise NotImplementedError("Path-mode not implemented!")


class YamlCredentialProvider(CredentialProvider):
    """Credential provider for YAML"""

    provider_code = "yaml"

    def __init__(self, yaml_path: str = "./data.yaml", default_separator: str = "."):
        """

        :param yaml_path: path to yaml file
        :param default_separator: default value separator for path-mode
        """

        self._yaml = yaml.safe_load(open(os.path.abspath(yaml_path)))

        self.separator = default_separator

    def _get_by_path(self, path: str, separator: str) -> typing.Any:
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

    def _get_by_key(self, key: str) -> typing.Any:
        """Retrieve value from a dictionary using a key.

        :param key: key from yaml
        """

        if key in self._yaml:
            return self._yaml[key]
        else:
            return None

    def get(self, key: str, path_mode: bool = False, separator: str = None) -> typing.Optional[typing.Any]:
        """Get value from json

        :param key: key or path for search
        :param path_mode: boolean mode switcher
        :param separator: separator for path keys in path mode
        """

        separator = separator if separator else self.separator

        if path_mode:
            return self._get_by_path(key, separator=separator)

        return self._get_by_key(key)

    def keys(self, path_mode: bool = False, separator: str = None) -> typing.List[str]:
        """Keys in json

        :param path_mode: [future] path mode for keys list
        :param separator: [future] separators for keys in path mode
        """
        # TODO: implemented path-mode for keys list

        if not path_mode:
            return self._yaml.keys()
        else:
            raise NotImplementedError("Path-mode not implemented!")
