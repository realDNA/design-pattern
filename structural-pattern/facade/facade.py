class HomeTheaterFacade:
    def __init__(self, dvdPlayer, projector, soundSystem, lights):
        self.dvdPlayer = dvdPlayer
        self.projector = projector
        self.soundSystem = soundSystem
        self.lights = lights

    def watchMovie(self, movie):
        print("Get ready to watch a movie")
        self.lights.dim(10)
        self.projector.on()
        self.soundSystem.setVolume(5)
        self.dvdPlayer.on()
        self.dvdPlayer.play(movie)

    def endMovie(self):
        print("Shutting down the home theater")
        self.dvdPlayer.off()
        self.soundSystem.off()
        self.projector.off()
        self.lights.dim(100)
