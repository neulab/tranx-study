# Example code, write your program here
import os
import json
def transform(line, id):
    print(line)
    line = json.loads(line)
    line[id] = id
    return json.dumps(line)

cur = './data'
for s in os.listdir(cur):
    subdir = os.path.join(cur, s)
    dir_type = None
    for f in os.listdir(subdir):
        if f.endswith('.txt'):
            dir_type = '.txt'
            break
        elif f.endswith('.json'):
            dir_type = '.json'
            break
    if dir_type is None:
        continue
    out_file = os.path.join('./output', s) + dir_type
    fout = open(out_file, 'w')
    file_list = sorted(os.listdir(subdir))
    num = 1
    for f in file_list:
        if not f.endswith(dir_type):
            continue
        in_file = os.path.join(subdir, f)
        with open(in_file, 'r') as fin:
            if dir_type == '.txt':
                fout.write(fin.read())
            else:
                for line in json.loads(fin.read()):
                    line['id'] = num
                    num += 1
                    fout.write(json.dumps(line))

            # for line in fin.readlines():
            #     if not line.strip():
            #         continue
            #     if dir_type == '.json':
            #         line = transform(line, num)
            #         num += 1
            #     fout.write(line)
    fout.close()


