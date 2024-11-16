from concreteComponent import BasicCoffee
from concreteDecorator import Milk, Sugar, WhippedCream

coffee = BasicCoffee()
print(f"{coffee.description()}: {coffee.cost()}")

coffeeWithMilk = Milk(coffee)
print(f"{coffeeWithMilk.description()}: {coffeeWithMilk.cost()}")

coffeeWithSugarAndMilk = Sugar(coffeeWithMilk)
print(f"{coffeeWithSugarAndMilk.description()}: {coffeeWithSugarAndMilk.cost()}")

coffeeWithAll = WhippedCream(coffeeWithSugarAndMilk)
print(f"{coffeeWithAll.description()}: {coffeeWithAll.cost()}")
