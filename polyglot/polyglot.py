from polyglot.exceptions import PolyglotException
from polyglot.extension import PolyglotExtensions


class Polyglot(object):
    def __init__(self,
                 command="init",
                 command_argument=".",
                 language_yml=None):
        assert isinstance(command, str), "Expected a string"
        assert isinstance(command_argument, str), "Expected a string"

        self.command = command
        self.parameters = command_argument

        self.language_yaml = language_yml

        self.files = {}

    def show(self):
        """
        Parse the results and show(return)
        the reuslts as an array(list)
        """
        if self.command == "init":
            return PolyglotExtensions(self.parameters).find_files(
                self.language_yaml)
        else:
            raise NameError(f"Command {self.command} not found")