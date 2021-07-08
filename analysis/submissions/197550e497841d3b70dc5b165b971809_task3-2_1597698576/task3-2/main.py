# Example code, write your program here
import os
import json
pathData = '/vagrant/task3-2/data'
pathOutput = '/vagrant/task3-2/output'

x=""
y=[]
for i in os.listdir(pathData) :
    path = pathData +'/'+i
    for j in os.listdir(path) :
        if j.endswith(".txt") :
            var=i
            f1=open(path+'/'+j , 'r')
            x+=f1.read()

        elif j.endswith(".json") :
            var1 = i
            with open(path+'/'+j , 'rb') as f :
                y.append(json.load(f))


f2= open(pathOutput+'/'+var+'.txt','w')
f2.write(x)

f3= open(pathOutput+'/'+var1+'.txt','w')
json.dump(y,f3)

