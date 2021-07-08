import os, errno
directory = "output"

try:
    os.makedirs(directory)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

with open("data.csv", "r") as in_file, open("output/output.csv", "w+") as out_file:
    lines = in_file.readlines()
    out_file.writelines(lines[1:-1:1])





