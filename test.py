from polyglot.core.beautify import Beautify, ExtensionMap
import os

b = Beautify(os.getcwd(), ExtensionMap({
    "lol" : []
}))