from condiment_decorator import CondimentDecorator


class Mocha(CondimentDecorator):

    def get_description(self):
        return self._beverage.get_description() + " - Mocha"

    def cost(self):
        return self._beverage.cost() + 10
