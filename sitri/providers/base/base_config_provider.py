"""
.. module:: config.providers
   :synopsis: Config Base
.. moduleauthor:: Aleksander Lavrov <github.com/egnod>
"""


import typing
from abc import ABC, abstractmethod


class ConfigProvider(ABC):
    """Base class for config providers."""

    @property
    @abstractmethod
    def provider_code(self) -> str:
        """Provider code property for identity provider in manager."""

    @abstractmethod
    def get(self, key: str, **kwargs) -> typing.Optional[typing.Any]:
        """Get value from storage.

        :param key: key for get value
        :param kwargs: additional arguments for providers
        """

    def keys(self, **kwargs) -> typing.List[str]:
        """Get keys list in storage."""
        raise NotImplementedError("keys method not impl for this provider!")


class ConfigProviderManager:
    """Manager for children ConfigProvider classes."""

    @staticmethod
    def get_by_code(code: str) -> typing.Optional[typing.Type[ConfigProvider]]:
        """Get config provider by provider_code.

        :param code: provider_code for search config provider
        :Example:
            .. code-block:: python

               ConfigProviderManager.get_by_code("system")

               -> SystemConfigProvider
        """
        for provider in ConfigProvider.__subclasses__():
            if provider.provider_code == code:
                return provider
        return None
