import sys

class Arguments(object):
    def __init__(self, arguments=None, execute=True, return_value=False):
        self.arguments = sys.argv[1:] if not arguments else arguments
        self.execute = execute
        self.return_value = return_value

        self.position = 0

    def current_character(self):pass