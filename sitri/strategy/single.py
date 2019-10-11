from .base import BaseStrategy
from ..base import BaseProvider


class SingleStrategy(BaseStrategy):
    strategy_provider_code = "single"

    def __init__(self, data_provider: BaseProvider) -> None:
        self.provider = data_provider

    def get(self, *args, **kwargs):
        return self.provider.get(*args, **kwargs)