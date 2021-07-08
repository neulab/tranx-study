# Example code, write your program here
import os

folderData = "data"
folderOut  = "output"

for filename in os.listdir(folderData):
    if filename.endswith(".txt"):
        f1 = open(folderData + '/' + filename, 'r+',encoding='utf8',errors="ignore")

        reader = f1.read()
        f1.close()
        f2 = open(folderOut + '/' + filename, 'w',encoding='utf8',errors="ignore")
        f2.write(reader.lstrip())
        f2.close()
