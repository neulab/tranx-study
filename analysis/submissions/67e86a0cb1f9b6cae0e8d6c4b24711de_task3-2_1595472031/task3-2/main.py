# Example code, write your program here
import os
import json
dirs = os.listdir('data')
for dir in dirs:
    if not os.path.isdir(os.path.join('data',dir)):
        continue
    dir_files = os.listdir(os.path.join('data',dir))
    if len(dir_files) == 0:
        continue
    if dir_files[0].endswith('.txt'):
        with open(os.path.join('output/{}.txt'.format(dir)), 'w') as out:
            files = sorted(dir_files)
            for f in files:
                with open(os.path.join('data',dir,f)) as in_f:
                    out.write(in_f.read())
    elif dir_files[0].endswith('.json'):
        files = sorted(dir_files)
        lst_all = []
        for f in files:
            with open(os.path.join('data',dir,f)) as in_f:
                lst = json.load(in_f)
                for l in lst:
                    l['id'] = len(lst_all) + 1
                    lst_all.append(l)
        with open(os.path.join('output','{}.json'.format(dir)),'w') as out:
            json.dump(lst_all,out)
