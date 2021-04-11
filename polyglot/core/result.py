import os


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
            self.data["files"][file_type] = round(
                (len(data[file_type]) / length) * 100, 2)

    def __find_by_lines(self, data):
        lines = {}
        for file_type in data:
            file_line_count = 0
            for filename in data[file_type]:
                with open(filename, "r", errors="ignore") as line_counter:
                    file_line_count += len(line_counter.read().split("\n"))
            lines[file_type] = file_line_count
        total_lines = sum([lines[key] for key in lines])
        for line_key in data:
            self.data["lines"][line_key] = round(
                (lines[line_key] / total_lines) * 100, 2)
