# Example code, write your program here
import json
import os
filePath = os.path.join("data","filelist")
jsonPath = os.path.join("data","roster")
outPath ="output"
files = os.listdir(filePath)
files =sorted(files)
a_list = []
for i in range(len(files)):
    with open(os.path.join(filePath,files[i]),'r') as f:
        a_list.append(f.readlines())
f.close()
with open(os.path.join(outPath,"filelist.txt"),'w') as outFile:
    for i in range(len(a_list)):
        outFile.writelines(a_list[i])
outFile.close()

files = os.listdir(jsonPath)
dic ={}
a = []
for i in range(len(files)):

    with open(os.path.join(jsonPath, files[i]), 'r') as file:
        json_data = json.load(file)
        for item in json_data:
            if i == 1:
                item['id'] += 20
            if i == 2:
                item['id'] +=40
            a.append(item)
f.close()
print(a)
with open(os.path.join(outPath,"roster.json"),'w') as outFile:
    json.dump(a, outFile)
outFile.close()
