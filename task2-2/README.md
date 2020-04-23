# Task Description

After running `python main.py`, the program trim the heading and trailing whitespaces and blank lines for all text files under `data`, normalize newlines to `\n`, and convert the encoding to `ascii`.
For other file types, do nothing.
Save everything to `output` directory.

# Example Output

```
$ python main.py
$ ls output
aaa.txt  bbb.txt  ccc.txt  ddd.png
(aaa.txt, bbb.txt, ccc.txt have been modified)
```