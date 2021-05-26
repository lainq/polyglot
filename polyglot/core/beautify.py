import os
import shutil
from clint.textui import colored
from collections.abc import Iterable

from polyglot.path import DirectoryError


class _ExtensionsionType:
    required_type = Iterable

    def __init__(self, placeholder):
        self.value = placeholder
        self.check_value_type(self.value)

    def check_value_type(self, value):
        """
        Make sure that the key value is an
        iterable, either a tuple, list, string
        or dictionary

        Args:
            value (any): The value to check the type of

        Raises:
            TypeError: Raises a TypeError when the value is not
            an iterable
        """
        if not isinstance(value, self.required_type):
            raise TypeError(colored.red(f"{value} not an iterable"))

    def __repr__(self):
        return self.value


class ExtensionMap(object):
    def __init__(self, extensions={}):
        assert isinstance(extensions, dict), "Extensions expected to be a dict"
        self.extensions = {}
        self.__add_all_extensions(extensions)

    def __add_all_extensions(self, extensions):
        """
        Add all the extensions from the dict passed
        in as a parameter

        Args:
            extensions (dict): The dict to copy
        """
        for key in extensions:
            _ExtensionsionType(extensions[key])
        self.extensions = extensions

    def add(self, folder, extensions):
        """
        Add a new folder to the extension map with its
        associated extension array

        Args:
            folder (string): The name of the folder
            extensions (Iterable): The extensions to search for

        Raises:
            KeyError: Raises an error when the key already
            exists in the map
        """
        if self.extensions.get(folder):
            raise KeyError(f"{folder} already exists in the map")

        _ExtensionsionType(extensions)
        self.extensions.setdefault(folder, extensions)

    def remove(self, folder):
        if folder not in self.extensions:
            raise KeyError(f"{folder} does not exist")

        del self.extensions[folder]

    def get(self):
        return self.extensions

    def __repr__(self):
        return str(self.extensions)

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return len(self.extensions)


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


class _Logs(object):
    def __init__(self, log):
        self.log_messages = log
        self.counter = 0

    def log(self, message, critical=False):
        color = colored.red if critical else colored.green
        if self.log_messages:
            self.counter += 1
            print(color(f"LOG[{self.counter}] {message}"))


class Beautify(object):
    def __init__(self, directory, extensions, prompt=True, log=True):
        assert isinstance(
            extensions, ExtensionMap
        ), "extensions expected to be an extension map"

        self.directory = self.__is_directory(directory)
        self.extensions = extensions
        self.log = _Logs(log)

        self.clean_directory(prompt)

    def clean_directory(self, prompt):
        if prompt:
            data = _Prompt(
                "Do you want to clear the directory", ["y", "n"]
            ).create_prompt()
            if data:
                self.__clean()

            return None

        self.__clean()

    def __clean(self):
        replace_files = {}
        data = self.extensions.get()
        for filename in os.listdir(self.directory):
            folder = self.__get_extension_folder(filename, data)
            if not folder:
                continue

            path = os.path.join(self.directory, folder)
            move_location = os.path.join(path, filename)

            if not os.path.exists(path) or not os.path.isdir(path):
                os.mkdir(path)

            shutil.move(os.path.join(self.directory, filename), move_location)
            self.log.log(
                f"Moved Successfully [{os.path.join(self.directory, filename)} => {move_location}]"
            )

    def __get_extension_folder(self, extension, data):
        for foldername in data:
            extension_list = data[foldername]
            for file_extension in extension_list:
                if extension.endswith(file_extension):
                    return foldername
        return None

    def __is_directory(self, directory):
        is_directory = os.path.isdir(directory)
        if not is_directory:
            raise DirectoryError(f"{directory} not a directory")

        return directory
