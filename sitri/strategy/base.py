from abc import ABCMeta, abstractmethod
from typing import Any


class BaseStrategy(metaclass=ABCMeta):
    """Base class for strategies classes."""

    @property
    @abstractmethod
    def provider_code(self) -> str:
        """Code for strategy manager."""

    @abstractmethod
    def get(self, *args: Any, **kwargs: Any) -> Any:
        """Get value by strategy."""
