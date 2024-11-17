from aggregate import Aggregate
from concreteIterator import ConcreteIterator


class ConcreteAggregate(Aggregate):
    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def createIterator(self):
        return ConcreteIterator(self.items)
