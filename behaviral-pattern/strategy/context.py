from strategy import PaymentStrategy


class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0

    def addItem(self, item, price):
        self.items.append(item)
        self.total += price

    def pay(self, paymentStrategy: PaymentStrategy):
        paymentStrategy.pay(self.total)
