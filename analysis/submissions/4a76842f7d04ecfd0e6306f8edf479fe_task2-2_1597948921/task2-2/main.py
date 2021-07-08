# Example code, write your program here
import os

path = "/vagrant/task2-2/data/"
patho = "/vagrant/task2-2/output/"
for i in os.listdir(path):
    if i.endswith(".txt"):
        f = open(path + i,'r',encoding="utf8",errors="ignore")
        reader = f.read()
        reader = reader.lstrip()
        f1 = open(patho + i,'w')
        f1.write(reader)
        reader=""