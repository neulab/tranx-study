# Example code, write your program here
import os
import shutil
k=os.listdir("data")
for i in k:
    l=i.split('.')
    if l[1]=='txt':
        with open('data/'+i,'r',encoding='ISO-8859-15') as file:
            l=file.read().strip()
            with open("output/"+i,'w',encoding='UTF-8') as file1:
                file1.write(l)
    else:
        shutil.copy('data/'+i,'output/'+i)
