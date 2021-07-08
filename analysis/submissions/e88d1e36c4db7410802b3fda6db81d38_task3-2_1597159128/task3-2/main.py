# Example code, write your program here
import os
import json
import re
import string

rootdir = 'data'
target_dir='output'
txt_list = []
json_list = []

for root, subFolders, files in os.walk(rootdir):
    for file in files:
        #print(file)
        if file[-3:] == 'txt':
            txt_folder=re.split('/', root)[1] + '.txt'
            #print(txt_folder)

            # txt_folder = string.split.root("/")
            # print(txt_folder)
            f = open(os.path.join(root, file), "r")
            #f.readlines()
            with open(os.path.join(target_dir, txt_folder), 'a+') as filehandle:
                filehandle.writelines(f.readlines())

for root, subFolders, files in os.walk(rootdir):
    for file in files:
        # print(file)
        if file[-4:] == 'json':
            json_folder = re.split('/', root)[1]+'.json'
            with open(os.path.join(root, file)) as f:
                data = json.load(f)
            # f.readlines()
            with open(os.path.join(target_dir, json_folder), 'a+') as json_file:
                json.dump(data, json_file)





