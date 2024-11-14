from concreteImplementor import GrilledPreparation, FriedPreparation
from refinedAbstraction import BeefHamburgur, ChickenHamburgur

grilledPreparation = GrilledPreparation()
friedPreparation = FriedPreparation()
beefHamburgurGrilled = BeefHamburgur(grilledPreparation)
beefHamburgurFried = BeefHamburgur(friedPreparation)
chickenHamburgurGrilled = ChickenHamburgur(grilledPreparation)
chickenHamburgurFried = ChickenHamburgur(friedPreparation)

print(beefHamburgurGrilled.serve())
print(beefHamburgurFried.serve())
print(chickenHamburgurGrilled.serve())
print(chickenHamburgurFried.serve())