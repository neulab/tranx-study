# Example code, write your program here
import os
import codecs
from shutil import copyfile

files = os.listdir('data')
for file in files:
    if file.split(".")[-1] != 'txt':
        copyfile('data/' + file, 'output/' + file)
        continue

    heading = True
    with codecs.open('data/' + file, 'r', encoding='ISO-8859-15') as f:
        with codecs.open('output/' + file, 'w', encoding='UTF-8') as w:
            for line in f.readlines():
                if heading:
                    if line.strip():
                        line = line.lstrip()
                        w.write(line)
                        heading = False
                else:
                    w.write(line)
