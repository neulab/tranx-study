# Example code, write your program here
import shutil
import os
# ---- BEGIN AUTO-GENERATED CODE ----
# ---- 2d586nvhojg9qq9s2qosiuecq ----
# query: import json parsing library
# to remove these comments and send feedback press alt-G
import json
# ---- END AUTO-GENERATED CODE ----


for root, subDirs, files in os.walk('data/'):
    print(root, subDirs, files)
    stTxt = ""
    stJson = []
    for file in sorted(files):
        if file.lower().endswith('.txt'):
            stTxt += open(os.path.join(root, file), 'r').read() + '\n'
        # ---- BEGIN AUTO-GENERATED CODE ----
        # ---- pjm5k7mhd7sfcc32j8xm6iid8 ----
        # query: check if file ends with .json
        # to remove these comments and send feedback press alt-G
        if file.lower().endswith('.json'):
            stJson += json.load(open(os.path.join(root, file), 'r'))
        # ---- END AUTO-GENERATED CODE ----
    d = '/'.join(root.split('/')[:-1]).replace('data', 'output')
    dd = root.split('/')[-1].replace('data', 'output')
    if not os.path.exists(d):
        os.mkdir(d)
    if not stTxt=='':
        fTxt = open(root.replace('data', 'output') + '.txt', 'w')
        fTxt.write(stTxt)
        fTxt.flush()
        fTxt.close()
    if not stJson == []:
        json.dump(stJson, open(root.replace('data', 'output') + '.json', 'w'))

