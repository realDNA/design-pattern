class Hamburgur:
    def __init__(self):
        self.bun = None
        self.patty = None
        self.sauce = None
        self.toppings = []
    
    def __str__(self):
        return f"Hamburgur with {self.bun} bun, {self.patty} patty, {self.sauce} sauce, and toppings: {','.join(self.toppings)}"