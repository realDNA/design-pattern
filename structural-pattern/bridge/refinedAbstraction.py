from abstraction import Hamburgur
from implementor import Preparation


class BeefHamburgur(Hamburgur):

    def __init__(self, preparation: Preparation):
        super().__init__(preparation)

    def serve(self):
        return f"serving beef hamburgur: {self.prepare()}, {self.cook()}, {self.box()}"


class ChickenHamburgur(Hamburgur):

    def __init__(self, preparation: Preparation):
        super().__init__(preparation)

    def serve(self):
        return f"serving chicken hamburgur: {self.prepare()}, {self.cook()}, {self.box()}"
