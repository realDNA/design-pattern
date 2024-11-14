from abc import ABC, abstractmethod
from product import Hamburgur

class HamburgurStore(ABC):
    
    @abstractmethod
    def createHamburgur(self, type: str) -> Hamburgur:
        pass

    def orderHamburgur(self, type: str) -> Hamburgur:
        hamburgur = self.createHamburgur(type)
        print(hamburgur.prepare())
        print(hamburgur.cook())
        print(hamburgur.box())
        return hamburgur
