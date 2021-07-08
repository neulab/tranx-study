# Example code, write your program here
import os
from distutils.dir_util import copy_tree
import shutil
import re

for subdir, dirs, files in os.walk('output'):
    for file in files:
        if file != '.gitkeep':
            os.remove(os.path.join(subdir, file))


for root, dirs, files in os.walk('output', topdown=False):
    for name in files:
        if name != '.gitkeep':
            os.remove(os.path.join(root, name))
    for name in dirs:
        if name != '.gitkeep':
            os.rmdir(os.path.join(root, name))

fromDirectory = "data"
toDirectory = "output"
copy_tree(fromDirectory, toDirectory)


for subdir, dirs, files in os.walk('output', topdown=False):
    for name in files:
        if name != '.gitkeep':
            #print(os.path.join(subdir, file))
            string = re.findall(r'(\/*)([0-9][0-9][0-9][0-9])-([0-9][0-9])-([0-9][0-9])(\/*)',name)
            print(name)
            if string != []:
                old = string[0][1]+'-'+string[0][2]+'-'+string[0][3]
                new = string[0][3]+'-'+string[0][2]+'-'+string[0][1]
                newName = name.replace(old, new)
            else:
                newName = name
            print(newName)
            os.rename(os.path.join(subdir, name), os.path.join(subdir, newName))

for subdir, dirs, files in os.walk('output', topdown=False):
        for name in dirs:
            if name != '.gitkeep':
                string = re.findall(r'(\/*)([0-9][0-9][0-9][0-9])-([0-9][0-9])-([0-9][0-9])(\/*)', name)
                print(name)
                if string != []:
                    old = string[0][1] + '-' + string[0][2] + '-' + string[0][3]
                    new = string[0][3] + '-' + string[0][2] + '-' + string[0][1]
                    newName = name.replace(old, new)
                else:
                    newName = name
                print(newName)
                os.rename(os.path.join(subdir, name), os.path.join(subdir, newName))