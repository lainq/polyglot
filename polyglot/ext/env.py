import os

from clint.textui import colored

class EnvAssignmentError(Exception):
    def __init__(self, error, line_number):
        self.message = error.strip()
        self.line = line_number

        error_message = colored.red(f"{self.message} [LINE:{self.line}]")
        super().__init__(error_message)

class Tokens(object):
    COMMENT_TOKEN = "#"

class EnvironmentVariable(object):
    def __init__(self, variable, value, token_type, line_number):
        self.variable = variable
        self.value = value
        self.token_type = token_type

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

        print(self.source)

        assignment_counts = self.source.count("=")
        if assignment_counts > 1:
            raise EnvAssignmentError("Multiple assignments in the same line", self.line_number)

        

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
        for line_number in range(len(data)):
            parser = EnvParser(data[line_number], line_number)
            parser.create_parser_tokens()

    def __read(self, filename):
        if not os.path.exists(filename) and os.path.isfile(filename):
            raise FileNotFoundError(f"{filename} does not exist")

        with open(filename, mode="r") as env_file_reader:
            return env_file_reader.read()
