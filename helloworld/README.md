# Hello World: A Warm Up

# Task Description

Write a program in Python 3.6 that deals with string processing following the following detailed instructions.

Please familiarize yourself with the IDE environment as well as the plugin (read [quick start](https://github.com/neulab/tranX-plugin#usage) first)

For the purpose of learning the IDE and the plugin, you will go through the process of asking the plugin about the intent, selecting one of the desired candidates, modifying the auto-generated code snippets accordingly, and eventually finalize and upload your edit.

- Open `main.py` in the PyCharm IDE editor.
- You can see there's existing code defining the variable `text`. Now we need to perform some transformations to the string.
- First, remove all non-alphanumeric characters from the `text`. Put the cursor at the line after, and bring up the query box by `Alt-Ctrl-G` (`Control+Options+G` for Mac) or click "Ask a Question" in the right click context menu, then enter "remove non-alphanumeric characters from string \`text\`". Note that we quote variable names in the query with grave accent mark (\`text\`).
- After hitting enter, we can see a list of candidates for the query intent. We select the third one: `re.sub('[^0-9a-zA-Z]+', '', text)`.
- An auto-generated code block surrounded by comments will be added to the editor. You need to check the code snippet and figure out if it is correct in this context. In this case, we first need to add the missing library for regular expressions `re` by `import re`. Then, we need to save processing result back to the variable `text`.
- After modifying, we have 
    ```
    import re
    text = re.sub('[^0-9a-zA-Z]+', '', text)
    ```
    between the comments inside the code block. Now we can test run the program to see if it works as desired. If so, we hit `Alt-G` (`Options+G` for Mac) or right click inside the code block to "Upload Edits". This will also remove the (annoying) chunk of comments surrounding the code snippet!
- Second, reverse the processed string `text`, by asking "reverse \`text\`", and select the first candidate `text[::-1]`. For this, we only need to assign the result back to `text` again and upload the edit in the same way as above.
- Third, we want to save the processed string to a text file named "out.txt". We ask "open a file "out.txt" in write mode" and select the first candidate `f = open('out.txt', 'wb')`. Note that we quote string literals with regular quotation marks ("").
- We then see the error in this generated code snippet: the write mode for text files should be `'w'` instead of `'wb'`. We modify this line of code to `f = open('out.txt', 'w')` and upload the edit to remove the comments.
- Finally, we write the string to the opened file `f` by `f.write(text)`, and close the file by `f.close()`. Now this example string processing task is complete. Run the program and see if it matches the example output shown below.


# Example Output

```
$ python3 main.py
$ cat out.txt
dlroWolleH
```