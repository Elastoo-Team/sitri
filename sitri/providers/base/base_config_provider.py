"""
.. module:: config.providers
   :synopsis: Config Base
.. moduleauthor:: Aleksander Lavrov <github.com/egnod>
"""
from __future__ import annotations

import inspect
import typing as t
from abc import ABC, abstractmethod

from sitri.logger import get_default_logger


class ConfigProvider(ABC):
    """Base class for config providers."""

    def __init__(self, logger: t.Any | None = None, *args: t.Any, **kwargs: t.Any) -> None:
        """Default init method for all providers."""

        if not logger:
            logger = get_default_logger(__name__)

        self.logger = logger

    @property
    @abstractmethod
    def provider_code(self) -> str:
        """Provider code property for identity provider in manager."""

    @abstractmethod
    def get(self, key: str, **kwargs: t.Any) -> t.Any | None:
        """Get value from storage.

        :param key: key for find value in provider source
        :param kwargs: additional arguments for providers
        """

    @abstractmethod
    def keys(self, **kwargs: t.Any) -> t.List[str]:
        """Get keys list in storage."""

    def fill(self, call: t.Callable[[t.Any], t.Any], **kwargs: t.Any) -> t.Any:
        """Fill callable object kwargs if all founded by provider.

        :param call: callable object for fill
        :param kwargs: additional arguments for getting
        """
        parameters = inspect.signature(call).parameters
        data = {}

        for key in parameters.keys():
            data[key] = self.get(key=key, **kwargs)

        return call(**data)


class ConfigProviderManager:
    """Manager for children ConfigProvider classes."""

    @staticmethod
    def get_by_code(code: str) -> t.Type[ConfigProvider] | None:
        """Get config provider by provider_code.

        :param code: provider_code for search config provider
        :Example:
            .. code-block:: python

               ConfigProviderManager.get_by_code("system")
        """
        for provider in ConfigProvider.__subclasses__():
            if provider.provider_code == code:  # type: ignore
                return provider
        return None
