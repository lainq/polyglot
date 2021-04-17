I've recently been working on a side project called `polyglot`. Polyglot is a python module that finds the percentage of different programming languages used in your project.

{% github pranavbaburaj/polyglot no-readme %}
You can check it out on Github and also drop a star.

## Get Started
In order to get started, you will need to have python and pip installed on your system.

 - Check the versions of `python` and `pip`
```
python -v
pip -v
```
 - Install `python-polyglot` using `pip`

To install `python-polyglot` in your system, use
```
pip install python-polyglot
```

## How to use it
Once Polyglot is all set up and good to go, implementing is easy as pie.
```python
from polyglot.core import Polyglot

# dot(.) represents the current working directory
dirname = "." or "path/to/dir"

poly = Polyglot(".")
poly.show()

```
This prints out something similar
```
+-------------------------+-------+
|         Language        | files |
+-------------------------+-------+
|       Ignore List       |  5.88 |
| GCC Machine Description | 11.76 |
|          Unknown        |  5.88 |
|           Text          |  5.88 |
|          Python         | 64.71 |
|           JSON          |  5.88 |
+-------------------------+-------+


+-------------------------+-------+
|         Language        | lines |
+-------------------------+-------+
|       Ignore List       | 17.22 |
| GCC Machine Description | 22.24 |
|         Unknown         |  2.83 |
|           Text          |  0.26 |
|          Python         | 57.07 |
|           JSON          |  0.39 |
+-------------------------+-------+
```

### `Ignores`
The `ignore` option is used to ignore specific files in the directory tree. For instance, if you don't want the `JSON` files to appear in the table, you can add the `.json` extension to a `polyglot-ignore` file and pass it as a parameter while creating the polyglot instance.

 - `Polyglot Ignores`
    Polyglot ignores are used to ignore 
    specific files in the directory tree. They 
    should have a `.polyglot` file extension.
    Polyglot Ignores as similar to gitignores 
    and are easy to write with almost the same 
    syntax. 
    
 - `Writing a Polyglot ignore.`
    Create a `test.polyglot` file and add the 
    files to ignore
```rb
# for a specific file extension
.json

# for a specific folder
dist/

# for a specific file
dub.sdl
LICENSE

# for specific folders in the directory
~.tox
```  
Once you have an ignore file, use it with polyglot like this
```python
poly = Polyglot(dirname, ignore="test.polyglot")
```

### `Arguments`
```python
from polyglot.arugments import Arguments
```
The Polyglot Arguments is used to parse a list of arguments(`sys.argv[1:]` by default) and perform actions related to Polyglot. 

 - You can either pass in arguments manually 
```python
args = Arguments(arguments=[
"--show=True", "--dir=.", "--o=out.json", "--ignore=test.polyglot"
], return_value=False)
```
or leave it blank to parse the command line arguments passed in along with the file
```python
args = Arguments()
```


 - Start the argument parser
```python
args.parse()
```

The command-line parser has four main options,
`--dir`(default:`current directory`) - The directory path
`--show`(default:`True`) - Whether to display the table or not
`--o`(default:`None`) - Outputs the data as JSON in the file
`--ignore`(default:`None`) - The ignore file

An example usage
```]
python -B <filename>.py --dir=. --show=False
```

<hr>

Please star the project on GitHub if you like it. And thank you for scrolling.
