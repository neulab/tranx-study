# Example code, write your program here

import os
import json

subdirs = os.listdir('data/')
for subdir in subdirs:
    path = 'data/' + subdir
    files = sorted(os.listdir(path))
    txt = ''
    json_cont = []
    for file in files:
        if '.txt' in file:
            with open(path + '/' + file, 'r') as f:
                txt += f.read()
                f.close()
        elif '.json' in file:
            with open(path + '/' + file, 'r') as f:
                json_cont.append(json.load(f))

    if len(json_cont):
        with open('output/' + subdir + '.json', 'w') as f:
            json.dump(json_cont, f)
            f.close()
    if txt:
        with open('output/' + subdir + '.txt', 'w') as f:
            f.write(txt)
            f.close()
