import os
import json

data = './data/'
output = './output/'

for dire in os.listdir(data):
    sub = data+dire+'/'
    res = []
    flag = ''
    id = 1
    if os.path.isdir(sub):
        for file in os.listdir(sub):
            if '.txt' in file:
                flag = 'txt'
                f = open(sub + file,  'r').readlines()
                res.extend(f)
            elif '.json' in file:
                flag = 'json'
                f = open(sub+file,)
                j = json.load(f)
                for item in j:
                    item['id'] = id
                    id += 1
                res.extend(j)
                f.close()

    if flag == 'txt':
        x = open(output+dire+'.txt', 'w')
        x.writelines(res.copy())
        x.close()
        res.clear()
    elif flag == 'json':
        x = open(output + dire + '.json', 'w')
        json.dump(res.copy(), x)
        x.close()
        res.clear()
        id = 1
    flag = ' '
