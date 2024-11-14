from creator import Prototype
import copy


class Hamburgur(Prototype):

    def __init__(self, bun, patty, sauce, toppings):
        self.bun = bun
        self.patty = patty
        self.sauce = sauce
        self.toppings = toppings

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return (f"Hamburgur with {self.bun} bun, {self.patty}, {self.sauce}, {','.join(self.toppings)}")
