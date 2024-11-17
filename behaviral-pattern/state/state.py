from abc import ABC, abstractmethod


class TrafficLightState(ABC):
    @abstractmethod
    def handle(self):
        pass
