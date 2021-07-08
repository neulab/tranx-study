# Example code, write your program here
import os
import shutil
import re
import datetime as dt
import time

inputfolder = '/vagrant/task3-1/data'
outputfolder = '/vagrant/task3-1/output'

print(os.listdir(inputfolder))
if not os.path.isdir(outputfolder):
    shutil.copytree(inputfolder,outputfolder)

def copy (outpute):
    for i in os.listdir(outpute):
        result=re.search(r'\d\d\d\d-\d\d-\d\d',i)
        if result :
            date=result.group()
            print(result.group())
            d =dt.datetime.strptime(date,'%Y-%m-%d')
            d =d.date()
            new = d.strftime('%d-%m-%Y')
            print(new)
            v=i.replace(date.new)
            print(v)
            if os.path.isfile(outpute+'/'+i):
                os.rename(outpute+'/'+i,outpute+'/'+v)
            elif os.path.isdir(outpute+'/'+i):
                os.rename(outpute + '/' + i, outpute + '/' + v)
                outputee = outpute+'/'+v
                copy(outputee)


time.sleep(1)
copy(outputfolder)