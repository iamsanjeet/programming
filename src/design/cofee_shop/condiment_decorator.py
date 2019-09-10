from abc import ABC, abstractmethod
from beverage import Beverage


class CondimentDecorator(Beverage):
    _beverage = None

    def __init__(self, b):
        self._beverage = b

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def cost(self):
        pass
