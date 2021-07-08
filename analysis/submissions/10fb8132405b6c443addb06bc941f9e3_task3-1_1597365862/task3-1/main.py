# Example code, write your program here
import shutil
import os
import re
import datetime as dt
import time
from datetime import datetime

srcc = "/vagrant/task3-1/data"
dstt = "/vagrant/task3-1/output"


def recursive_copy(src, dst):
    for files in os.listdir(src):
        if os.path.isfile(src + '/' + files):
            if not os.path.exists(dst + '/' + files):
                shutil.copy(src + '/' + files, dst)
        elif os.path.isdir(src + '/' + files):
            if not os.path.exists(dst + '/' + files):
                os.mkdir(dst + '/' + files)
                recursive_copy(src + '/' + files, dst + '/' + files)


def change_name(dst):
    for file in os.listdir(dst):
        match = re.search(r'\d\d\d\d-\d\d+-\d\d', file)
        if match:
            old_format = match.group()
            d = dt.datetime.strptime(old_format, '%Y-%m-%d')
            d = d.date()
            new_format = d.strftime('%d-%m-%Y')
            new_name = file.replace(old_format, new_format)
            if os.path.isfile(dst + '/' + file):
                if file != new_name:
                    os.rename(dst + '/' + file, dst + '/' + new_name)
            elif os.path.isdir(dst + '/' + file):
                if file != new_name:
                    os.rename(dst + '/' + file, dst + '/' + new_name)
                dst = dst + '/' + new_name
                change_name(dst)


if len(os.listdir(dstt)) == 0:
    recursive_copy(srcc, dstt)
time.sleep(1)
change_name(dstt)
