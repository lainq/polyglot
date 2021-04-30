import os

class PolyglotPath(object):
    def __init__(self, path=None):
        self.directory = self.__find_directory_path(path)

    def __find_directory_path(self, path):
        if path == "." or path == None:
            return os.getcwd()

        return path

    def __repr__(self):
        return str(self.directory)

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        if not os.path.isdir(self.directory):
            return -1
        
        return len(os.listdir(self.directory))

    