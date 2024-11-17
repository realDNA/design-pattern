from abc import ABC, abstractmethod


class Aggregate(ABC):
    @abstractmethod
    def createIterator(self):
        pass
