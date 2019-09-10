from beverage import Beverage


class DarkRoast(Beverage):
    _description = "Dark Roast"
    _cost = 20

    def get_description(self):
        return self._description

    def cost(self):
        return self._cost


