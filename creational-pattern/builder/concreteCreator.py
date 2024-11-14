from creator import HamburgurBuilder
from product import Hamburgur


class BeefHamburgurBuilder(HamburgurBuilder):

    def __init__(self):
        self.hamburgur = Hamburgur()

    def addBun(self):
        self.hamburgur.bun = "sesame"
        return self

    def addPatty(self):
        self.hamburgur.patty = "beef"
        return self

    def addSauce(self):
        self.hamburgur.sauce = "BBQ"
        return self

    def addToppings(self):
        self.hamburgur.toppings.extend(["A", "B", "C", "D"])
        return self

    def getHamburgur(self) -> Hamburgur:
        return self.hamburgur


class ChickenHamburgurBuilder(HamburgurBuilder):

    def __init__(self):
        self.hamburgur = Hamburgur()

    def addBun(self):
        self.hamburgur.bun = "plain"
        return self

    def addPatty(self):
        self.hamburgur.patty = "chicken"
        return self

    def addSauce(self):
        self.hamburgur.sauce = "tomato"
        return self

    def addToppings(self):
        self.hamburgur.toppings.extend(["A", "B", "C", "D"])
        return self

    def getHamburgur(self) -> Hamburgur:
        return self.hamburgur
