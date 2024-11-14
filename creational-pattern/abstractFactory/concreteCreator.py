from product import Hamburgur, Drink
from creator import FastFoodFactory
from concreteProduct import BeefHamburgur, ChickenHamburgur, Cola, Lemonade

class BeefMealFactory(FastFoodFactory):

    def createHamburgur(self) -> Hamburgur:
        return BeefHamburgur()

    def createDrink(self) -> Drink:
        return Cola()
    
class ChikenMealFactory(FastFoodFactory):

    def createHamburgur(self) -> Hamburgur:
        return ChickenHamburgur()

    def createDrink(self) -> Drink:
        return Lemonade()