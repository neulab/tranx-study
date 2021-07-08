# Example code, write your program here
from os import walk

import os
import re
import re
from datetime import datetime
from scipy.stats import moment
import shutil

out_path ="output"
source_path ="data1"
Newname =''
new_files = []
arr = os.listdir(source_path)
new_files = arr
count =0
while count < len(arr) :
    arr = os.listdir(source_path)
    if len(arr) == count:
        break;
    for i in range(len(arr)):
    # get data from files and folders name
        match = re.search(r'\d{4}-\d{2}-\d{2}', arr[i])
        if (match):
            date = datetime.strptime(match.group(), '%Y-%m-%d').date()
            str2= date.strftime('%d-%m-%Y')
            Newname = re.sub(r'\d{4}-\d{2}-\d{2}',str2,arr[i])
            os.rename(os.path.join(source_path,arr[i]),os.path.join(source_path,Newname))
            arr[i] = Newname
        if re.findall('.txt', arr[i]) or re.findall('.png', arr[i]):
            count +=1
            shutil.copy(os.path.join(source_path,arr[i]), os.path.join(out_path,Newname))
        else:
            count = 0
            # make Folder
            os.makedirs(os.path.join(out_path,arr[i]))
            source_path = os.path.join(source_path,arr[i])
            out_path=os.path.join(out_path,arr[i])



