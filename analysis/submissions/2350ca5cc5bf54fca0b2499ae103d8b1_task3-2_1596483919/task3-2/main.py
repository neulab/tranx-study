# Example code, write your program here
import os
import json

txt_files = list()
json_files = list()
d = dict()

for dir in os.listdir('data'):
    d[dir] = {'text':[], 'json':[]}
    for file in os.listdir('data/'+dir):
        if '.txt' in file:
            txt_files.append('data/'+dir+'/'+file)
            d[dir]['text'].append('data/'+dir+'/'+file)
        elif '.json' in file:
            json_files.append('data/'+dir+'/'+file)
            d[dir]['json'].append('data/' + dir + '/' + file)

for dir in d:
    if len(d[dir]['text']) > 0:
        with open('output/'+dir+'.txt', 'w+') as textfile:
            for file in d[dir]['text']:
                with open(file) as inputtextfile:
                    textfile.write(inputtextfile.read())
    if len(d[dir]['json']) > 0:
        json_list = list()
        id = 1
        for file in d[dir]['json']:
            with open(file) as jsonfile:
                json_dict = json.load(jsonfile)
                for el in json_dict:
                    element = el.copy()
                    element['id'] = id
                    id += 1
                    json_list.append(element)
        with open('output/' + dir + '.json', 'w+') as jsonfile:
            jsonfile.write(str(json_list))