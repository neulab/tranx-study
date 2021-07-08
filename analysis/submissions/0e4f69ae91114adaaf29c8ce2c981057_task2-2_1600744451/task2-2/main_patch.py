# Example code, write your program here
import os
import shutil

files = os.listdir("data/")
for file in files:
    path = "data/" + file
    write_path = "output/" + file
    if '.txt' in file:
        with open(path, 'rb') as f:
            s = f.readlines()
            f.close()
        s_edited = []
        for line in s:
            s_edited.append(line.strip().decode('iso-8859-1') + '\n')
        s_edited = ''.join(s_edited).strip()
        with open(write_path, 'w') as f:
            f.write(s_edited)
            f.close()
    else:
        shutil.copyfile(path, write_path)