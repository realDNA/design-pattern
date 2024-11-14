from concreteCreator import BeefMealFactory, ChikenMealFactory
from director import Meal

beefFactory = BeefMealFactory()
chickenFactory = ChikenMealFactory()

beefMeal = Meal(beefFactory)
chickenMeal = Meal(chickenFactory)

beefMeal.serve()
chickenMeal.serve()
