import os

from polyglot.path import DirectoryError

class Beautify(object):
    def __init__(self, directory, extensions, prompt=True):
        self.directory = self.__is_directory(directory)
        self.extensions = extensions

        self.clean_directory(prompt)

    def clean_directory(self, prompt):
        pass

    def __is_directory(self, directory):
        is_directory = os.path.isdir(directory)
        if not is_directory:
            raise DirectoryError(f"{directory} not a directory")

        return directory
