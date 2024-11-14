from abc import ABC, abstractmethod

class Preparation(ABC):

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def box(self):
        pass