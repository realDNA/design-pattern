from target import Hamburgur

def serveHamburgur(hamburgur: Hamburgur):
    print(hamburgur.prepare())
    print(hamburgur.cook())
    print(hamburgur.box())