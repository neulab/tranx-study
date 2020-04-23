# Task Description

After running `python main.py`, the program copies all files and directories under the `data` directory to `output` directory. 
In the process directory or file names containing dates are renamed such that the date is reformatted from `yyyy-mm-dd` format to `dd-mm-yyyy` format.

# Example Output

```
$ python main.py
$ ls data
 Photos_2019-03-22   ccc.txt   data-02-01-1994.txt  'mybook at 2020-04-01.txt'
$ ls output
 Photos_22-03-2019   ccc.txt   data-02-01-1994.txt  'mybook at 01-04-2020.txt'
```