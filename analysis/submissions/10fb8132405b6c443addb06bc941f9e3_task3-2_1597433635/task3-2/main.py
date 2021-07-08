# Example code, write your program here
import os
import json
import glob

Data_Dir = "/vagrant/task3-2/data"
Out_Dir = "/vagrant/task3-2/output"


b = ""
c = []
for folder in os.listdir(Data_Dir):
    new_folder = Data_Dir + '/' + folder
    for file in os.listdir(new_folder):
        f = open(Data_Dir + '/' + folder + '/' + file, 'r')
        if file.endswith(".txt"):
            f.seek(0)
            b += f.read()
            text_file_name = folder
        elif file.endswith(".json"):
            json_file_name = folder
            f.close()
            with open(Data_Dir + '/' + folder + '/' + file, "rb") as infile:
                c.append(json.load(infile))

f1 = open(Out_Dir + '/' + text_file_name + ".txt", 'w')
f1.write(b)
f1.close()
with open(Out_Dir + '/' + json_file_name + ".json", 'w') as outfile:
    json.dump(c, outfile)




