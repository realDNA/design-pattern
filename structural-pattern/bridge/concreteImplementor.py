from implementor import Preparation


class GrilledPreparation(Preparation):

    def prepare(self):
        return "Preparing Ingredients for grilled hamburgur"

    def cook(self):
        return "Grilling the hamburgur"

    def box(self):
        return "Boxing the grilled hamburgur"


class FriedPreparation(Preparation):

    def prepare(self):
        return "Preparing Ingredients for fried hamburgur"

    def cook(self):
        return "Frying the hamburgur"

    def box(self):
        return "Boxing the fried hamburgur"
