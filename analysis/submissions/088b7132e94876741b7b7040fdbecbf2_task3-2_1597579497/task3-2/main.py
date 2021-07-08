# Example code, write your program here
import os
import json
Datapath = '/vagrant/task3-2/data'
Outputpath = '/vagrant/task3-2/output'

string =""
y=[]

for i in os.listdir(Datapath):
    path = Datapath+'/'+i
    for j in os.listdir(path):
        if j.endswith(".txt"):
            variable =i
            fd = open(path+'/'+j,'r')
            string += fd.read()

        elif j.endswith(".json"):
            var1 = i
            with open(path+'/'+j,'rb') as f:
                y.append(json.load(f))
k=0
for i in y:
    for j in i :
        if j == 1:
            y[i][j]=k
            k+=1

f2 = open(Outputpath+'/'+variable+'.txt','w')
f2.write(string)

f3=open(Outputpath+'/'+var1+'.txt','w')
json.dump(y,f3)