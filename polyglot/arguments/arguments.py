import sys
import os

from polyglot.arguments.position import Position
from polyglot.exceptions.custom import PolyglotException
class Arguments(object):
    def __init__(self, arguments=None, execute=True, return_value=False):
        self.arguments = sys.argv[1:] if not arguments else arguments
        self.execute = execute
        self.return_value = return_value

        self.position = Position(0)
        
        self.tokens = self.parse()

    def parse(self):
        assert isinstance(self.arguments, list)
        valid_flags = ["--dir", "--o", "--show", "--ignore"]

        parameters = {
            "dir" : os.getcwd(),
            "o" : None,
            "show" : True,
            "ignore" : []
        }

        current_character = self.position.current_character(self.arguments)
        while current_character is not None:
            if not self.is_valid_flag(valid_flags, current_character):
                exception = PolyglotException(
                    f"{current_character} is not recogonised as a valid parmeter",
                    f"Try again with valid parameters",
                    fatal=False
                )
                return None
            character_key = current_character[2:]
            if "=" not in character_key:
                exception = PolyglotException(
                    f"User equal-to(=) to add value to parameters",
                    f"Try again with valid values",
                    fatal=False
                )
                return None
            
            if character_key.count("=") > 1:
                exception = PolyglotException(
                    f"More than one assignments for the same parameter",
                    f"Try again with valid values",
                    fatal=False
                )
                return None

            data = character_key.split("=")
            key, value = data[0], data[1]

            parameters[key] = value

            self.position.increment()
            current_character = self.position.current_character(self.arguments)

        print(parameters)

    def is_valid_flag(self, valid_cases, current_character):
        for valid_case_index in range(len(valid_cases)):
            if current_character.startswith(valid_cases[valid_case_index]):
                return True

        return False