from polyglot.core import Polyglot
import os

polyglot = Polyglot(".", ignore=["language.yml"]).show(display=True)

print(polyglot)