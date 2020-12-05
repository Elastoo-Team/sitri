from sitri.providers.base import ConfigProvider
from sitri.strategy.base import BaseStrategy


class SingleStrategy(BaseStrategy):
    provider_code = "single"

    def __init__(self, data_provider: ConfigProvider) -> None:
        self.provider = data_provider

    def get(self, *args, **kwargs):
        return self.provider.get(*args, **kwargs)

    def __getattribute__(self, item):
        try:
            return super().__getattribute__(item)

        except AttributeError:
            return self.provider.__getattribute__(item)
