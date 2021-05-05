from polyglot.core.beautify import Beautify, ExtensionMap
import os


# "C:\Users\user\Pictures
b = Beautify(os.path.join("C:", "Users", "user", "Pictures"), ExtensionMap({
    "tetsing_ruby_files" : [".rb"]
}))