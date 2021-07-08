# Example code, write your program here
import os

path = "/vagrant/task2-2/data"
output_path = "/vagrant/task2-2/output"
for filename in os.listdir(path):
    if filename.endswith(".txt") :
        f = open(path + '/' + filename,'r+',encoding="iso-8859-15")
        reader = f.read()
        f.close()
        f1 = open(output_path + '/' + filename,'w',encoding="utf-8")
        f1.write(str(reader).lstrip())
        f1.close()