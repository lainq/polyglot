import os

class ProjectFiles(object):
    def __init__(self, files, folders):
        assert isinstance(files, dict), "Files expected to be a dict"
        self.files = files
        self.folders = folders


class Project(object):
    def __init__(self, project_name, project_files):
        assert isinstance(
            project_files,
            ProjectFiles), "Parameter expected to be of type ProjectFiles"
        self.name = project_name
        self.files = project_files

    def create(self, clean=False):
        directory = self.__directory_path(self.name)
        if os.path.exists(directory) and os.path.isdir(directory):
            directory_length = len(os.listdir(directory))
            if directory_length > 0:
                if not clean:
                    raise FileExistsError(f"{directory} already exists")
                    return None

                os.rmdir(directory)
                os.mkdir(directory)
        else:
            os.mkdir(directory)

        self.__create_project_files(directory)

    def __create_project_files(self, directory):
        for filename in self.files.files:
            self.write_file_data(os.path.join(directory, filename),
                                 self.files.files.get(filename))

        for folder in self.files.folders:
            if not os.path.isdir(folder):
                os.mkdir(os.path.join(directory, folder))

    def write_file_data(self, filename, data=""):
        with open(filename, "w") as file_writer:
            file_writer.write(data)

    def __directory_path(self, project_name):
        assert isinstance(project_name,
                          str), "Porject name expected to be a string"
        if project_name == ".":
            return os.getcwd()

        return os.path.join(os.getcwd(), project_name)
