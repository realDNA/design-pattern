from subject import Image
from concreateSubject import RealImage


class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.realImage = None

    def display(self):
        if not self.realImage:
            self.realImage = RealImage(self.filename)

        self.realImage.display()
