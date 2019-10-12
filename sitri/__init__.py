"""
.. module:: __init__
   :synopsis: General Sitri class
.. moduleauthor:: Aleksander Lavrov <github.com/egnod>
"""


import typing

from .config.providers import ConfigProvider, ConfigProviderManager
from .credentials.providers import CredentialProvider, CredentialProviderManager
from .strategy.base import BaseStrategy
from .strategy.single import SingleStrategy


class Sitri:
    """Class for unite credential and config provider
    """

    def __init__(
        self,
        credential_provider: typing.Union[CredentialProvider, BaseStrategy],
        config_provider: typing.Union[ConfigProvider, BaseStrategy],
    ):
        """

        :param credential_provider: object of credential provider
        :param config_provider: object of config provider
        """

        if isinstance(credential_provider, BaseStrategy):
            self.credential = credential_provider

        else:
            self.credential = SingleStrategy(credential_provider)

        if isinstance(config_provider, BaseStrategy):
            self.config = config_provider

        else:
            self.config = SingleStrategy(config_provider)

    def get_credential(self, key: str, default: typing.Any = None, **kwargs) -> typing.Union[typing.Any, None]:
        """Get value from credential provider

        :param key: key for credential provider
        :param default: if provider return None
        """
        variable = self.credential.get(key, **kwargs)

        return variable if variable else default

    def get_config(self, key: str, default: typing.Any = None, **kwargs) -> typing.Union[typing.Any, None]:
        """Get value from config provider

        :param key: key for config provider
        :param default: if provider return None
        """
        variable = self.config.get(key, **kwargs)

        return variable if variable else default
