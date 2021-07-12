import os
from clint.textui import colored


class IgnoreFileError(FileNotFoundError):
    def __init__(self, message_data):
        self.error_message = colored.red(message_data.strip())
        super().__init__(self.error_message)


class PolyglotExtensionError(Exception):
    def __init__(self, message_data):
        self.error_message = colored.red(message_data.strip())
        super().__init__(self.error_message)


class Ignore(object):
    def __init__(self, ignore_list_filename):
        assert isinstance(ignore_list_filename, str)

        self.ignore_files = []
        self.ignore_list_filename = ignore_list_filename
        self.ignore_data = self.read_file(self.ignore_list_filename)

        self.files = None

    def create_ignore_files(self, files, directory):
        """
        Update the ignore files list
        based on information from the polyglot ignore
        file
        """
        self.files = files
        for ignore_data_line in self.ignore_data:
            if ignore_data_line.startswith("."):
                self.__find_file_extension(ignore_data_line)
            elif ignore_data_line.endswith("/"):
                self.find_dir_files(ignore_data_line[:-1])
            elif ignore_data_line.startswith("~"):
                self.add_root_dirs(ignore_data_line[1:], directory)
            else:
                self.add_files(ignore_data_line)

        self.add_root_dirs(".git", directory)
        return self.ignore_files

    def add_root_dirs(self, root, dirname):
        root_directory = os.path.join(dirname, root)
        if not self.files:
            return None

        for filename in self.files:
            if filename.startswith(root_directory):
                self.ignore_files.append(filename)

    def find_dir_files(self, directory_name):
        """
        Get all the files with the directory_name
        as the parent directory
        """
        if not self.files:
            return None
        for filename in self.files:
            dirname = os.path.basename(os.path.dirname(filename))
            if dirname == directory_name:
                self.ignore_files.append(filename)

    def add_files(self, data_line):
        """
        Added other files with the basename as
        the data_line
        """
        if not self.files:
            return None
        for filename in self.files:
            if os.path.basename(filename) == data_line:
                self.ignore_files.append(filename)

    def __find_file_extension(self, extension):
        """
        Add all the files with the specific
        file extension
        """
        if not self.files:
            return None
        for filename in self.files:
            if filename.endswith(extension):
                self.ignore_files.append(filename)

    @staticmethod
    def __find_all_files(ignore_files, ignore_extensions, files):
        for filename_index in range(len(files)):
            current_filename = files[filename_index]
            file_extension = current_filename.split(".")[-1]
            if current_filename.enswith(file_extension):
                ignore_files.append(current_filename)
        return ignore_files

    def read_file(self, read_file_name, ignore_text=True):
        """
        Valiate a file and read the file
        """
        if not os.path.exists(read_file_name) or not os.path.isfile(read_file_name):
            raise IgnoreFileError(f"{read_file_name} is not a valid file")

        if ignore_text and not read_file_name.endswith(".polyglot"):
            raise PolyglotExtensionError(
                f"Ignore files require to have a .polyglot file extension"
            )

        with open(read_file_name, "r") as file_reader:
            file_data = file_reader.read().split("\n")

            if not ignore_text:
                return file_data

            return Ignore.remove_specific_list_element(
                [
                    (filename if len(filename.strip()) > 0 else None)
                    for filename in file_data
                ],
                [None],
            )

    @staticmethod
    def remove_specific_list_element(list_data, remove_element):
        """
        Remove a specific list of elements from another
        list and return the new list
        """
        assert isinstance(list_data, list)
        return_array = []
        for element in list_data:
            if element not in remove_element:
                return_array.append(element)

        return return_array
