# Polyglot

Find the percentage of programming languages used in your project

## Installation

Clone the repository

```
git clone https://github.com/pranavbaburaj/polyglot.git
```

Install the requirements

```
pip install -r requirements.txt
```

Build the setup script

```
python setup.py sdist

pip install .
```

## How to use it

```python
from polyglot import Polyglot
import os as os
import pprint as pprint

printer = pprint.PrettyPrinter()

# alternatively, you can use a dot(.) that denotes
# the current directory
# you can also simply use a filename like 'hello' that returns you (cwd/hello)

dirname = os.getcwd()

poly = Polyglot("init", ignore=["language.yml"])

poly.show(display=True)
```

Result :

```
+-------------------------+-------+
|         Language        | files |
+-------------------------+-------+
|       Ignore List       |  5.88 |
| GCC Machine Description | 11.76 |
|       Unknown file      |  5.88 |
|           Text          |  5.88 |
|          Python         | 64.71 |
|           JSON          |  5.88 |
+-------------------------+-------+


+-------------------------+-------+
|         Language        | lines |
+-------------------------+-------+
|       Ignore List       | 17.22 |
| GCC Machine Description | 22.24 |
|       Unknown file      |  2.83 |
|           Text          |  0.26 |
|          Python         | 57.07 |
|           JSON          |  0.39 |
+-------------------------+-------+
```

[Development paused]()
