import json
import os
import uuid

class UseAscii(object):
    @staticmethod
    def string_to_ascii_string(string, separator="."):
        assert "__str__" in dir(string)
        string_form, return_value = str(string), ""
        for current_character in string_form:
            return_value += str(UseAscii.get_ascii_value(current_character)) + separator
        return return_value

    @staticmethod
    def get_ascii_value(character):
        try:
            return ord(character)
        except Exception as exception:
            return -1

    @staticmethod
    def ascii_string_to_string(ascii_string, separator="."):
        return_value = ""
        for character in list(filter(lambda element: element.strip(),ascii_string.split(separator))):
            if len(character) == 0:continue
            value = int(character)
            if value == -1:continue
            return_value += chr(value)
        return return_value

class JsonStore(object):
    def __init__(self, filename, database_name, typeof_data="any"):
        self.file = filename
        self.name = database_name.strip()
        self.__path = os.path.join(os.path.dirname(self.file), f"{self.name}.json")
 
        assert len(self.name) > 0, "Name should have atleast one character"
        if not (type(typeof_data).__name__ == "type" or typeof_data == "any"):
            raise TypeError(f"Invalid type : {type(typeof_data).__name__}")

        self.typeof_data = typeof_data
        self.__store = self.initialize_database()

        self.__store = self.__store if isinstance(self.__store, dict) else {}

        self.commit()

    @property
    def keys(self):
        return list(self.__store.keys())

    def __create_short_uuid(self, check_for_duplicate=[], length=5):
        short_uuid = lambda: str(uuid.uuid4())[:length]
        value = short_uuid()
        while value in check_for_duplicate:
            value = short_uuid()
        return value

    def initialize_database(self):
        if not os.path.isfile(self.__path):
            with open(self.__path, "w") as file_writer:
                file_writer.write(json.dumps({}))
                return {}
        return self.__get_store_content()

    def __get_store_content(self):
        with open(self.__path, "r") as file_reader:
            try:
                return json.loads(file_reader.read())
            except Exception as exception:
                with open(self.__path, "w") as file_writer:
                    file_writer.write(json.dumps({}))
                return {}

    def add(self, data):
        if not self.__validate_data_type(data):
            raise TypeError(f"Parameter")
        key = self.__create_short_uuid(check_for_duplicate=self.keys)
        self.__store[key] = (
            UseAscii.string_to_ascii_string(data) if isinstance(data, str) else data
        )
        self.commit()

    @property
    def __expected_parameter_type(self):
        if self.typeof_data == "any":
            return "any"

        return self.typeof_data.__name__

    def filter_by_value(self, value):
        values = list(self.__store.values())
        keys = self.keys
        matches = [
            keys[index] if val == value else None for index, val in enumerate(values)
        ]
        return list(filter(lambda element: element is not None, matches))

    def get(self, key=None):
        if len(self.keys) == 0 and key == None:
            return None
        return_value = self.__store[key or self.keys[0]]
        if not isinstance(return_value, str):
            return return_value
        return UseAscii.ascii_string_to_string(return_value)

    def commit(self):
        with open(self.__path, "w") as file_writer:
            file_writer.write(json.dumps(self.__store))

    def __validate_data_type(self, data):
        if self.typeof_data == "any":
            return True
        return isinstance(data, self.typeof_data)
