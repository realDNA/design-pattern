from decoratorp import CoffeeDecorator


class Milk(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1.5

    def description(self):
        return self._coffee.description() + ', Milk'


class Sugar(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.5

    def description(self):
        return self._coffee.description() + ', Sugar'


class WhippedCream(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2.0

    def description(self):
        return self._coffee.description() + ', Whipped Cream'
