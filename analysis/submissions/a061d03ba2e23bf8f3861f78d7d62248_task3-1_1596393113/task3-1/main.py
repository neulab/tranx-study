# Example code, write your program here
from shutil import copyfile
from glob import glob
import re
import os

get_dir = lambda d: '/'.join(d.split('/')[:-1])

# yyyy-mm-dd format to dd-mm-yyyy format
test_string = '/something/else-2020-08-21/2020-09-12.png'
p = re.compile('([0-9]{4})-([0-9]{2})-([0-9]{2})')

fix_dates = lambda s: p.sub(r'\3-\2-\1', s)

for fname in glob('data/**/*.*', recursive=True):
    dest = fname.replace('data/', 'output/')
    dest = fix_dates(dest)
    dest_dir = get_dir(dest)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    copyfile(fname, dest)