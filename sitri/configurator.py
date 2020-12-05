"""
.. module:: configurator
   :synopsis: General Sitri class
.. moduleauthor:: Aleksander Lavrov <github.com/egnod>
"""


import typing

from loguru import logger

from sitri.providers.base import ConfigProvider
from sitri.strategy.base import BaseStrategy
from sitri.strategy.single import SingleStrategy


class SitriProviderConfigurator:
    """Class for unite config provider."""

    def __init__(
        self,
        config_provider: typing.Union[ConfigProvider, BaseStrategy],
    ):
        """
        :param config_provider: object of config provider
        """

        self.config = None

        if isinstance(config_provider, BaseStrategy):
            self.config = config_provider

        elif config_provider:
            self.config = SingleStrategy(config_provider)

    def get(self, key: str, default: typing.Any = None, **kwargs) -> typing.Union[typing.Any, None]:
        """Get value from config provider.

        :param key: key for config provider
        :param default: if provider return None
        """
        if not self.config:
            logger.info("No config provider")
            return None

        variable = self.config.get(key, **kwargs)

        return variable if variable else default
