# Example code, write your program here
from glob import glob
import os
import json

def do_txt(files, outfile):
    ret = []
    for f in files:
        lines = open(f, 'r').readlines()
        ret.extend(lines)
    open(outfile, 'w').writelines(ret)

def do_json(files, outfile):
    data = None
    for f in files:
        with open(f, 'r') as file:
            if not data:
                data = json.load(file)
            else:
                for line in json.load(file):
                    data.append(line)

    for i, line in enumerate(data):
        data[i]['id'] = i + 1

    with open(outfile, 'w') as f:
        json.dump(data, f, indent=2)



def process_dir(d):
    files = list(glob(d + '/*'))
    try:
        ext = files[0].split('/')[-1].split('.')[1]
    except:
        ext = None
    name = d.split('/')[-1]

    if ext is None:
        return

    outfile = 'output/' + name + '.' + ext

    if ext == 'txt':
        do_txt(sorted(files), outfile)
    elif ext == 'json':
        do_json(sorted(files), outfile)
    else:
        raise ValueError('unsupported file type')



for d in glob('data/*'):
    process_dir(d)