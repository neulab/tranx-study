# Example code, write your program here
import os
import glob
import re
import os
from os import path
import shutil
import datetime
from distutils.dir_util import copy_tree
from datetime import date
#reformatted from yyyy-mm-dd format to dd-mm-yyyy format

src = 'data'
src_files = os.listdir(src)
dest = 'output'
dest_files = os.listdir(dest)

root_src_dir = 'data' #os.path.join('data/','source')
root_target_dir = 'output' #os.path.join('output/','target')

operation= 'copy' # 'copy' or 'move'

for src_dir, dirs, files in os.walk(root_src_dir):
    dst_dir = src_dir.replace(root_src_dir, root_target_dir)
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst_dir, file_)
        if os.path.exists(dst_file):
            os.remove(dst_file)
        if operation is 'copy':
            shutil.copy(src_file, dst_dir)
        elif operation is 'move':
            shutil.move(src_file, dst_dir)

for root, subdirs, files in os.walk(dest):
    #print(files)
    for file in files:
        #print(file)
        if re.search(r'(\d{4})-(\d{1,2})-(\d{1,2})', file):
            updated_files = re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', file)
            os.rename(os.path.join(root,file), os.path.join(root,updated_files))

for root, subdirs, files in os.walk(dest):
    #print(subdirs)
    for subdir in subdirs:
        #print(subdirs)
        if re.search(r'(\d{4})-(\d{1,2})-(\d{1,2})', subdir):
            updated_subdir = re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', subdir)
            os.rename(os.path.join(root, subdir), os.path.join(root, updated_subdir))



















    #re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', files)
    # if re.search(r'\d{4}[-/]\d{2}[-/]\d{2}', files) == True:
    #     re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', files)
    #     print(files)
    #print(files)
    #os.rename('a.txt', 'b.kml')





# s = "Jason's birthday is on 1991-09-21"
# match = re.search(r'\d{4}-\d{2}-\d{2}', s)
# date = datetime.datetime.strptime(match.group(), '%Y-%m-%d').date()
# print date