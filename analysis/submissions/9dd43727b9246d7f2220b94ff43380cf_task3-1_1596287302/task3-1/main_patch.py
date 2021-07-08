# Example code, write your program here
import os, shutil
import sys

from dateutil.parser import parse
from numpy.core.defchararray import rfind
import re, datetime

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            print(s, file=sys.stderr)
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
            
def checkAndConverDateFormat (String):
    match = re.search('\d{4}-\d{2}-\d{2}', String)
    if (match != None):
        date = datetime.datetime.strptime(match.group(), '%Y-%m-%d').date()
        strDate = date.strftime('%d-%m-%Y')
        strDate2 = date.strftime('%Y-%m-%d')
        String = String.replace(strDate2, strDate)
    return String

def rename (path):
    os.chdir(path)
    for file in os.listdir(path):
        os.rename(file, checkAndConverDateFormat(file))


source = "data"
destination = "output"
copytree(source, destination)
rename("output/")
rename("output/Photos_22-03-2019")


