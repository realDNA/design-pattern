from creator import HamburgurStore
from product import Hamburgur
from concreteProduct import BeefHamburgur, ChickenHamburgur

class MyHamburgurStore(HamburgurStore):
    def createHamburgur(self, type: str) -> Hamburgur:
        if type == "beef":
            return BeefHamburgur()
        elif type == "chicken":
            return ChickenHamburgur()
        else:
            raise ValueError("no such product")