from polyglot.ext.env import Env
import os
data = Env().load()

print(os.environ.get('hehe'))