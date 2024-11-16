from component import FileSystemComponent


class Directory(FileSystemComponent):

    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def getSize(self):
        totalSize = 0

        for child in self.children:
            totalSize += child.getSize()

        return totalSize

    def display(self, indent=0):
        print(' '*indent + f"Directory: {self.name}")
        for child in self.children:
            child.display(indent=indent+2)
