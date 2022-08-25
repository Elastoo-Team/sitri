from __future__ import annotations

from typing import Any

from sitri.providers.base import ConfigProvider
from sitri.strategy.base import BaseStrategy


class SingleStrategy(BaseStrategy):
    """SingleStrategy."""

    provider_code = "single"

    def __init__(self, data_provider: ConfigProvider) -> None:
        """__init__.

        :param data_provider:
        :type data_provider: ConfigProvider
        :rtype: None
        """
        self.provider = data_provider

    def get(self, *args: Any, **kwargs: Any) -> Any:
        """get.

        :param args:
        :param kwargs:
        """
        return self.provider.get(*args, **kwargs)

    def __getattribute__(self, item: str) -> Any:
        """__getattribute__.

        :param item:
        """
        try:
            return super().__getattribute__(item)

        except AttributeError:
            return self.provider.__getattribute__(item)
