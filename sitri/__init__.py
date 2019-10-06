import typing

from .config.providers import ConfigProvider, ConfigProviderManager
from .credentials.providers import CredentialProvider, CredentialProviderManager


class Sitri:
    def __init__(self, credential_provider: CredentialProvider = None, config_provider: ConfigProvider = None):

        if not credential_provider or not config_provider:
            raise RuntimeError("Provider not found!")

        self.credential_provider = credential_provider
        self.config_provider = config_provider

    def get_credential(self, name: str, default: typing.Any = None) -> typing.Union[typing.Any, None]:
        variable = self.credential_provider.get(name)

        return variable if variable else default

    def get_config(self, name: str, default: typing.Any = None) -> typing.Union[typing.Any, None]:
        variable = self.config_provider.get(name)

        return variable if variable else default
