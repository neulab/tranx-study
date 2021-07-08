# Example code, write your program here
import os
import codecs

directory = 'data/'
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        print(os.path.join(directory, filename))
        inp = codecs.open('data/'+filename, 'r', encoding='iso-8859-15', errors='backslashreplace')
        out = codecs.open('output/'+filename, 'w', encoding='utf-8')
        string = inp.read()
        lines = string.splitlines()
        string = '\n'.join(lines)
        string = string.strip()
        out.write(string)
        inp.close()
        out.close()
    else:
        continue