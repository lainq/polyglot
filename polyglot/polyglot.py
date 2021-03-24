from polyglot.exceptions import PolyglotException
from polyglot.extension import PolyglotExtensions

import sys as sys
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
        return PolyglotSearchResult(PolyglotExtensions(self.parameters).find_files(
                self.language_yaml)).create_polyglot_result()

class PolyglotSearchResult(object):
    def __init__(self, polyglot_object):
        self.polyglot_object = self.get_polyglot_object(polyglot_object)

        if not self.polyglot_object:
            sys.exit()

    def get_polyglot_object(self, polyglot_object):
        return (isinstance(polyglot_object, dict))

    def create_polyglot_result(self):
        pass