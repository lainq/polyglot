from polyglot.exceptions import PolyglotException
from polyglot.extension import PolyglotExtensions

class Polyglot(object):
    def __init__(self,
                 command_argument=".",
                 language_yml=None):
        assert isinstance(command_argument, str), "Expected a string"
        self.parameters = command_argument

        self.language_yaml = language_yml

    def show(self):
        """
        Parse the results and show(return)
        the reuslts as an array(list)
        """
        return PolyglotExtensions(self.parameters).find_files(
                self.language_yaml)
    