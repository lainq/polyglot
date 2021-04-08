from polyglot.core import Polyglot
import os

polyglot = Polyglot(os.path.join(os.getcwd(), "lolo"), ignore=["language.yml"]).show()

