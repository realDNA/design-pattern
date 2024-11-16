from subject import Image


class RealImage(Image):

    def __init__(self, filename):
        self.filename = filename
        self.loadImageFromDisk()

    def loadImageFromDisk(self):
        print(f"Loading Image From Disk: {self.filename}")

    def display(self):
        print(f"Displaying Image: {self.filename}")
