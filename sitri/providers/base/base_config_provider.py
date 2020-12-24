"""
.. module:: config.providers
   :synopsis: Config Base
.. moduleauthor:: Aleksander Lavrov <github.com/egnod>
"""
import inspect
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

        :param key: key for find value in provider source
        :param kwargs: additional arguments for providers
        """

    @abstractmethod
    def keys(self, **kwargs) -> typing.List[str]:
        """Get keys list in storage."""

    def fill(self, call: typing.Callable, **kwargs):
        """Fill callable object kwargs if all founded by provider.

        :param call: callable object for fill
        :param kwargs: additional arguments for getting
        """
        parameters = inspect.signature(call).parameters
        data = {}

        for key in parameters.keys():
            data[key] = self.get(key=key, **kwargs)

        return call(**data)


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
