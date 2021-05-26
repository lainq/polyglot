import os

from clint.textui import colored


def find_token_type(value):
    if value.isdigit():
        return (int, float)

    return str


class EnvAssignmentError(Exception):
    def __init__(self, error, line_number):
        self.message = error.strip()
        self.line = line_number

        error_message = colored.red(f"{self.message} at line {self.line}")
        super().__init__(error_message)


class InvalidVariableName(EnvAssignmentError):
    def __init__(self, message, line):
        super().__init__(message, line)


class Tokens(object):
    COMMENT_TOKEN = "#"


class EnvironmentVariable(object):
    def __init__(self, variable, value, token_type, line_number):
        self.line = line_number

        self.variable = self.__check_variable_name(variable)
        self.value = value
        self.token_type = token_type

    def __check_variable_name(self, name):
        if len(name) == 0:
            raise InvalidVariableName(f"Invalid variable name {name}", self.line)
        first = name[0]
        if first.isdigit():
            raise InvalidVariableName(
                f"Variable name {name} starts with a number", self.line
            )

        return name


class EnvParserPosition(object):
    def __init__(self, position=0):
        self.position = position

    def increment(self, increment_by=1):
        self.position += increment_by

    def decrement(self, decrement_by=1):
        self.position += -decrement_by

    def current_character(self, data):
        if len(data) == self.position:
            return None

        return data[self.position]


class EnvParser(object):
    tokens = []

    def __init__(self, source, line):
        self.source = source.strip()
        self.line_number = line + 1
        self.position = EnvParserPosition(0)
        self.character = self.position.current_character(self.source)

    def create_parser_tokens(self):
        if len(self.source) == 0 or self.source.startswith(Tokens.COMMENT_TOKEN):
            return []

        assignment_counts = self.source.count("=")
        if assignment_counts > 1 or assignment_counts == 0:
            raise EnvAssignmentError("Multiple or no assignments ", self.line_number)

        name, value = self.source.split("=")
        token_type = find_token_type(value)
        existing_variables = list(
            filter(lambda list_element: list_element.variable == name, self.tokens)
        )
        if not len(existing_variables) == 0:
            raise InvalidVariableName(
                f"Duplicate variable name {name}", self.line_number
            )
        token = EnvironmentVariable(name, value, token_type, self.line_number)
        self.tokens.append(token)

        return self.tokens

    def update(self):
        self.position.increment(1)
        self.character = self.position.current_character(self.source)


class Env(object):
    defualt_filename = os.path.join(os.getcwd(), ".env")

    def __init__(self, env=None, load=True):
        assert isinstance(env, str) or env == None, "Unexpected type of parameter env"
        self.env = env or self.defualt_filename
        self.load_to_process = load

    def load(self):
        data = self.__read(self.env).split("\n")
        tokens = []
        for line_number in range(len(data)):
            parser = EnvParser(data[line_number], line_number)
            token_data = parser.create_parser_tokens()
            for token_element in token_data:
                tokens.append(token_element)

        for token_element in tokens:
            os.environ.setdefault(token_element.variable, token_element.value)

    def __read(self, filename):
        if not os.path.exists(filename) and os.path.isfile(filename):
            raise FileNotFoundError(f"{filename} does not exist")

        with open(filename, mode="r") as env_file_reader:
            return env_file_reader.read()
