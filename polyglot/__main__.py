import sys
import os

from clint.textui import colored

COMMANDS = [
    "stats"
]

class EventLogger(object):
    pass

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
                    f"Parameters should start with double hiphens "
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
        
        if self.ignore == -2:
           self.ignore = self.__find_ignore_file()
        else:
            self.ignore = None
        
        print(self.ignore)

    def __find_ignore_file(self):
        if not os.path.isdir(self.directory):
            _ = CommandLineException(f"{self.directory} is not a directory")
            return None
        files = list(filter(lambda current_element:current_element.endswith(".polyglot"), os.listdir(self.directory)))
        print(files)

def command_executor(results):
    command, params = results.command, results.parameters
    if command == "stats":
        _ = LanguageStats(params)

def main():
    arguments = sys.argv[1:]
    argument_parser = ArgumentParser(arguments)
    results = argument_parser.create_argument_parser()
    if results.command not in COMMANDS:
        error = CommandLineException(f"Invalid command : {results.command}")
    command_executor(results)

if __name__ == "__main__":
    main()