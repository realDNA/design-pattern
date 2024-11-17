from iterator import Iterator


class ConcreteIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def first(self):
        self._index = 0
        return self._collection[self._index]

    def next(self):
        self._index += 1
        if not self.isDone():
            return self._collection[self._index]
        return None

    def isDone(self):
        return self._index >= len(self._collection)

    def currentItem(self):
        if not self.isDone():
            return self._collection[self._index]
        return None
