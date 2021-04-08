import os as os
import logging as Logger
import requests
import yaml

LANGUAGE_FILE = "https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml"

# class PolyglotExtension(object):
#     def __init__(self, param):
#         assert isinstance(param, str), "Expected a string"

#         self.parameter = param

#         self.directory_name = self.__get_dir_name(self.parameter)
#         self.files = {}

#     def __get_dir_name(self, param):
#         """Get the directory name pased on the parameter"""
#         if param == ".":
#             return os.getcwd()
#         else:
#             if os.path.isabs(param):
#                 return param
#             else:
#                 return os.path.join(os.getcwd(), param)

#     def __search_language_file(self,
#                                search_file_name="language",
#                                extension="yml"):
#         filename = f"{search_file_name}.{extension}"
#         if filename in os.listdir(self.directory_name):
#             return os.path.join(os.getcwd(), filename)

#         return None

#     def find_files(self, yaml_file):
#         if yaml_file == None:
#             search_yaml_file = self.__search_language_file()
#             if search_yaml_file is not None:
#                 yaml_file = search_yaml_file
#             else:
#                 log_messages = [
#                     Logger.error("Cannot find the language file"),
#                     Logger.warning("Installing the language file")
#                 ]
#                 yaml_file = self.__install_language_file()

#         with open(yaml_file, "r") as yaml_reader:
#             file_content = yaml_file_loader.load(
#                 yaml_reader, Loader=yaml_file_loader.FullLoader)

#         for language in dict(file_content):
#             assert isinstance(file_content[language], dict), "Expected a dict"

#             for key in dict(file_content[language]):
#                 if key != "extensions":
#                     del file_content[language][key]

#         return self.__search_directories(file_content)

#     def __search_directories(self, content):
#         for filename in os.listdir(self.directory_name):
#             if os.path.isfile(filename):
#                 if "." not in filename: continue
#                 extension = f".{str(filename).split('.')[-1]}"
#                 language = self.__determine_language(extension, content)

#                 if language in self.files:
#                     self.files[language].append(filename)
#                 else:
#                     self.files[language] = [filename]
#         return self.files

#     def __determine_language(self, ext, content):
#         for lang in content:
#             if "extensions" in content[lang]:
#                 if str(ext) in content[lang]["extensions"]:
#                     return lang
#         return "Unknown Files"

#     def __install_language_file(self):
#         filename = os.path.join(os.getcwd(), "language.yml")
#         url = "https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml"
#         Logger.info(f"Installing file from {url} to {filename}")
#         try:
#             open(filename,
#                  "wb").write(Requests.get(url, allow_redirects=True).content)
#         except Exception as exception:
#             Logger.info("Process failed")
#             raise exception

#         return filename

def validate_argument_types(values, types, message):
    assert len(values) == len(types), "Values and types should have the same length"
    for index in range(len(values)):
        assert isinstance(values[index], types[index]), str(message)
    return True

def install_files(read_url, write_file_dir, filename, extension):
    assert isinstance(read_url, str), "Read url expected to be a string"
    assert isinstance(write_file_dir, str), "Write path expected to be a string"

    filename = os.path.join(write_file_dir, f"{filename}.{extension}")
    try:
        with open(filename, "wb") as file_writer:
            file_writer.write(requests.get(read_url, allow_redirects=True).content)
    except Exception as exception:
        raise Exception
    
    return filename



class Extensions(object):
    def __init__(self, language_file, display, files):
        self.language_detection_file = language_file
        self.display_output = display
        self.filenames = files

        content = self.remove_unwanted_keys(
            self.__create_language_file(self.language_detection_file)[0]
        )

        print(content)

    def remove_unwanted_keys(self, file_content):
        for language in dict(file_content):
            assert isinstance(file_content[language], dict), "Expected a dict"
            for key in dict(file_content[language]):
                if key != "extensions":
                    del file_content[language][key]
        return file_content

    def __create_language_file(self, language_file):
        if language_file is not None and isinstance(language_file, str):
            if not language_file.endswith(".yml"):
                raise Exception("Language file expected to be a yaml file")
            return Extensions.read_file_data(language_file, True)

        return Extensions.read_file_data(install_files(LANGUAGE_FILE, os.getcwd(), "language", "yml"), True)    

    @staticmethod
    def read_file_data(filename, is_yaml=False):
        with open(filename, "r") as file_reader:
            file_content = file_reader.read()
            line_number_count = len(file_content.split("\n"))

            if not is_yaml:
                return file_content, line_number_count
            
            return yaml.safe_load(file_content), line_number_count

    
            
        

        
