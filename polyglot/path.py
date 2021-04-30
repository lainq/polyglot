import os
from clint.textui import colored

class Log(object):
    def __init__(self, message, critical=False):
        pass

class _Stat(object):
    def __init__(self, path):
        self.path = path

        self.parent = os.path.dirname(path)
        self.basename = os.path.basename(path)
        self.directory = os.path.isdir(path)
        self.file = os.path.isfile(path)
        self.absolute = os.path.abspath(path)

    def __repr__(self):
        return str({
            "parent" : self.parent,
            "basename" : self.basename,
            "directory" : self.directory,
            "file" : self.file,
            "abs" : self.absolute
        })

    def __str__(self):
        return self.__repr__()

class PolyglotPath(object):
    def __init__(self, path=None):
        self.directory = self.__find_directory_path(path)

    def __find_directory_path(self, path):
        if path == "." or path == None:
            return os.getcwd()

        return path

    @property
    def is_directory(self):
        return os.path.isdir(self.directory)

    def touch(self, create_files, log=True):
        pass

    @property
    def parent(self):
        return os.path.dirname(self.directory)

    @property
    def stat(self):
        return _Stat(self.directory)

    def __repr__(self):
        return str(self.directory)

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        if not os.path.isdir(self.directory):
            return -1
        
        return len(os.listdir(self.directory))

    