from prettytable import PrettyTable
from clint.textui import colored


class Display(object):
    def __init__(self, display_text):
        assert isinstance(display_text, dict), "Expected a dict"
        self.text = display_text

        if not "files" in self.text or not "lines" in self.text:
            raise NameError("Cannot find required keys - lines, files")

        self.display_output()

    def display_output(self):
        """
        Verify the dict elements to be dicts 
        and then continue to print out
        the dict data in tabular form using
        prettytable.
        """
        self.verify_text()

        for display_text_type in self.text:
            print("\n")
            table = PrettyTable()
            table.field_names = ["Language", display_text_type]
            for data in self.text[display_text_type]:
                table.add_rows([[data, self.text[display_text_type][data]]])
            print(colored.yellow(table))

    def verify_text(self):
        assert isinstance(self.text["files"],
                          dict), "Files expected to be a dict"
        assert isinstance(self.text["lines"],
                          dict), "lines expected to be a dict"
