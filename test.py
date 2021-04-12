from polyglot.core.ignore import Ignore
from polyglot.core import Polyglot

p = Polyglot(".")

ignore_file = Ignore("ignore.polyglot")
ignore_file.create_ignore_files(p.find_directory_files(
    p.directory
))