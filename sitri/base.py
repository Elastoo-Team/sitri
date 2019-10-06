import typing
from abc import ABCMeta, abstractmethod


class BaseProvider(metaclass=ABCMeta):
    @property
    @abstractmethod
    def provider_code(self) -> str:
        pass

    @abstractmethod
    def get(self, key: str) -> typing.Optional[typing.Any]:
        pass

    def keys(self) -> typing.List[str]:
        raise NotImplementedError("keys method not impl for this provider!")
