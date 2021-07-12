import sys
import os
import json
import pathlib
import pip

from clint.textui import colored

from polyglot.core.polyglot import Polyglot
from polyglot.core.project import Project, ProjectFiles
from polyglot.core.tree import Tree
from polyglot.ext.dir import ls

COMMANDS = ["stats", "project", "tree", "dir", "ls", "help", "up"]
DESCRIPTIONS = [
    "--dir=<dir> --ignore=<ignore> --detect=<file> --fmt=<fmt> --output=<filename>",
    "--manifest=<filename>",
    "--dir=<dir>",
    "--dir=<dir>",
    "--dir=<dir>",
    "",
    "",
]


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
        """Create an exception and exit the program if
        the exception is fatal
        """
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
        """
        Parse the arguments into different commands
        and parameters. The first element in the
        argv list is considered to be the command.

        All the following elements should start with --
        and are considered as parameters
        """
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


class HelpMessage(object):
    def __init__(self, commands, descriptions):
        assert isinstance(commands, list)
        self.commands = commands
        self.descriptions = descriptions

        self.create_help_string()

    def create_help_string(self):
        statements = ["usage: polyglot <command> <param>=<value>", ""]

        for index, command in enumerate(self.commands):
            statements.append(
                f"{command}{self.spaces(command, COMMANDS)} -> {self.descriptions[index]}"
            )
        print("\n".join(statements))

    def spaces(self, command, commands):
        largest = max(
            [len(commands[current_index]) for current_index in range(len(commands))]
        )
        return "".join([" " for index in range(largest - len(command))])


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


class ListDirectories(object):
    def __init__(self, directory, only_dirs):
        self.directory = directory
        self.dirs = only_dirs

        self.list_directory_content()

    def list_directory_content(self):
        for filename in self.content:
            current_path = os.path.join(self.directory, filename)
            size = f"[size:{os.stat(current_path).st_size} bytes]"
            color = colored.green if os.path.isfile(current_path) else colored.blue
            print(f"{color(filename)} -> {colored.yellow(size)}")

    @property
    def content(self):
        return list(filter(self.file_filter_function, os.listdir(self.directory)))

    def file_filter_function(self, filename):
        if self.dirs:
            return os.path.isdir(filename)
        return True


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
    command_directory = params.get("--dir") or os.getcwd()
    if command_directory == -2:
        command_directory = os.getcwd()
    if not os.path.isdir(command_directory):
        EventLogger.error(f"{command_directory} is not a directory")
        return None
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
    elif command == "tree":
        directory = params.get("--dir") or os.getcwd()
        if directory == -2:
            directory = os.getcwd()
        if not os.path.isdir(directory):
            EventLogger.error(f"{directory} is not a directory")
            return None

        try:
            tree = Tree(directory)
            tree.generate()
        except Exception as tree_exception:
            EventLogger.error(tree_exception.__str__())
            sys.exit(1)
    elif command == "dir":
        ls(command_directory)
    elif command == "ls":
        dirs = ListDirectories(command_directory, params.get("--only-dirs"))
    elif command == "help":
        help = HelpMessage(COMMANDS, DESCRIPTIONS)
    elif command == "up":
        pip.main(["install", "python-polyglot", "--upgrade"])


class Properties(object):
    def __init__(self, path):
        assert os.path.exists(path), f"{path} does not exist"
        self.path = self.find_file_path(path)
        self.properties_command()

    def find_file_path(self, path):
        if path == ".":
            return os.getcwd()
        elif path == "..":
            return os.path.dirname(path)

        return path

    def properties_command(self):
        print(
            colored.green(os.path.basename(self.path), bold=True),
            colored.yellow(f"[{self.file_type}]"),
        )
        self.draw_seperator()

        properties = self.properties
        for property in properties:
            print(
                colored.cyan(f"{property} -> "),
                colored.yellow(properties.get(property)),
            )

    def draw_seperator(self):
        length = len(self.basename) + (len(self.file_type) + 3)
        for index in range(length):
            print(colored.yellow("-"), end=("\n" if index + 1 == length else ""))

    @property
    def properties(self):
        return {
            "type": self.file_type,
            "extension": self.file_extension,
            "parent": self.find_file_path(pathlib.Path(self.path).parent.__str__()),
            "size": os.stat(self.path).st_size,
        }

    @property
    def file_extension(self):
        if os.path.isdir(self.path):
            return ""
        split_path = self.basename.split(".")
        if len(split_path[0]) == 0 or split_path[0] == self.basename:
            return ""
        return split_path[-1]

    @property
    def basename(self):
        return os.path.basename(self.path)

    @property
    def file_type(self):
        return "DIR" if os.path.isdir(self.path) else "FILE"


def main():
    arguments = sys.argv[1:]
    if len(arguments) == 0:
        return 1
    argument_parser = ArgumentParser(arguments)
    results = argument_parser.create_argument_parser()
    if not results.command:
        return 1

    if results.command.strip().__len__() == 0:
        return 1

    if results.command not in COMMANDS:
        try:
            Properties(results.command)
        except AssertionError as exception:
            EventLogger.error(exception.__str__())
            sys.exit()
    command_executor(results)


if __name__ == "__main__":
    exit_status = main()
    if exit_status == 1:
        HelpMessage(COMMANDS, DESCRIPTIONS)
