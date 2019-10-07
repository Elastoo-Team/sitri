"""
.. module:: __init__
   :synopsis: General Sitri class
.. moduleauthor:: Aleksander Lavrov <github.com/egnod>
"""


import typing

from .config.providers import ConfigProvider, ConfigProviderManager
from .credentials.providers import CredentialProvider, CredentialProviderManager


class Sitri:
    """Class for unite credential and config provider
    """

    def __init__(self, credential_provider: CredentialProvider = None, config_provider: ConfigProvider = None):
        """

        :param credential_provider: object of credential provider
        :param config_provider: object of config provider
        """
        if not credential_provider or not config_provider:
            raise RuntimeError("Provider not found!")

        self.credential_provider = credential_provider
        self.config_provider = config_provider

    def get_credential(self, key: str, default: typing.Any = None) -> typing.Union[typing.Any, None]:
        """Get value from credential provider

        :param key: key for credential provider
        :param default: if provider return None
        """
        variable = self.credential_provider.get(key)

        return variable if variable else default

    def get_config(self, key: str, default: typing.Any = None) -> typing.Union[typing.Any, None]:
        """Get value from config provider

        :param key: key for config provider
        :param default: if provider return None
        """
        variable = self.config_provider.get(key)

        return variable if variable else default
