from concreteCreator import Hamburgur

originalHamburgur = Hamburgur("sesame", "beef", "BBQ", ["A", "B", "C"])
print("originalHamburgur: ", originalHamburgur)
clonedHamburgur = originalHamburgur.clone()
clonedHamburgur.bun = "whole grain"
clonedHamburgur.patty = "chicken"
clonedHamburgur.sauce = "mayo"
clonedHamburgur.toppings = ["E", "F", "G"]
print("cloned Hamburgur: ", clonedHamburgur)
print("original Hamburgur: ", originalHamburgur)
