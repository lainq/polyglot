import os

from polyglot.path import DirectoryError


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
        self.directory = self.__is_directory(directory)
        self.extensions = extensions

        self.clean_directory(prompt)

    def clean_directory(self, prompt):
        if prompt:
            prompt = _Prompt("Do you want to clear the directory",
                             ["y", "n"]).create_prompt()
            if prompt:
                self.__clean()
                return None

        self.__clean()

    def __clean(self):
        pass

    def __is_directory(self, directory):
        is_directory = os.path.isdir(directory)
        if not is_directory:
            raise DirectoryError(f"{directory} not a directory")

        return directory
