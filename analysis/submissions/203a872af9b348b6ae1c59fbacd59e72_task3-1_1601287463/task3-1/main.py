from distutils.dir_util import copy_tree
import glob
import os
import re

src = 'data'
dest = 'output'
fromDirectory = src
toDirectory =  dest

copy_tree(fromDirectory, toDirectory)

print(glob.glob("output/**/*.*", recursive = True))
for full_name in glob.glob("output/*.*"):

    name = full_name.split("/")[-1]
    dt = re.findall(r'\b\d{4}-\d\d?-\d\d?\b', name)
    if not dt:
        continue
    start = name.index(dt[0])
    dt = dt[0].split("-")
    new_name = name[:start] + dt[-1] + "-" + dt[-2] + "-" + dt[-3] + name[start+10:]
    full_new_name = ''.join(full_name.split("/")[:-1]) + "/" + new_name
    os.rename(full_name, full_new_name)
