# Task Description

After running `python main.py`, the program extracts required information from the HTML page `https://frankxfz.me/`. 

Specifically, save all the hyperlink URLs (one URL per line) to `output/urls.txt`, all the bold text phrases (one per line) to `output/bold.txt`, all the italics text phrases (one per line) to `output/italics.txt`, and all `red (#FF0000)` colored text phrases (one per line) into `output/red.txt`


# Example Output

```
$ python main.py
$ ls output
urls.txt  bold.txt  italics.txt  red.txt 

$ less output/urls.txt
https://www.lti.cs.cmu.edu/
https://www.cs.cmu.edu/
...

$ less output/bold.txt
A Benchmark for Structured Procedural Knowledge Extraction from Cooking Videos.
Frank F. Xu
...

$ less output/italics.txt
Indirect Supervision for Information Extraction
Proceedings of 43rd International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR)
...

$ less output/red.txt
(Best Poster Award Honorable Mention)
(2nd place in the shared task)
...
```