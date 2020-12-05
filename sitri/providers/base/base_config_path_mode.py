"""
.. module:: config.providers
   :synopsis: Config Base
.. moduleauthor:: Aleksander Lavrov <github.com/egnod>
"""


import typing
from abc import ABC, abstractmethod


class PathModeStateProvider(ABC):
    """Base class for config providers with path_mode discovery."""

    _default_path_mode_state: bool = False

    def _get_path_mode_state(self, path_mode_param: typing.Optional[bool]) -> bool:
        return path_mode_param if path_mode_param is not None else self._default_path_mode_state

    @abstractmethod
    def get(self, key: str, path_mode: typing.Optional[bool] = None, **kwargs) -> typing.Optional[typing.Any]:
        """Get value from storage.

        :param key: key for get value
        :param path_mode: find value by path with separated key
        :param kwargs: additional arguments for providers
        """

    @abstractmethod
    def _get_by_path(self, path: str, separator: str) -> typing.Any:
        """Retrieve value from a dictionary using a list of keys.

        :param path: string with separated keys
        """

    @abstractmethod
    def _get_by_key(self, key: str) -> typing.Any:
        """Retrieve value from a dictionary using a key.

        :param key: key from json
        """
