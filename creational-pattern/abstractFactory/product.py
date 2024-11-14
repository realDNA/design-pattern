from abc import abstractmethod, ABC

class Hamburgur(ABC):

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def box(self):
        pass

class Drink(ABC):

    @abstractmethod
    def pour(self):
        pass