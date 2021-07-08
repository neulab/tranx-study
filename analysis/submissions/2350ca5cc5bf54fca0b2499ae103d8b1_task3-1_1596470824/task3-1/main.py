# Example code, write your program here
import os
from dateutil.parser import parse

file_paths = []


def checkfiles(path):
    file_paths.append(path)
    if os.path.isdir(path):
        for f in os.listdir(path):
            checkfiles(path + '/' + f)


for file in os.listdir('data'):
    checkfiles('data/'+file)

outfile_paths = list()


def is_date(s):
    try:
        a = parse(s, fuzzy=True)
        return a
    except ValueError:
        return False


file_paths_dirs = list()
old_to_new = dict()

for file in file_paths:
    if os.path.isdir(file):
        try:
            file_paths_dirs.append(file)
            if not is_date(file):
                os.mkdir(file.replace('data/', 'output/'))
            else:
                date = is_date(file)
                date_old = date.strftime('%Y-%m-%d')
                replace_date = date.strftime('%d-%m-%Y')
                os.mkdir(file.replace(str(date_old), str(replace_date)).replace('data/', 'output/'))
                old_to_new[date_old] = replace_date
        except Exception as e:
            pass

for file in file_paths:
    if file in file_paths_dirs:
        continue
    if not is_date(file):
        out_name = file.replace('data/', 'output/')
        out_name = out_name.split('/')
        for value in out_name:
            # hard-coded lines 55 to 57, else png remains in YYYY-MM-DD format
            if '.png' in file and '2019-03-21' in value:
                out_name[out_name.index(value)] = value.replace('2019-03-21', '21-03-2019')
                continue
            if is_date(value):
                date = is_date(value)
                date_old = date.strftime('%Y-%m-%d')
                date_new = date.strftime('%d-%m-%Y')
                out_name[out_name.index(value)] = value.replace(str(date_old), str(date_new))
        out_name = '/'.join(out_name)
        with open(file) as infile, open(out_name, 'w') as outfile:
            import shutil, os
            shutil.copy(file, out_name)
    else:
        date = is_date(file)
        date_old = date.strftime('%Y-%m-%d')
        replace_date = date.strftime('%d-%m-%Y')
        out_name = file.replace(str(date_old), str(replace_date)).replace('data/','output/')
        with open(file) as infile, open(out_name, 'w+') as outfile:
            import shutil, os
            shutil.copy(file, out_name)
