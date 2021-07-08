# Example code, write your program here
import  os
import shutil
import re
import datetime as dt
import time

source = 'data'
dest = 'output'


print(os.listdir(source))
if not os.path.isdir(dest) :
    shutil.copytree(source,dest)
def copyFiles(destination) :
    for i in os.listdir(destination):
        x= re.search(r'\d\d\d\d-\d\d-\d\d',i)
        if x :
            date=x.group()
            print(x.group())
            d=dt.datetime.strptime(date,'%Y-%m-%d')
            d=d.date()
            new=d.strftime('%d-%m-%Y')
            print(new)
            v=i.replace(date,new)
            print(v)
            if os.path.isfile(destination+'/'+i) :
                os.rename(destination+'/'+i ,destination+'/'+v)
            elif  os.path.isdir(destination+'/'+i) :
                os.rename(destination + '/' + i, destination + '/' + v)
                destt=destination+'/'+v
                copyFiles(destt)
time.sleep(1)
copyFiles(dest)