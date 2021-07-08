# Example code, write your program here
import os, json

rootpath = 'data'
outpath = 'output'
for dir in os.listdir(rootpath):
    subpath= os.path.join(rootpath, dir)
    files = sorted(os.listdir(subpath))
    texts = None
    jsons = []
    json_cnt = 0
    for file in files:
        path = os.path.join(subpath, file)
        if file.split('.')[-1] == 'txt':
            if texts == None: texts = open('%s/%s.txt'%(outpath, dir), 'w')
            data = open(path, 'r').readlines()
            texts.writelines(data)
        elif file.split('.')[-1] == 'json':
            data = json.load(open(path))
            for i in range(len(data)):
                json_cnt += 1
                data[i]['id'] = json_cnt
            jsons.extend(data)
    if texts != None: texts.close()
    if json_cnt > 0: json.dump(jsons, open('%s/%s.json'%(outpath, dir), 'w'))