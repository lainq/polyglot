import os
import json
import yaml
import toml

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
                Ignore(self.ignore).create_ignore_files(
                    self.files, self.directory))

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
                    if filename.startswith(os.path.join(
                            self.directory, ".git")):
                        continue
                    filenames.append(os.path.join(root, filename))

        return filenames

    def show(self,
             language_detection_file=None,
             display=True,
             fmt=None,
             output=None):
        DEFAULT_LANGUAGE_DETECTION_FILE = "language.yml"
        if language_detection_file is None:
            for filename in os.listdir(os.getcwd()):
                if filename == DEFAULT_LANGUAGE_DETECTION_FILE and os.path.isfile(
                        filename):
                    language_detection_file = os.path.join(
                        os.getcwd(), filename)
                    break

        extensions = Extensions(language_detection_file, display, self.files)
        data = extensions.get_extension_data()

        result = Result(data).show_file_information()
        if display and fmt is None:
            display_text = Display(result)
        elif display and fmt is not None:
            if fmt.lower() == 'l':
                result['files'] = {}
                display_text = Display(result)
            elif fmt.lower() == 'f':
                result['lines'] = {}
                display_text = Display(result)

        if isinstance(output, str):
            with open(output, mode="w", encoding="utf8") as output_logger:
                if output.endswith(".yml") or output.endswith(".yaml"):
                    yaml.dump(result, output_logger, allow_unicode=True)
                elif output.endswith(".toml"):
                    output_logger.write(toml.dumps(result))
                else:
                    output_logger.write(json.dumps(result, indent=4))

        return result
