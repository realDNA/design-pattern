from flyweightFactory import FlyWeightFactory

flyWeightFactory = FlyWeightFactory()
flyWeight1 = flyWeightFactory.getFlyWeight("Arial-12-Red")
flyWeight2 = flyWeightFactory.getFlyWeight("Arial-12-Red")
flyWeight3 = flyWeightFactory.getFlyWeight("Times-14-Blue")

flyWeight1.operation("Character A")
flyWeight2.operation("Character B")
flyWeight3.operation("Character C")

flyWeightFactory.listFlyWeights()
