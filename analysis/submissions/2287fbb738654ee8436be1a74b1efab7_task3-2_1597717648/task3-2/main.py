# Example code, write your program here
import os
import string
import json


str = ""

listaya = []
for subdir, dirs, files in os.walk('data/'):
    for file in files:
        if file.endswith('.txt'):
            f = open(subdir + os.sep + file,'r')
            s = f.read()
            f.close()
            try:
                f1 = open('output/'+subdir.split('/')[len(subdir.split('/'))-1], 'a')
            except:
                f1 = open('output/' + subdir.split('/')[len(subdir.split('/')) - 1], 'w+')

            f1.write(s)
            f1.close()
        elif file.endswith('.json'):
            f = open(subdir + os.sep + file, 'r')
            s = f.read()
            f.close()

            for i in json.loads(s):
                listaya.append(i)
st = json.dumps(listaya)
f2 = open('output/roster.json', 'w')
f2.write(st)
f2.close()


