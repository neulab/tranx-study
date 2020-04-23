# Task Description

After running `python main.py`, the program looks at all the subdirectories in the `data` directory. 
In the process, the directories with `.txt` files in it are processed by concatenating all `.txt` files into one `.txt` file, ordered in alphanumeric order of the filenames, and named by the directory name.
The directories with `.json` files in it are processed by concatenating all the lists represented in JSON `.json` files into one list and then saved as a `.json` file, ordered in alphanumeric order of the filenames, and named by the directory name.
You are also required to re-number the `"id"` field for each object in the list starting from `1`.

# Example Output

```
$ python main.py
$ ls data
filelist  roster  todo
$ ls output
filelist.txt   roster.json
```