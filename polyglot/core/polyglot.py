import os
import stat

from polyglot.core.extension import Extensions
from polyglot.core.result import Result
from polyglot.core.display import Display
from polyglot.core.ignore import Ignore

from polyglot.exceptions.exceptions import (PolyglotFileNotFoundError)


class Polyglot(object):
    """
    The main polyglot class. An instance of this class
    is created by the user to use the core functions of
    the module

    Attributes:
        ignore -- The files to ignore
        directory -- The abspath of the directory to check
        files -- All the files inside of the directory

    """
    def __init__(self, directory_name: str, ignore=None):
        assert ignore == None or isinstance(
            ignore, str), "Expected to be a string or None"
        self.ignore = ignore
        self.directory = Polyglot.find_directory_path(directory_name)
        self.files = self.find_directory_files(self.directory)

        if self.ignore:
            self.files = Ignore.remove_specific_list_element(
                self.files,
                Ignore(self.ignore).create_ignore_files(self.files, self.directory))

    @staticmethod
    def find_directory_path(directory_path: str):
        """
        Determine the directory path based on
        the parameter. If the path is a dot(.) return the
        current working directory, else return 
        the path if the path is a directory, else
        throw an error
        """
        assert isinstance(directory_path, str), "Path expected to be a string"
        if directory_path == ".":
            return os.getcwd()

        if os.path.isdir(directory_path):
            return directory_path

        raise PolyglotFileNotFoundError(f"{directory_path} does not exist")

    def __find_hidden_files(self, hidden, filepath):
        """
        Make sure that the root of the file
        is not hidden
        """
        hidden_root = [
            str(filepath).startswith(hidden_file) for hidden_file in hidden
        ]
        return True in hidden_root

    def find_directory_files(self, directory):
        """
        Find all the files by walking through
        the directory tree
        """
        filenames = []
        hidden_directories = []
        for (root, dirs, files) in os.walk(directory, topdown=True):
            if not self.__find_hidden_files(hidden_directories, root):
                for filename in files:
                    if filename.startswith(os.path.join(self.directory, ".git")):
                        continue
                    filenames.append(os.path.join(root, filename))

        return filenames

    def show(self, language_detection_file=None, display=True):
        DEFAULT_LANGUAGE_DETECTION_FILE = "./language.yml"
        if language_detection_file is None and os.path.isfile(DEFAULT_LANGUAGE_DETECTION_FILE):
            language_detection_file = DEFAULT_LANGUAGE_DETECTION_FILE

        extensions = Extensions(language_detection_file, display, self.files)
        data = extensions.get_extension_data()

        result = Result(data).show_file_information()
        if display:
            display_text = Display(result)
        return result
