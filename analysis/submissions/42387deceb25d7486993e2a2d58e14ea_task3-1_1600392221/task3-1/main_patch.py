# Example code, write your program here
import shutil
import os
import re
# src = os.getcwd() + '/data'
# dst = os.getcwd() + '/output1'
src = './data'
dst = './output'

def reformat(m):
    m = m.group(0)
    print(m)
    y, m, d = m.split('-')
    return '-'.join([d, m, y])

def copytree(src, dst):

    for item in os.listdir(src):
        s = os.path.join(src, item)
        item = re.sub('(\d{4}-(((0)[0-9])|((1)[0-2]))-([0-2][0-9]|(3)[0-1]))', reformat, item)
        d = os.path.join(dst, item)

        if os.path.isdir(s):
            print(s, d)
            if not os.path.exists(d):
                os.makedirs(d)
            copytree(s, d)
        else:
            shutil.copyfile(s, d)
            print(s, d)
copytree(src, dst)