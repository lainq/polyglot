import os

class Pfg(object):
    default_filename = "config.pfg"

    def __init__(self, filename=None, data={}):
        self.filename = filename or self.default_filename
        self.data = data

    def create(self):
        if os.path.exists(self.filename) and os.path.isfile(self.filename):
            raise FileExistsError(f"{self.filename} already exists")
            