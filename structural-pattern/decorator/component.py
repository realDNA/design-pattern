from abc import ABC, abstractmethod


class Coffee(ABC):

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass
