from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass
