from abc import ABC, abstractmethod
from product import Hamburgur

class HamburgurBuilder(ABC):

    @abstractmethod
    def addBun(self):
        pass

    @abstractmethod
    def addPatty(self):
        pass

    @abstractmethod
    def addSauce(self):
        pass

    @abstractmethod
    def addToppings(self):
        pass

    @abstractmethod
    def getHamburgur(self) -> Hamburgur:
        pass