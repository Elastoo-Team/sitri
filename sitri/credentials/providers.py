import typing
from abc import ABC

from ..base import BaseProvider


class CredentialProvider(ABC, BaseProvider):
    pass


class CredentialProviderManager:
    @staticmethod
    def get_by_code(code: str) -> typing.Optional[typing.Type[CredentialProvider]]:
        for provider in CredentialProvider.__subclasses__():
            if provider.provider_code == code:
                return provider
        return None
