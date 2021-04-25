from polyglot.core.project import Project,ProjectFiles

d = Project("hello", ProjectFiles(
    {"lol.py" :"dd","ap.js" : "0"},
    ["lmao"]
), polyglot=True).create()