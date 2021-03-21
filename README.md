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

poly = Polyglot("init", dirname)

printer.pprint(poly.show())
```

[Development paused]()
