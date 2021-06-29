import json
import os
import uuid


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
        self.__store[key] = data
        self.commit()

    @property
    def __expected_parameter_type():
        if self.typeof_data == "any":
            return "any"

        return typeof_data.__name__

    def filter_by_value(self, value):
        values = list(self.__store.values())
        keys = self.keys
        matches = [
            keys[index] if val == value else None for index, val in enumerate(values)
        ]
        return list(filter(lambda element: element is not None, matches))

    def get(self, key=None):
        if key:
            return self.__store[key]
        if len(self.keys) == 0:
            return None
        return self.__store[self.keys[0]]

    def commit(self):
        with open(self.__path, "w") as file_writer:
            file_writer.write(json.dumps(self.__store))

    def __validate_data_type(self, data):
        if self.typeof_data == "any":
            return True
        return isinstance(data, self.typeof_data)
