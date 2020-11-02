import typing

from .. import ConfigProvider, CredentialProvider
from .base import BaseStrategy


class SingleStrategy(BaseStrategy):
    provider_code = "single"

    def __init__(self, data_provider: typing.Union[ConfigProvider, CredentialProvider]) -> None:
        self.provider = data_provider

    def get(self, *args, **kwargs):
        return self.provider.get(*args, **kwargs)

    def __getattribute__(self, item):
        try:
            return super().__getattribute__(item)

        except AttributeError:
            return self.provider.__getattribute__(item)
