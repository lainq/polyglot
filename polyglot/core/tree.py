import os
import pathlib
import itertools
import clint

class UnknownPathError(FileNotFoundError):
    def __init__(self, error_message):
        self.message = clint.textui.colored.red(error_message)

        super.__init__(self.message)

class Tree(object):
    space = '    '
    branch = '│   '
    tree = '├── '
    last = '└── '

    def __init__(self, directory):
        self.directory = directory if self.__verify_directory_path(os.getcwd() if directory == "." else directory) else None

    def __verify_directory_path(self, directory):
        if not os.path.exists(directory) or not os.path.isdir(directory):
            return False

        return True

    def __add_path(directory, prefix, level=-1, limit=False):
        if not level:
            return None

        if limit:
            contents = [d for d in directory.iterdir() if d.is_dir()]
        else: 
            contents = list(directory.iterdir())
        pointers = [self.tree] * (len(contents) - 1) + [self.last]
        for pointer, path in zip(pointers, contents):
            if path.is_dir():
                yield prefix + pointer + path.name
                extension = self.branch if pointer == self.tree else self.space 
                yield from self.__add_path(directory, prefix=prefix+extension, level=level-1)
            elif not limit_to_directories:
                yield prefix + pointer + path.name

    def generate(self, level=-1, limit_to_directories=False, length_limit=None):
        if not self.directory:
            raise UnknownPathError(f"Cannot find {self.directory}")

        path = pathlib.Path(self.directory)
        iterator = self.__add_path(path, level=level)
        for line in itertools.islice(iterator, length_limit):
            print(clint.textui.colored.yellow(line))
        if next(iterator, None):
            print(clint.textui.colored.red(
                f'... length_limit, {length_limit}, reached, counted:'
            ))
t = Tree(".").generate()
        
