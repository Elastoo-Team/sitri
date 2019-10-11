from .base import BaseStrategy
from ..base import BaseProvider
import typing


class IndexPriorityStrategy(BaseStrategy):
    """Get value from providers with priority by index in tuple"""

    strategy_provider_code = "single"

    def __init__(self, data_providers: typing.Tuple[BaseProvider]) -> None:
        """
        :param data_providers: config or credential providers
        """

        self.providers = data_providers

    def get(self, *args, **kwargs):
        """Get value by index priority strategy

        :param args: any args for providers
        :param kwargs: any kwargs for providers
        """
        for provider in self.providers:
            result = provider.get(*args, **kwargs)

            if result:
                return result