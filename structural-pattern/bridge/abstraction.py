from implementor import Preparation


class Hamburgur:

    def __init__(self, preparation: Preparation):
        self.preparation = preparation

    def prepare(self):
        return self.preparation.prepare()

    def cook(self):
        return self.preparation.cook()

    def box(self):
        return self.preparation.box()
