# CLI
The polyglot module comes along with a command line application. The cli can be accessed using `polyglot` or `pgt`

## `Stats`
```ps1
polyglot stats
```
#### Parameters
- `--dir`:The directory to check the stats
    - Default : Current directory
- `--ignore`: Files to ignore
    - Defult: By default the cli searches for files with a `.polyglot`extension
- `--detect`: The language detection file
- `--fmt`: `l` for comparison based on loc, `f` for files.
- `--output`: Store the stats output into a file. Only json files and toml files are allowed.

```ps1
polyglot stats --dir=/home/Documents --ignore --fmt=l --output=output.toml
```

## `Tree`
```ps1
polyglot tree
```

#### Parameters
- `--dir`: The directory. Set to the current directory by default.

## `dir` or `ls`
```ps1
polyglot ls
polyglot dir
```

## `up`
Update your cli
```
polyglot up
```


