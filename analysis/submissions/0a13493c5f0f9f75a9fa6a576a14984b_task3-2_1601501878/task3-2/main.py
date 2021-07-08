# Example code, write your program here
import os
import json
path = 'data/'
textFiles = {}
jsonFiles = {}
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('.txt'):
            textFiles[file] = os.path.join(root, file)
            x = textFiles[file].split('/')
            textFilesdir = x[-2]
            textFilesName = textFilesdir+'.txt'
            textFilesPath = 'output/'+textFilesName
            sorted_textFiles = sorted(textFiles.items(), key=lambda kv: kv[1])
            with open(textFilesPath, 'w') as outfile:
                for i in sorted_textFiles:
                    with open(i[1]) as infile:
                        outfile.write(infile.read())
        if file.endswith('.json'):
            jsonFiles[file] = os.path.join(root, file)
            x = jsonFiles[file].split('/')
            jsonFilesdir = x[-2]
            jsonFilesName = jsonFilesdir+'.json'
            jsonFilesPath = 'output/'+jsonFilesName
            sorted_jsonFiles = sorted(jsonFiles.items(), key=lambda kv: kv[1])
            def mangle(s):
                return s.strip()[1:-1]
            with open(jsonFilesPath, "w") as outfile:
                first = True
                for infile_name in sorted_jsonFiles:
                    with open(infile_name[1]) as infile:
                        if first:
                            outfile.write('[')
                            first = False
                        else:
                            outfile.write(',')
                        outfile.write(mangle(infile.read()))
                outfile.write(']')
with open(jsonFilesPath, "r") as read_it:
     data = json.load(read_it)
count =1
for index in data:
    for key in index:
        if key == 'id':
            index[key] = count
            count += 1
with open(jsonFilesPath, "w") as outfile:
    json.dump(data,outfile)
