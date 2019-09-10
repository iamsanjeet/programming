from beverage import Beverage
from darkroast import DarkRoast
from condiment_decorator import CondimentDecorator
from mocha import Mocha


if __name__ == '__main__':
    b = DarkRoast()
    print(b.get_description())
    print(b.cost())
    bb = Mocha(b)
    print(bb.get_description())
    print(bb.cost())