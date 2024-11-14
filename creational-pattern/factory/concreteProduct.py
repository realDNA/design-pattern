from product import Hamburgur

class BeefHamburgur(Hamburgur):
    def prepare(self):
        return "Prepare beef hamburgur"
    
    def cook(self):
        return "Cooking beef hamburgur"
    
    def box(self):
        return "Boxing beef hamburgur"
    
class ChickenHamburgur(Hamburgur):
    def prepare(self):
        return "Prepare chicken hamburgur"
    
    def cook(self):
        return "Cooking chicken hamburgur"
    
    def box(self):
        return "Boxing chicken hamburgur"