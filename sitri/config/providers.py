"""
.. module:: config.providers
   :synopsis: Config Base
.. moduleauthor:: Aleksander Lavrov <github.com/egnod>
"""


import typing
from abc import ABC

from ..base import BaseProvider


class ConfigProvider(ABC, BaseProvider):
    """Base class for config providers."""


class ConfigProviderManager:
    """Manager for childeren ConfigProvider classes."""

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
