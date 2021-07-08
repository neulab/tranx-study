# Example code, write your program here
import os
from shutil import copyfile
import codecs

for file in os.listdir('data/'):
    if file.endswith('.txt'):
        with codecs.open('data/'+file, 'r', 'ISO-8859-15') as fin, codecs.open('output/'+file, 'w', 'utf8') as fout:
            for line in fin:
                data = line.strip()
                if data == '':
                    continue
                data = data+'\n'
                fout.write(data)
    else:
        copyfile('data/'+file, 'output/'+file)
