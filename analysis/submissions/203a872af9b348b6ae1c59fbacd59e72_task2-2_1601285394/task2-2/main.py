# Example code, write your program here
from os import listdir
from os.path import isfile, join

mypath = 'data'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles = [f for f in onlyfiles if '.txt' in f]

for file in onlyfiles:
    with open('data/' + file, encoding='ISO-8859-15') as f:
        data = f.read()
    with open('output/' + file, 'w', encoding='utf-8') as f:
        data = data.strip()
        f.write(data)

