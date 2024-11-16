from abc import ABC, abstractmethod


class FileSystemComponent:

    @abstractmethod
    def getSize(self):
        pass

    @abstractmethod
    def display(self):
        pass
