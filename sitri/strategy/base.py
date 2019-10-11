from abc import ABCMeta, abstractmethod


class BaseStrategy(metaclass=ABCMeta):
    """ Base class for strategies classes """

    @property
    @abstractmethod
    def strategy_provider_code(self) -> str:
        """Code for strategy manager"""

        pass

    @abstractmethod
    def get(self, *args, **kwargs):
        """Get value by strategy"""

        pass
