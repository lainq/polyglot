import os
import pathlib
import itertools
import clint

class UnknownPathError(FileNotFoundError):
    def __init__(self, error_message):
        self.message = clint.textui.colored.red(error_message)

        super.__init__(self.message)

class Tree(object):
    def __init__(self, directory, ignore_folders=[]):
        self.directory = directory if self.__verify_directory_path(directory) else None

    def __verify_directory_path(self, directory):
        if not os.path.exists(directory) or not os.path.isdir(directory):
            return False

        return True

    def generate(self, level=-1, limit_to_directories=False, length_limit=None):
        if not self.directory:
            raise UnknownPathError(f"Cannot find {self.directory}")

        
