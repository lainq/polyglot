import os
import stat
class Polyglot(object):
    def __init__(self, directory_name:str):
        self.directory = Polyglot.find_directory_path(directory_name)
        self.files = self.__find_directory_files(self.directory)

    @staticmethod
    def find_directory_path(directory_path:str):
        assert isinstance(directory_path, str), "Path expected to be a string"
        if directory_path == ".":
            return os.getcwd()

        if os.path.isdir(directory_path):
            return directory_path

        raise FileNotFoundError(f"{directory_path} does not exist")

    def __find_hidden_files(self, hidden, filepath):
        hidden_root = [
            str(filepath).startswith(hidden_file) for hidden_file in hidden
        ]
        return True in hidden_root

    def __find_directory_files(self, directory):
        filenames = []
        hidden_directories = []
        for (root,dirs,files) in os.walk(directory, topdown=True):
            if Polyglot.is_hidden_directory(root):
                hidden_directories.append(root)

            if not self.__find_hidden_files(hidden_directories, root):
                for filename in files:
                    filenames.append(os.path.join(root, filename))

        return filenames


    @staticmethod
    def is_hidden_directory(filepath):
        assert isinstance(filepath, str), "Expected a string"
        return bool(os.stat(filepath).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)
