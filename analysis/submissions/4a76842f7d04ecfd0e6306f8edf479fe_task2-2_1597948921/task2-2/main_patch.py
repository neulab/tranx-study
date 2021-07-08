# Example code, write your program here
import os

path = "data/"
patho = "output/"
for i in os.listdir(path):
    if i.endswith(".txt"):
        f = open(path + i,'r',encoding="utf8",errors="ignore")
        reader = f.read()
        reader = reader.lstrip()
        f1 = open(patho + i,'w')
        f1.write(reader)
        reader=""