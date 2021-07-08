# Example code, write your program here
import os
import re

pat =re.compile('(\d\d\d\d)-(\d\d)-(\d\d)')
os.system('cp -r data/* output/')
for root, dirs, filenames in os.walk('output', topdown=False):
    for filename in filenames:
        o = pat.sub('\\2-\\3-\\1', filename)
        os.renames(os.path.join(root, filename), os.path.join(root, o))
    for d in dirs:
        o = pat.sub('\\2-\\3-\\1', d)
        os.renames(os.path.join(root, d), os.path.join(root, o))