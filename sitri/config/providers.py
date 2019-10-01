import typing
from abc import ABCMeta, abstractmethod, abstractproperty


class ConfigProvider(metaclass=ABCMeta):
    @abstractproperty
    def provider_code(self) -> str:
        pass

    @abstractmethod
    def get_variable(self, name: str) -> typing.Union[typing.Any, None]:
        pass

    @abstractmethod
    def get_variables_list(self) -> typing.List[typing.Any]:
        pass


class ConfigProviderManager:
    @staticmethod
    def get_by_code(code: str) -> typing.Union[ConfigProvider, None]:
        for provider in ConfigProvider.__subclasses__():
            if provider.provider_code == code:
                return provider
