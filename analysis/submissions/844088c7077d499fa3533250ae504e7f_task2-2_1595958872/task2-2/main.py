from os import listdir
from os.path import isfile, join
from shutil import copyfile


def clean(file):
    with open(file, 'r', encoding="ISO-8859-1") as f:
        print(file)
        return '\n'.join([line for line in f.read().strip().splitlines()]).encode('utf-8')


for fname in listdir('data/'):
    fpath = join('data/', fname)
    if isfile(fpath):
        output_path = join('output/', fname)
        if fpath.endswith('.txt'):
            with open(output_path, 'wb') as out_f:
                out_f.write(clean(fpath))
        else:
            copyfile(fpath, output_path)
