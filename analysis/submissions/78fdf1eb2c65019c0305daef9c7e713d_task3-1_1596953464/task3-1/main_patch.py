# Example code, write your program here
import os,re
import shutil
from os.path import isdir


def Changer():
    for subdir, dirs, files in os.walk("./data/"):
        for file in files:
            # Renaming files if a date was found
            date = re.search(r'(.*)((\d\d\d\d)\-(\d\d)\-(\d\d))(.*)', file)
            if date:
                new_file = date[1]+date[5]+'-'+date[4]+'-'+date[3]+date[6]
            else:
                new_file = file
            # Renaming folders if a date was found
            date = re.search(r'(.*)((\d\d\d\d)\-(\d\d)\-(\d\d))(.*)', subdir)
            if date:
                new_path = date[1] + date[5] + '-' + date[4] + '-' + date[3] + date[6]
            else:
                new_path = subdir
            new_path = re.search(r'(\.\/data\/)(.*)', new_path)
            new_path = './output/' + new_path[2]
            # Create a new folder if it doesn't exist
            if not os.path.exists(new_path):
                os.makedirs(new_path)
            shutil.copy2(subdir + '/' + file, new_path+ '/' + new_file)

    return

if __name__=='__main__':
    Changer()