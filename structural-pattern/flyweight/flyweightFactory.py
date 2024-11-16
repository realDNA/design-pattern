from concreteFlyWeight import ConcreteFlyWeight


class FlyWeightFactory:

    def __init__(self):
        self.flyweights = {}

    def getFlyWeight(self, key):
        if key not in self.flyweights:
            self.flyweights[key] = ConcreteFlyWeight(key)

        return self.flyweights[key]

    def listFlyWeights(self):
        print(f"FlyWeights: {list(self.flyweights.keys())}")
