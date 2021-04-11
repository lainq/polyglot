from polyglot.core import Polyglot

d = Polyglot("wsws")
print(d.show(display=False))


# ```
# +-------------------------+-------+
# |         Language        | files |
# +-------------------------+-------+
# |       Ignore List       |  5.88 |
# | GCC Machine Description | 11.76 |
# |       Unknown file      |  5.88 |
# |           Text          |  5.88 |
# |          Python         | 64.71 |
# |           JSON          |  5.88 |
# +-------------------------+-------+


# +-------------------------+-------+
# |         Language        | lines |
# +-------------------------+-------+
# |       Ignore List       | 17.22 |
# | GCC Machine Description | 22.24 |
# |       Unknown file      |  2.83 |
# |           Text          |  0.26 |
# |          Python         | 57.07 |
# |           JSON          |  0.39 |
# +-------------------------+-------+
# ```