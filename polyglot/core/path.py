import os
import json
import yaml
from clint.textui import colored


class LanguageException(FileNotFoundError):
    def __init__(self, text):
        self.message = colored.red(text)
        super().__init__(self.message)


class LanguageJSON(object):
    def __init__(self, json_path, rename=None):
        self.path = json_path
        self.rename = self.create_new_name(rename)

    def create_new_name(self, rename):
        if not isinstance(rename, str):
            filename = self.path.split(".")[0]
            return f"{filename}.yml"

        return rename

    def convert_to_yaml(self):
        if not os.path.exists(self.path):
            raise LanguageException(f"Cannot find {self.path}")
        with open(self.path, "r", encoding="utf8") as file_reader:
            data = json.loads(file_reader.read())

        with open(self.path, "w", encoding="utf8") as yaml_writer:
            yaml.dump(data, yaml_writer, allow_unicode=True)

        os.rename(self.path, self.rename)
        return self.rename
