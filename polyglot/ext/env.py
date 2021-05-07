import os


class Env(object):
    defualt_filename = os.path.join(os.getcwd(), ".env")

    def __init__(self, env=None, load=True):
        assert isinstance(env, str) or env == None, "Unexpected type of parameter env"
        self.env = env or self.defualt_filename
        self.load_to_process = load

    def load(self):
        data = self.__read(self.env)
        print(data)

    def __read(self, filename):
        if not os.path.exists(filename) and os.path.isfile(filename):
            raise FileNotFoundError(f"{filename} does not exist")

        with open(filename, mode="r") as env_file_reader:
            return env_file_reader.read()
