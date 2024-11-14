from target import Hamburgur
from adaptee import VeggieBurgur


class VeggieBurgurAdaptor(Hamburgur):
    def __init__(self, veggieBurgur: VeggieBurgur):
        self.veggieBurgur = veggieBurgur

    def prepare(self):
        return self.veggieBurgur.prepareVeggie()

    def cook(self):
        return self.veggieBurgur.cookVeggie()

    def box(self):
        return self.veggieBurgur.boxVeggie()
