# from polyglot.exceptions import PolyglotException
# from polyglot.extension import PolyglotExtensions

# import sys as sys, os as os


# def get_dir_name(param):
#     """Get the directory name pased on the parameter"""
#     if param == ".":
#         return os.getcwd()
#     else:
#         if os.path.isabs(param):
#             return param
#         else:
#             return os.path.join(os.getcwd(), param)


# class Polyglot(object):
#     def __init__(self, dirname=None, language_yml=None):
#         self.parameters = os.getcwd() if dirname != None else get_dir_name(
#             dirname)

#         self.language_yaml = language_yml

#     def show(self):
#         """
#         Parse the results and show(return)
#         the reuslts as an array(list)
#         """
#         return PolyglotSearchResult(
#             PolyglotExtensions(self.parameters).find_files(
#                 self.language_yaml)).create_polyglot_result(self.parameters)


# class PolyglotSearchResult(object):
#     def __init__(self, polyglot_object):
#         self.polyglot_object = self.__get_polyglot_object(polyglot_object)

#         if not self.polyglot_object:
#             sys.exit()

#     def __get_polyglot_object(self, polyglot_object):
#         return polyglot_object if (isinstance(polyglot_object,
#                                               dict)) else False

#     def create_polyglot_result(self, file_name):
#         polyglot_result_data = {}
#         self.filename = file_name

#         polyglot_result_data["files"] = self.find_by_percentage(
#             self.polyglot_object)
#         polyglot_result_data["lines"] = self.find_by_lines(
#             self.polyglot_object)

#         return polyglot_result_data

#     def find_by_percentage(self, polyglot):
#         file_percentage = {}
#         for polyglot_file_type in polyglot:
#             file_percentage[polyglot_file_type] = round(
#                 (len(polyglot[polyglot_file_type]) / len(self.file_length())) *
#                 100, 2)
#         return file_percentage

#     def find_by_lines(self, polyglot):
#         lines = {}
#         for file_type in polyglot:
#             for filename in polyglot[file_type]:
#                 with open(filename, "r") as line_counter:
#                     if not file_type in lines: lines[file_type] = 0

#                     lines[file_type] += len(
#                         str(line_counter.read()).split("\n"))
#         for file_type_count in lines:
#             lines[file_type_count] = round(
#                 (lines[file_type_count] / self.lines_length()) * 100, 2)
#         return lines

#     def lines_length(self):
#         files = self.file_length()
#         count = 0

#         for filename in files:
#             with open(filename, "r") as file_reader:
#                 count += len(str(file_reader.read()).split("\n"))
#         return count

#     def file_length(self):
#         return list(filter(self.filter_files, os.listdir(self.filename)))

#     def filter_files(self, data):
#         return "." in data and os.path.isfile(data)

#     def __len__(self):
#         return 0
