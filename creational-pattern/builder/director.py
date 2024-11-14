from creator import HamburgurBuilder


class HamburgurDirector:
    def __init__(self, builder: HamburgurBuilder):
        self.builder = builder

    def constructHamburgur(self):
        return (self.builder.addBun().addPatty().addSauce().addToppings().getHamburgur())
