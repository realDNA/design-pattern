from flyweight import FlyWeight


class ConcreteFlyWeight(FlyWeight):

    def __init__(self, intrinsicState):
        self.intrinsicState = intrinsicState

    def operation(self, extrinsicState):
        print(
            f"Intrinsic state: {self.intrinsicState}, Extrinsic state: {extrinsicState}")
