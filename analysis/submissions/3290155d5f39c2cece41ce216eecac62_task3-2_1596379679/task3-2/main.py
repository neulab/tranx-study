# Example code, write your program here
import os
import sys
import json

rootdir = 'output'

for root, subdir, files in os.walk(rootdir):
    for file in files:
        filepath = os.path.join(root, file)
        if filepath.endswith(".txt") or filepath.endswith(".json"):
            os.remove(filepath)

rootdir = 'data'



for root, subdir, files in os.walk(rootdir):
    for file in files:
        filepath = os.path.join(root, file)
        if filepath.endswith(".txt"):
            if os.path.exists('output/'+root.split('/')[1]+'.txt'):
                append_write = 'a'  # append if already exists
            else:
                append_write = 'w'  # make a new file if not
            out = open('output/'+root.split('/')[1]+'.txt', append_write)
            inp = open(filepath, 'r')
            out.write(inp.read())
            out.close()
            inp.close()
        if filepath.endswith(".json"):
            inp = open(filepath, 'r')
            newJ = json.loads(inp.read())
            try:
                out = open('output/'+root.split('/')[1]+'.json', 'r')
                oldJ = json.loads(out.read())
                l=list()
                for i in oldJ:
                    l.append(i)
                for i in newJ:
                    l.append(i)
                out.close()
                out = open('output/'+root.split('/')[1]+'.json', 'w')
                json.dump(l,out)
            except:
                out = open('output/' + root.split('/')[1] + '.json', 'w')
                json.dump(newJ,out)
            out.close()
            inp.close()