# Example code, write your program here

import os
import re
import shutil
from datetime import datetime

pattern = re.compile(r"^(.*)(\d{4}-\d{2}-\d{2})(.*)")


def p(root, file):
    sr = os.path.join('data', root)
    src_path = os.path.join(sr, file)
    dr = os.path.join('output', root)
    os.makedirs(dr, exist_ok=True)
    m = pattern.search(file)
    if None is m:
        dst_path = os.path.join(dr, file)
    else:
        pre, t, suf = m.groups()
        tt = datetime.strptime(t, '%Y-%m-%d').strftime('%d-%m-%Y')
        dst_path = os.path.join(dr, '{pre}{t}{suf}'.format(pre=pre, t=tt, suf=suf))
    shutil.copy(src_path, dst_path)


for root, subdirs, files in os.walk('data'):
    for file in files:
        p('/'.join(root.split('/')[1:]), file)
