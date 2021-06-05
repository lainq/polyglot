import sys
import os
import json

from clint.textui import colored

from polyglot.core.polyglot import Polyglot
from polyglot.core.project import Project, ProjectFiles

COMMANDS = ["stats", "project"]


class EventLogger(object):
    @staticmethod
    def info(message):
        print(colored.cyan(f"INFO:{message}"))

    @staticmethod
    def warning(message):
        print(colored.yellow(f"WARNING:{message}"))

    @staticmethod
    def error(message):
        print(colored.red(f"ERROR:{message}"))


class CommandLineException(object):
    def __init__(self, message, suggestion=None, fatal=True):
        self.message = message
        self.suggestion = suggestion
        self.is_fatal = fatal

        self.create_exception()

    def create_exception(self):
        print(colored.red(f"ERROR:{self.message}"))
        if self.suggestion:
            print(colored.yellow(self.suggestion.strip()))
        if self.is_fatal:
            sys.exit(1)


class ArgumentParser(object):
    class _ArgumentParserResults(object):
        def __init__(self, command, parameters):
            self.command = command
            self.parameters = parameters

    def __init__(self, arguments):
        self.arguments = arguments

    def create_argument_parser(self):
        command, parameters = None, {}
        for index, current in enumerate(self.arguments):
            if index == 0:
                command = current
                continue

            if not current.startswith("--"):
                exception = CommandLineException(
                    f"Invalid parameter {current}",
                    f"Parameters should start with double hiphens ",
                )

            statement = current.split("=")
            parameter_key, value = statement[0], -2
            if len(statement) > 1:
                value = "=".join(map(str, statement[1:]))
            parameters.setdefault(parameter_key, value)
        return self._ArgumentParserResults(command, parameters)

    def create_help_command(self):
        print("Help")


class LanguageStats(object):
    def __init__(self, parameters):
        self.directory = parameters.get("--dir") or os.getcwd()
        self.ignore = parameters.get("--ignore") or -1
        self.language_file = (
            None
            if (parameters.get("--detect") or None) == -2
            else parameters.get("--detect")
        )
        self.fmt = parameters.get("--fmt")
        self.output = parameters.get("--output") or None

        if self.fmt not in ["l", "f", "L", "F"]:
            self.fmt = None
        else:
            self.fmt = self.fmt.lower()

        if self.ignore == -2:
            self.ignore = self.__find_ignore_file()
        else:
            self.ignore = None

        try:
            polyglot = Polyglot(self.directory, self.ignore)
            polyglot.show(self.language_file, True, self.fmt, self.output)
        except Exception as exception:
            EventLogger.error(exception.__str__())
            sys.exit(1)

    def __find_ignore_file(self):
        if not os.path.isdir(self.directory):
            _ = CommandLineException(f"{self.directory} is not a directory")
            return None
        files = list(
            filter(
                lambda current_element: current_element.endswith(".polyglot"),
                os.listdir(self.directory),
            )
        )
        if len(files) == 0:
            EventLogger.error(f"Could not find an ignore file in {self.directory}")
            return None

        if len(files) > 1:
            EventLogger.warning(f"Found {len(files)} ignore files")

        ignore_filename = files[0]
        EventLogger.info(f"{ignore_filename} is taken as the ignore file")
        return ignore_filename


def search_for_manifest(manifest_filename):
    filename = os.path.join(os.getcwd(), manifest_filename)
    if not os.path.isfile(filename):
        _ = CommandLineException(f"{manifest_filename} does not exist")
    try:
        with open(filename, "r") as file_reader:
            return json.load(file_reader)
    except Exception as exception:
        CommandLineException(exception.__str__())


def command_executor(results):
    command, params = results.command, results.parameters
    if command == "stats":
        _ = LanguageStats(params)
    elif command == "project":
        manifest_file = params.get("--manifest") or "manifest.json"
        if manifest_file == -2:
            manifest_file = "manifest.json"
        manifest_data = search_for_manifest(manifest_file)

        name, files, folders = (
            manifest_data.get("name") or ".",
            manifest_data.get("files") or {},
            manifest_data.get("directories") or manifest_data.get("folders") or [],
        )
        try:
            project = Project(name, ProjectFiles(files, folders))
            project.create()
        except Exception as ProjectException:
            EventLogger.error(ProjectException.__str__())
            sys.exit(1)


def main():
    arguments = sys.argv[1:]
    argument_parser = ArgumentParser(arguments)
    results = argument_parser.create_argument_parser()
    if results.command not in COMMANDS:
        error = CommandLineException(f"Invalid command : {results.command}")
    command_executor(results)


if __name__ == "__main__":
    main()
