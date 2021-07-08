# Example code, write your program here
import os,shutil
import re,datetime
directory = 'output'
extensions = (['.txt','.png'])
def copytree(src,dst,symlinks=False,ignore=None):
    for item in os.listdir(src):
        s= os.path.join(src, item)
        d= os.path.join(dst,item)
        if os.path.isdir(s):
            shutil.copytree(s,d,symlinks,ignore)
        else:
            shutil.copy2(s,d)

copytree('data','output',symlinks=False,ignore=None)

path ='output/'
format ="%Y-%m-d"
for root, dirs, files in os.walk(path):
    for file in files:
        filename, extension = os.path.splitext(file)
        match = re.search('\d{4}-\d{2}-\d{2}', filename)
        if match != None:
            index = match.start()
            date = datetime.datetime.strptime(match.group(), '%Y-%m-%d').strftime('%d-%m-%Y')
            filename = re.sub('\d{4}-\d{2}-\d{2}', date, filename)
            newfile = filename + extension
            os.rename(os.path.join(root, file), os.path.join(root, newfile))
filelist = os.listdir('output')
format ="%Y-%m-d"
for file in filelist:
    filename, extension = os.path.splitext(file)
    match = re.search('\d{4}-\d{2}-\d{2}', filename)
    if match != None:
        index = match.start()
        date = datetime.datetime.strptime(match.group(), '%Y-%m-%d').strftime('%d-%m-%Y')
        filename=re.sub('\d{4}-\d{2}-\d{2}',date,filename)
        newfile = filename+extension
        newfilename = "output/"+newfile
        oldfilename = "output/"+file
        os.rename(oldfilename, newfilename)