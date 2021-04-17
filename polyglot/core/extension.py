import os
import requests
import yaml

from polyglot.core.path import LanguageJSON

LANGUAGE_FILE = "https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml"


def validate_argument_types(values, types, message):
    assert len(values) == len(
        types), "Values and types should have the same length"
    for index in range(len(values)):
        assert isinstance(values[index], types[index]), str(message)
    return True


def install_files(read_url, write_file_dir, filename, extension):
    assert isinstance(read_url, str), "Read url expected to be a string"
    assert isinstance(write_file_dir,
                      str), "Write path expected to be a string"

    filename = os.path.join(write_file_dir, f"{filename}.{extension}")
    try:
        with open(filename, "wb") as file_writer:
            file_writer.write(
                requests.get(read_url, allow_redirects=True).content)
    except Exception as exception:
        raise Exception

    return filename


class Extensions(object):
    def __init__(self, language_file, display, files):

        self.language_detection_file = language_file
        self.display_output = display
        self.filenames = files

        self.languages = {}

        self.content = self.remove_unwanted_keys(
            self.__create_language_file(self.language_detection_file)[0])

    def get_extension_data(self):
        return self.__split_files(self.filenames, self.content)

    def __split_files(self, files, content):
        """
        Loop through each file in the files array
        and determine the language with the help of
        the language extension 
        """
        for filename in files:
            language = self.__find_language_name(filename, content)
            if language not in self.languages:
                self.languages[language] = []

            self.languages[language].append(filename)
        return self.languages

    def __find_language_name(self, filename, content):
        extension = f".{filename.split('.')[-1]}"
        for language_key in content:
            if "extensions" not in content[language_key]:
                continue

            if extension in content[language_key]["extensions"]:
                return language_key

        return "Unknown file"

    def remove_unwanted_keys(self, file_content):
        """
        Remove all the unwanted keys from the 
        file_content dictionary and only keep
        the 'extensions' key
        """
        for language in dict(file_content):
            assert isinstance(file_content[language], dict), "Expected a dict"
            for key in dict(file_content[language]):
                if key != "extensions":
                    del file_content[language][key]
        return file_content

    def __create_language_file(self, language_file):
        """
        If language file is mentioned, and the file is a string
        return the filecontent and the number of lines

        Else, install the language file from the internet
        and return the file_content along with the number of lines
        """
        if language_file is not None and isinstance(language_file, str):
            if not language_file.endswith(
                    ".yml") and not language_file.endswith(
                        ".json") and not language_file.endswith(".yaml"):
                raise Exception(
                    "Language file expected to be a yaml or json file")

            if language_file.endswith(".json"):
                filename = LanguageJSON(language_file).convert_to_yaml()
                return Extensions.read_file_data(filename, True)
            else:
                return Extensions.read_file_data(language_file, True)

        return Extensions.read_file_data(
            install_files(LANGUAGE_FILE, os.getcwd(), "language", "yml"), True)

    @staticmethod
    def read_file_data(filename, is_yaml=False):
        """
        Read the specified filename and if the file
        is a yaml file,parse the yaml string
        using the yaml library
        """
        with open(filename, "r") as file_reader:
            file_content = file_reader.read()
            line_number_count = len(file_content.split("\n"))

            if not is_yaml:
                return file_content, line_number_count

            return yaml.safe_load(file_content), line_number_count
