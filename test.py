from polyglot.core.beautify import Beautify, ExtensionMap
import os


# "C:\Users\user\Pictures
b = Beautify(os.path.join("C:", "Users", "user", "Pictures"), ExtensionMap({
    ".rb" : ["tetsing_ruby_files"]
}))