from concreteAggregate import ConcreteAggregate

aggregate = ConcreteAggregate()
aggregate.addItem("item 1")
aggregate.addItem("item 2")
aggregate.addItem("item 3")
iterator = aggregate.createIterator()
item = iterator.first()
print("item: ", item)
while not iterator.isDone():
    item = iterator.next()
    print("item: ", item)
