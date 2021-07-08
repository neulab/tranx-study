# Example code, write your program here
import os
import re
from shutil import copyfile, copytree

def copy_data(dir_path):
    files = os.listdir(dir_path)
    for file in files:
        src_path = dir_path + file
        dest_path = 'output/' + re.sub(r'(\d\d\d\d)-(\d\d)-(\d\d)', r'\3-\2-\1', src_path)[5:]
        if os.path.isfile(src_path):
            copyfile(src_path, dest_path)
            pass
        else:
            os.mkdir(dest_path)
            copy_data(src_path + '/')

copy_data('data/')
