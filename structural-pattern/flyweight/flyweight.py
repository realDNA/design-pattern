from abc import ABC, abstractmethod


class FlyWeight(ABC):

    @abstractmethod
    def operation(self, extrinsicState):
        pass
