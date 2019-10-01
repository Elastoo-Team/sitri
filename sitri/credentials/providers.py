import typing
from abc import ABCMeta, abstractmethod, abstractproperty


class CredentialProvider(metaclass=ABCMeta):
    @abstractproperty
    def provider_code(self) -> str:
        pass

    @abstractmethod
    def get_credential(self, identifier: str) -> typing.Any:
        pass


class CredentialProviderManager:
    @staticmethod
    def get_by_code(code: str) -> typing.Union[CredentialProvider, None]:
        for provider in CredentialProvider.__subclasses__():
            if provider.provider_code == code:
                return provider
