import os
import stat

from polyglot.core.extension import Extensions
from polyglot.core.result import Result
from polyglot.core.display import Display

from polyglot.exceptions.exceptions import (
    PolyglotFileNotFoundError
)

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

    def __init__(self, directory_name: str, ignore=[]):
        assert isinstance(ignore, list), "Expected to be a list"
        self.ignore = ignore
        self.directory = Polyglot.find_directory_path(directory_name)
        self.files = self.__find_directory_files(self.directory)

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

    def __find_directory_files(self, directory):
        """
        Find all the files by walking through
        the directory tree
        """
        filenames = []
        hidden_directories = []
        for (root, dirs, files) in os.walk(directory, topdown=True):
            if Polyglot.is_hidden_directory(root):
                hidden_directories.append(root)

            if not self.__find_hidden_files(hidden_directories, root):
                for filename in files:
                    if filename in self.ignore:
                        continue
                    filenames.append(os.path.join(root, filename))

        return filenames

    @staticmethod
    def is_hidden_directory(filepath):
        assert isinstance(filepath, str), "Expected a string"
        return bool(
            os.stat(filepath).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)

    def show(self, language_detection_file=None, display=False):
        extensions = Extensions(language_detection_file, display, self.files)
        data = extensions.get_extension_data()

        result = Result(data).show_file_information()
        if display:
            display_text = Display(result)
        return result