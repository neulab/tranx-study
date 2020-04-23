# Task Description

After running `python main.py`, the program extracts required information from the HTML page `http://inklab.usc.edu/project-NExT/`. 

Specifically, save all the hyperlink URLs (one URL per line) to `output/urls.txt`, all the bold text phrases (one per line) to `output/bold.txt`, and all `crimson` colored text phrases (one per line) into `output/crimson.txt`

# Example Output

```
$ python main.py
$ ls output
urls.txt  bold.txt  crimson.txt
$ less output/urls.txt
https://openreview.net/forum?id=rJlUt0EYwS
https://github.com/INK-USC/NExT
....
$ less output/bold.txt
exps
categs
avg ops
...
$ less output/crimson.txt
Learning from Explanations with Neural Execution Tree
Abstract
...

```