import os
import typing

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
        yaml_data: str = None,
        default_separator: str = ".",
        found_file_error: bool = True,
        default_path_mode_state: bool = False,
    ):
        """

        :param yaml_path: path to yaml file
        :param yaml_data: yaml data in string
        :param default_separator: default value separator for path-mode
        :param found_file_error: if true no file not found error raise on yaml.load
        :param default_path_mode_state: default state for path mode on get value by key
        """

        if not yaml_data:
            try:
                self._yaml = yaml.safe_load(open(os.path.abspath(yaml_path)))

            except FileNotFoundError:
                if not found_file_error:
                    self._yaml = {}

                else:
                    raise

        else:
            yaml_data = StringIO(yaml_data)
            self._yaml = yaml.safe_load(yaml_data)

        self.separator = default_separator
        self._default_path_mode_state = default_path_mode_state

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

    def get(
        self, key: str, path_mode: typing.Optional[bool] = None, separator: str = None
    ) -> typing.Optional[typing.Any]:
        """Get value from json.

        :param key: key or path for search
        :param path_mode: boolean mode switcher
        :param separator: separator for path keys in path mode
        """

        separator = separator if separator else self.separator

        if self._get_path_mode_state(path_mode):
            return self._get_by_path(key, separator=separator)

        return self._get_by_key(key)

    def keys(self, path_mode: bool = False, separator: str = None) -> typing.List[str]:
        """Keys in json.

        :param path_mode: [future] path mode for keys list
        :param separator: [future] separators for keys in path mode
        """
        # TODO: implemented path-mode for keys list

        if not path_mode:
            return self._yaml.keys()
        else:
            raise NotImplementedError("Path-mode not implemented!")
