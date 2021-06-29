import os


class _FilterResults(object):
    def __init__(self, result, count=None):
        self.result = result
        self.count = count

    def __repr__(self):
        return f"Result:{self.result}"


def __filter_extension_handler(file, extension):
    file_extension = f".{file.split('.')[-1:][0]}"
    return file.endswith(extension)


def filter_by_extension(extension, directory=os.getcwd(), count=True):
    files = list(
        filter(
            lambda file: __filter_extension_handler(file, extension),
            os.listdir(directory),
        )
    )
    results = _FilterResults(files)
    if count:
        results.count = len(files)
    return results
