# Example code, write your program here
import os


path = "/vagrant/task2-2/data"
path_out = "/vagrant/task2-2/output"


for filename in os.listdir(path):
    if filename.endswith(".txt"):
        f = open(path + '/' + filename, 'r+')
        reader = f.read()
        f.close()
        f1 = open(path_out + '/' + filename, 'w')
        f1.write(reader.lstrip())
        f1.close()

