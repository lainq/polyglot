import os

from polyglot.core.ignore import Ignore


class Result(object):
    def __init__(self, file_information):
        assert isinstance(file_information, dict), "Expected a dict"

        self.file_information = file_information
        self.data = {"files": {}, "lines": {}}

    def show_file_information(self):
        files = self.__find_by_files(self.file_information)
        lines = self.__find_by_lines(self.file_information)

        return self.data

    def __find_by_files(self, data):
        length = sum([len(data[key]) for key in data])
        for file_type in data:
            self.data["files"][file_type] = {
                "data": f"{round((len(data[file_type]) / length) * 100, 2)} %",
                "total": len(data[file_type]),
                "blank": len(
                    Ignore.remove_specific_list_element(
                        [
                            os.path.getsize(filename) == 0
                            for filename in data[file_type]
                        ],
                        [False],
                    )
                ),
            }

    def __find_by_lines(self, data):
        lines = {}
        empty = {}
        for file_type in data:
            file_line_count = 0
            empty_line_count = 0
            for filename in data[file_type]:
                if not os.path.exists(filename):
                    continue

                with open(filename, "r", errors="ignore") as line_counter:
                    file_data = line_counter.read().split("\n")

                    file_line_count += len(file_data)
                    for line in file_data:
                        if len(line.strip()) == 0:
                            empty_line_count += 1

            lines[file_type] = file_line_count
            empty[file_type] = empty_line_count
        total_lines = sum([lines[key] for key in lines])
        for line_key in data:
            self.data["lines"][line_key] = {
                "data": f"{round((lines[line_key] / total_lines) * 100, 2)} %",
                "total": lines.get(line_key),
                "blank": empty.get(line_key),
            }
