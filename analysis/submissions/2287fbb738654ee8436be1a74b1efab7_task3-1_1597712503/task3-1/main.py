# ---- BEGIN AUTO-GENERATED CODE ----
# ---- ul4zsiu17d6lqf3syrayun5ke ----
# query: copy directory to another directory
# to remove these comments and send feedback press alt-G
# query: copy directory to directory
# to remove these comments and send feedback press alt-G
import os
import shutil
import re


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


copytree('data/', 'output/', False, None)


for subdir, dirs, files in os.walk('output/'):
    for file in files:
        name = []
        filepath = subdir + os.sep + file
        try:
            name = re.findall(r'(.*)(\d\d\d\d)-(\d\d)-(\d\d)(.*)', file)
            os.rename(filepath, subdir+os.sep+name[0][0]+name[0][3]+"-"+name[0][2]+"-"+name[0][1])
        except:
            print("")

for subdir, dirs, files in os.walk('output/'):
    for file in dirs:
        name = []
        filepath = subdir + os.sep + file
        try:
            name = re.findall(r'(.*)(\d\d\d\d)-(\d\d)-(\d\d)(.*)', file)
            os.rename(filepath, subdir + os.sep + name[0][0] + name[0][3] + "-" + name[0][2] + "-" + name[0][1])
        except:
            print("")

# ---- END AUTO-GENERATED CODE ----
