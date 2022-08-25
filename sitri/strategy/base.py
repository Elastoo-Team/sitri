from __future__ import annotations

import typing as t
from abc import ABCMeta, abstractmethod


class BaseStrategy(metaclass=ABCMeta):
    """Base class for strategies classes."""

    @property
    @abstractmethod
    def provider_code(self) -> str:
        """Code for strategy manager."""

    @abstractmethod
    def get(self, *args: t.Any, **kwargs: t.Any) -> t.Any:
        """Get value by strategy."""
