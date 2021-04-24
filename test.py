from polyglot.core.ignore import Ignore
from polyglot.core import Polyglot


print("Hello")
p = Polyglot(".")

# ignore_file = Ignore("ignore.polyglot")
# ignore_file.create_ignore_files(p.find_directory_files(
#     p.directory
# ))
print("Hello2")

p.show(language_detection_file="E:\polyglot-1\language.yml",output="l.toml")

