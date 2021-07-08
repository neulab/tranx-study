import os
import json

dic_txt = {}
dic_json = {}
for root, dirnames, filenames in os.walk('data'):
    for f in filenames:
        if 'json' in f:
            dic_json[root] = filenames
        if 'txt' in f:
            dic_txt[root] = filenames

for txt in dic_txt:
    dir = txt
    files = dic_txt[txt]

    data = []
    files = sorted(files)
    for f in files:
        with open(dir + "/" + f, 'r') as inp:
            data.append(inp.read())

    with(open('output/' + dir.split("/")[-1] + ".txt", 'w')) as out:
        out.write(''.join(data))

for js in dic_json:
    dir = js
    files = dic_json[js]

    data = []
    files = sorted(files)
    for f in files:
        with open(dir + "/" + f) as inp:
            items = json.load(inp)
        for it in items:
            data.append(it)
    id = 1
    for d in data:
        d['id'] = id
        id += 1
    in_str = json.dumps(data)
    with(open('output/' + dir.split("/")[-1] + ".json", 'w')) as out:
        out.write(in_str)

