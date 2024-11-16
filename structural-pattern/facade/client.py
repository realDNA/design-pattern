from subsystem import DVDPlayer, Projector, SoundSystem, Lights
from facade import HomeTheaterFacade

dvdPlayer = DVDPlayer()
projector = Projector()
soundSystem = SoundSystem()
lights = Lights()

homeTheater = HomeTheaterFacade(
    dvdPlayer=dvdPlayer, projector=projector, soundSystem=soundSystem, lights=lights)
homeTheater.watchMovie("Doraemon")
homeTheater.endMovie()
