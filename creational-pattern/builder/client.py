from concreteCreator import BeefHamburgurBuilder, ChickenHamburgurBuilder
from director import HamburgurDirector

beefBuilder = BeefHamburgurBuilder()
chickenBuilder = ChickenHamburgurBuilder()
director = HamburgurDirector(beefBuilder)
beefHamburgur = director.constructHamburgur()
print(beefHamburgur)
director = HamburgurDirector(chickenBuilder)
chickenHamburgur = director.constructHamburgur()
print(chickenHamburgur)