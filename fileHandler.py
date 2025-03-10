from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

class TextFileHandler(FileHandler):
    def read(self):
        return "Reading text data..."

    def write(self, data):
        return f"Writing text:{data}"

class BinaryFileHandler(FileHandler):
    def read(self):
        return "Reading binary data..."

    def write(self, data):
        return f"Write bytes:{data}"
