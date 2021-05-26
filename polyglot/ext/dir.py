import os
import time
import prettytable


class _Directory(object):
    def __init__(self, path=os.getcwd(), display=True):
        self.path = path
        self.show = display

    def create(self):
        data = self.__create_data()
        table = prettytable.PrettyTable()
        table.field_names = ["Modified at", "label", "size", "path"]
        for key in data:
            table.add_row(
                [
                    data[key].get("modified"),
                    data[key].get("label"),
                    data[key].get("size"),
                    key,
                ]
            )

        if self.show:
            print(table)
        return data

    def __create_data(self):
        data = {}
        files = os.listdir(self.path)
        data["."] = self.__generate_data(self.path)
        data[".."] = self.__generate_data(os.path.dirname(self.path))

        for file_index in range(len(files)):
            filename = files[file_index]
            data.setdefault(
                os.path.basename(filename),
                self.__generate_data(os.path.join(self.path, filename)),
            )

        return data

    def __generate_data(self, path):
        return {
            "modified": time.ctime(os.path.getmtime(path)),
            "label": "<DIR>" if os.path.isdir(path) else "",
            "size": self.__get_file_length(path) if os.path.isfile(path) else "",
        }

    def __get_file_length(self, path):
        try:
            with open(path, "rb") as file_reader:
                return len(file_reader.read())
        except Exception as exception:
            return ""


def directory(path=os.getcwd(), display=True):
    final_directory_path = path
    if final_directory_path == ".":
        final_directory_path = os.getcwd()
    elif final_directory_path == "..":
        final_directory_path = os.path.dirname(os.getcwd())

    return _Directory(final_directory_path, display).create()


def ls(path=os.getcwd(), display=True):
    data = directory(path, display)
    return data
