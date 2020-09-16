import typing
from abc import ABCMeta, abstractmethod


class BaseProvider(metaclass=ABCMeta):
    """Base Provider for config and credential providers."""

    @property
    @abstractmethod
    def provider_code(self) -> str:
        """Provider code property for identity provider in manager."""

    @abstractmethod
    def get(self, key: str, **kwargs) -> typing.Optional[typing.Any]:
        """Get value from storage.

        :param key: key for get value
        :param kwargs: additional arguments for providers
        """

    def keys(self, **kwargs) -> typing.List[str]:
        """Get keys list in storage."""
        raise NotImplementedError("keys method not impl for this provider!")
