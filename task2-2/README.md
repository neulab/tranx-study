# Task Description

After running `python main.py`, the program trim the heading and trailing whitespaces and blank lines for all text files under `data`, normalize newlines to `\n` (LF), and convert text files from encoding `ISO-8859-15` to encoding `UTF-8`.
For other file types, do nothing.
Save everything to `output` directory.

# Example Output

```
$ python main.py
$ ls output
aaa.txt  bbb.txt  ccc.txt  ddd.png

$ cd output
$ file aaa.txt
aaa.txt: ASCII text
$ file bbb.txt
bbb.txt: UTF-8 Unicode text
$ file ccc.txt
ccc.txt: UTF-8 Unicode text
```

You can also check out directory `example_output/`.