import os

from polyglot.path import DirectoryError

class ExtensionMap(object):
    def __init__(self, extensions={}):
        assert isinstance(extensions, dict), "Extensions expected to be a dict"
        self.extensions = {}
        self.__add_all_extensions(extensions)

    def __add_all_extensions(self, extensions):
        self.extensions = extensions

    def add(self, folder, extensions):
        if self.extensions.get(folder):
            raise KeyError(f"{folder} already exists in the map")

        self.extensions.setdefault(folder, extensions)

    def remove(self, folder):
        if folder not in self.extensions:
            raise KeyError(f"{folder} does not exist")

        del self.extensions[folder]

    def get(self):
        return self.extensions


class _Prompt(object):
    def __init__(self, prompt, options, require=True):
        self.prompt = prompt
        self.options = options
        self.require = require

    def create_prompt(self):
        data = None
        while data not in self.options:
            data = input(f"{self.prompt} (y/n) ")
        return data == "y"


class Beautify(object):
    def __init__(self, directory, extensions, prompt=True):
        assert isinstance(extensions, (dict, ExtensionMap))

        self.directory = self.__is_directory(directory)
        self.extensions = extensions

        self.clean_directory(prompt)

    def clean_directory(self, prompt):
        if prompt:
            data = _Prompt("Do you want to clear the directory",
                             ["y", "n"]).create_prompt()
            if data:
                self.__clean()

            return None

        self.__clean()

    def __clean(self):
        print("LOl")

    def __is_directory(self, directory):
        is_directory = os.path.isdir(directory)
        if not is_directory:
            raise DirectoryError(f"{directory} not a directory")

        return directory
