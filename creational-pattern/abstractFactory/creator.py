from abc import ABC, abstractmethod
from product import Hamburgur, Drink

class FastFoodFactory(ABC):

    @abstractmethod
    def createHamburgur(self) -> Hamburgur:
        pass

    @abstractmethod
    def createDrink(self) -> Drink:
        pass