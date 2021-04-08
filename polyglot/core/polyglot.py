import os

class Polyglot(object):
    def __init__(self, directory_name):
        self.directory = Polyglot.find_directory_path()

    