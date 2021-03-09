from .exceptions import *
import os as os
import logging as Logger

class PolyglotExtensions(object):
    def __init__(self, param):
        assert isinstance(param, str), "Expected a string"

        self.parameter = param

        self.directory_name = self.__get_dir_name(self.parameter)
        

    def __get_dir_name(self, param):
        """Get the directory name pased on the parameter"""
        if param == ".":
            return os.getcwd()
        else:
            if os.path.isabs(param):
                return param
            else:
                return os.path.join(os.getcwd(), param)

    def find_files(self):
        langauge_file = os.path.exists("../language.yaml")
        if not langauge_file:
            Logger.error("Cannot find the language file")
            self.__install_language_file()

    def __install_language_file(self):
        pass


class Polyglot(object):
    def __init__(self, command="init", command_argument="."):
        assert isinstance(command, str), "Expected a string"
        assert isinstance(command_argument, str), "Expected a strng"

        self.command = command
        self.parameters = command_argument

        self.files = {}

    def show(self):
        """
        Parse the results and show(return)
        the reuslts as an array(list)
        """
        if self.command == "init":
            poly = PolyglotExtensions(self.parameters).find_files()
