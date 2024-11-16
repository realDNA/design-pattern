from component import FileSystemComponent


class File(FileSystemComponent):

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def getSize(self):
        return self.size

    def display(self, indent):
        print(' '*indent + f"File: {self.name}, Size: {self.size} bytes")
