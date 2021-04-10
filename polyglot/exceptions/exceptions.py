from clint.textui import colored


class PolyglotFileNotFoundError(FileNotFoundError):
    def __init__(self, message):
        self.message = colored.red(message)

        super().__init__(self.message)

    def str(self):
        return self.message
