# Example code, write your program here

import os
import shutil

if not os.path.exists('output/'):
    os.mkdir('output/')

for filename in os.listdir('data/'):
    if filename.endswith('.txt'):
        f = open('data/' + filename, 'r', encoding='ISO-8859-15')
        st = f.read().replace('\r\n', '\n')
        fNew = open('output/' + filename, 'w', encoding='utf-8')
        fNew.write(st)
        fNew.flush()
        fNew.close()
    else:
        shutil.copy2('data/' + filename, 'output/' + filename)

