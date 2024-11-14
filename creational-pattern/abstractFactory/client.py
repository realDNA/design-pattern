from concreteCreator import BeefMealFactory, ChikenMealFactory
from server import Meal

beefFactory = BeefMealFactory()
chickenFactory = ChikenMealFactory()

beefMeal = Meal(beefFactory)
chickenMeal = Meal(chickenFactory)

beefMeal.serve()
chickenMeal.serve()
