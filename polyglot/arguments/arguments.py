import sys
import os
import json

from polyglot.arguments.position import Position
from polyglot.exceptions.custom import PolyglotException
from polyglot.core.polyglot import Polyglot


class Arguments(object):
    """
    Pass a set of arguments which is parsed and
    later executed

    Attributes-
        arguments -- The arguments to parse
        return_value -- Whether to return any value
        position -- The lexer postion

    """

    def __init__(self, arguments=None, return_value=False):
        self.arguments = sys.argv[1:] if not arguments else arguments
        self.return_value = return_value

        self.position = Position(0)

    def parse(self):
        """
        Parse the arguments and validate
        them . Also execute the functions
        """
        assert isinstance(self.arguments, list)
        valid_flags = ["--dir", "--o", "--show", "--ignore"]

        parameters = {"dir": os.getcwd(), "o": None, "show": str(True), "ignore": ""}

        current_character = self.position.current_character(self.arguments)
        while current_character is not None:
            if not self.is_valid_flag(valid_flags, current_character):
                exception = PolyglotException(
                    f"{current_character} is not recogonised as a valid parmeter",
                    f"Try again with valid parameters",
                    fatal=False,
                )
                return None
            character_key = current_character[2:]
            if "=" not in character_key:
                exception = PolyglotException(
                    f"User equal-to(=) to add value to parameters",
                    f"Try again with valid values",
                    fatal=False,
                )
                return None

            if character_key.count("=") > 1:
                exception = PolyglotException(
                    f"More than one assignments for the same parameter",
                    f"Try again with valid values",
                    fatal=False,
                )
                return None

            data = character_key.split("=")
            key, value = data[0], data[1]

            parameters[key] = value

            self.position.increment()
            current_character = self.position.current_character(self.arguments)

        return_data = self.validate_parameters(parameters)
        if return_data == None:
            return return_data
        else:
            polyglot = Polyglot(parameters["dir"], ignore=parameters["ignore"])
            data = polyglot.show(display=parameters["show"])

            if parameters["o"]:
                with open(parameters["o"], "w") as writer:
                    writer.write(json.dumps(data))

            if self.return_value:
                return data

    def is_valid_flag(self, valid_cases, current_character):
        for valid_case_index in range(len(valid_cases)):
            if current_character.startswith(valid_cases[valid_case_index]):
                return True

        return False

    def validate_parameters(self, parameters):
        if parameters["show"] not in [str(True), str(False)]:
            exception = PolyglotException(
                "Invalid value for paramter show", "Try again", fatal=False
            )
            return None

        parameters["show"] = bool(parameters["show"])
        parameters["ignore"] = parameters["ignore"].split(",")
        return parameters
