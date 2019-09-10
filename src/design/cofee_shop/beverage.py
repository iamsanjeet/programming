from abc import ABC, abstractmethod

class Beverage(ABC):
    description = "Unknown Beverage"

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def cost(self):
        pass
