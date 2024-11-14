from creator import FastFoodFactory


class Meal:
    def __init__(self, factory=FastFoodFactory):
        self.hamburgur = factory.createHamburgur()
        self.drink = factory.createDrink()

    def serve(self):
        # print("self.hamburgur = ", self.hamburgur)
        print(self.hamburgur.prepare())
        print(self.hamburgur.cook())
        print(self.hamburgur.box())
        print(self.drink.pour())
