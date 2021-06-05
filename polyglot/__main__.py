import sys

from clint.textui import colored

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
            parameter_key, value = statement[0], ""
            if len(statement) > 1:
                value = "=".join(map(str, statement[1:]))
            parameters.setdefault(parameter_key, value)
        return self._ArgumentParserResults(command, parameters)

    def create_help_command(self):
        print("Help")

def main():
    arguments = sys.argv[1:]
    argument_parser = ArgumentParser(arguments)
    results = argument_parser.create_argument_parser()
    print(results)

if __name__ == "__main__":
    main()