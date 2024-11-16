class DVDPlayer:
    def on(self):
        print("DVD Player is on")

    def play(self, movie):
        print(f"play movie: {movie}")

    def off(self):
        print("DVD Player is off")


class Projector:
    def on(self):
        print("Projector is on")

    def off(self):
        print("Projector is off")


class SoundSystem:
    def on(self):
        print("Sound system is on")

    def off(self):
        print("Sound system is off")

    def setVolume(self, level):
        print(f"Setting Volume to {level}")


class Lights:
    def dim(self, level):
        print(f"Dimming lights to {level} %")
