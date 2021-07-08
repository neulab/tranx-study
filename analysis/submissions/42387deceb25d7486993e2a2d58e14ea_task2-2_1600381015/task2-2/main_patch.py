# Example code, write your program here
import os
import shutil
for file in os.listdir('data'):
    if file.endswith('.txt'):
        fin = open(os.path.join('data', file), 'r', encoding = 'ISO-8859-15')
        f = fin.readlines()
        start = end = None
        for i in range(len(f)):
            if f[i].strip():
                start = i
                break
        for i in range(len(f) - 1, -1, -1):
            if f[i].strip():
                end = i
                break
        f[start] = f[start].lstrip()
        f[end] = f[end].rstrip()
        out = open(os.path.join('output', file), 'w')
        for line in f[start:end + 1]:
            out.write(line)
        fin.close()
        out.close()
    else:
        shutil.copyfile(os.path.join('data', file), os.path.join('output', file))

