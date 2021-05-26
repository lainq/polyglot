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
            if bool(self.text[display_text_type]):
                print("\n")
                table = PrettyTable()
                table.field_names = [
                    "Language",
                    display_text_type.capitalize(),
                    "Total",
                    "Blank",
                ]

                for data in self.text[display_text_type]:
                    current_data = self.text[display_text_type][data]
                    current_row = [
                        data,
                        current_data.get("data"),
                        current_data.get("total"),
                        current_data.get("blank"),
                    ]

                    table.add_rows([current_row])
                print(colored.yellow(table))

    def verify_text(self):
        assert isinstance(self.text["files"], dict), "Files expected to be a dict"
        assert isinstance(self.text["lines"], dict), "lines expected to be a dict"
