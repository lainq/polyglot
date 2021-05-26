import os
from clint.textui import colored
from collections.abc import Iterable


class DirectoryError(Exception):
    def __init__(self, error_message):
        self.error_message = colored.red(error_message)

        super().__init__(self.error_message)


class FileContentFilter(object):
    def __init__(self, files=None, folders=None):
        self.__validate_parameter_types(files=files, folders=folders)

        self.files = files
        self.folders = folders

    def __validate_parameter_types(self, **kwargs):
        valid_types = bool
        for parameter_key, value in kwargs.items():
            if not type(value) == valid_types:
                if value == None:
                    continue
                raise TypeError(f"{parameter_key} expected to be of type bool or None")
        return True


class Log(object):
    def __init__(self, message, critical=False):
        self.message = colored.red(message) if critical else colored.cyan(message)
        self.create_message_log(self.message)

    def create_message_log(self, message, end="\n"):
        print(message, end=end)


class _Stat(object):
    def __init__(self, path):
        self.path = path

        self.parent = os.path.dirname(path)
        self.basename = os.path.basename(path)
        self.directory = os.path.isdir(path)
        self.file = os.path.isfile(path)
        self.absolute = os.path.abspath(path)

    def __repr__(self):
        return str(
            {
                "parent": self.parent,
                "basename": self.basename,
                "directory": self.directory,
                "file": self.file,
                "abs": self.absolute,
            }
        )

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
    def basename(self):
        return os.path.basename(self.directory)

    def listdir(self):
        return os.listdir(self.directory)

    @property
    def content(self):
        return self.listdir()

    @property
    def is_directory(self):
        return os.path.isdir(self.directory)

    def touch(self, create_files=[], log=True):
        assert isinstance(
            create_files, Iterable
        ), "Parameter expected to be an iterable"

        for index, filename in enumerate(create_files):
            with open(
                os.path.join(self.directory, filename), "w"
            ) as create_file_writer:
                create_file_writer.write("")

            log = Log(f"{index+1} Created {filename}")

    def mkdirs(self, directories, log=True, overwrite=False):
        assert isinstance(directories, Iterable)

        for index, dirname in enumerate(directories):
            if os.path.exists(dirname) and os.path.isdir(dirname):
                Log(f"{index+1} Failed to create {dirname}", critical=True)
            else:
                os.mkdir(dirname)
                Log(f"{index+1}. Created {dirname}")

    def join(self, *args):
        path = self.directory
        for joinpath in args:
            path = os.path.join(path, joinpath)

        return path

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
