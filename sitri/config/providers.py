import typing
from abc import ABC

from ..base import BaseProvider


class ConfigProvider(ABC, BaseProvider):
    pass


class ConfigProviderManager:
    @staticmethod
    def get_by_code(code: str) -> typing.Optional[typing.Type[ConfigProvider]]:
        for provider in ConfigProvider.__subclasses__():
            if provider.provider_code == code:
                return provider
        return None
