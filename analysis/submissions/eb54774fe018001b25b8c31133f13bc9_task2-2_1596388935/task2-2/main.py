# Example code, write your program here
import os
import codecs
from shutil import copyfile
if not os.path.exists("output"):
    os.mkdir("ouput")

for file in os.listdir("data"):
    if file.endswith(".txt"):
        # print(os.path.join("data", file))
        with codecs.open(os.path.join("data", file), 'r', encoding='ISO-8859-15') as f:
            text = f.read()
        # process Unicode text

        with codecs.open("output/"+file, 'w', encoding='utf8') as f:
            f.write(text.strip())
    else:
        copyfile(os.path.join("data", file), "output/"+file)

