# csv-aggregator

Simple python script to read a bunch of csv files, combine them, and write them out to an excel file.

- [requirements](#requirements)
  - [modules](#modules)
- [usage](#usage)
  - [arguments](#arguments)

# requirements

* python > 3
* pip

## modules

install dependencies by running:

```bash
pip install -r requirements.txt
```

# usage

```bash
./main.py -p ./path/to/your/csv/files -m '*pattern*matching*your*files*.csv' -o 'output_file_name.xlsx'
```

*note: if you get a "permission denied" error, make sure main.py is executable (`chmod +x main.py`)*

## arguments

| description                                     | long arg  | short arg | default  | required |
| ----------------------------------------------- | --------- | --------- | -------- | -------- |
| The path your csv files are in                  | path      | p         | `.`      | false    |
| Glob pattern to match your files                | match     | m         | `*.csv`  | false    |
| What to save your output as - path and filename | output    | o         |          | true     |
| The name of the excel sheet                     | name      | n         | `Sheet1` | false    |
| The delimiter for your csv files                | separator | s         | `,`      | false    |
