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

        self.ignore_files = {"files":[],"dirs":[], "ext":[]}
        self.ignore_list_filename = ignore_list_filename
        self.ignore_data = self.read_file(self.ignore_list_filename)


    def __find_all_files(ignore_files, ignore_extensions, files):
        for filename_index in range(len(files)):
            current_filename = files[filename_index]
            file_extension = current_filename.split(".")[-1]
            if current_filename.enswith(file_extension):
                ignore_files.append(current_filename)
        return ignore_files

    def read_file(self, read_file_name, ignore_text=True):
        if not os.path.exists(read_file_name) or not os.path.isfile(read_file_name):
            raise IgnoreFileError(f"{read_file_name} is not a valid file")

        if ignore_text and not read_file_name.endswith(".polyglot"):
            raise PolyglotExtensionError(f"Ignore files require to have a .polyglot file extension")

        with open(read_file_name, "r") as file_reader:
            file_data = file_reader.read().split("\n")

            if not ignore_text:
                return file_data
            
            return self.remove_specific_list_element(
                [(filename if len(filename.strip()) > 0 else None) for filename in file_data],
                None
            )
    
    def remove_specific_list_element(self, list_data, remove_element):
        assert isinstance(list_data, list)
        return_array = []
        for element in list_data:
            if element != remove_element:
                return_array.append(element)
        
        return return_array
    