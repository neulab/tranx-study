# Example code, write your program here
import shutil
import datetime
import os


def dateConverter(s):
    st = s + ''
    for i in range(len(st)-10):
        try:
            #print(st[i:i+10])
            dt = datetime.datetime.strptime(st[i:i+10], '%Y-%m-%d')
            st = st.replace(st[i:i+10], dt.strftime('%d-%m-%Y'))
            #print(st)
        except Exception:
            continue
    return st


for root, subDirs, files in os.walk('data/'):
    for subDir in subDirs:
        os.mkdir(dateConverter(os.path.join(root.replace('data', 'output'), subDir)+'/'))
    for file in files:
        shutil.copy2(os.path.join(root, file), dateConverter(os.path.join(root.replace('data', 'output'), file)))
