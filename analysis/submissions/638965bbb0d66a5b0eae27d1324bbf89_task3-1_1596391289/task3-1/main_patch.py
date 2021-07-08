import os
import shutil
import re
from datetime import datetime


def format_date(name):
    match = re.search(r'\d{4}-\d{2}-\d{2}', name)
    if not match:
        return name
    date = datetime.strptime(match.group(), '%Y-%m-%d')
    old_date = date.strftime('%Y-%m-%d')
    formatted_date = date.strftime('%d-%m-%Y')
    formatted_name = name.replace(old_date, formatted_date)
    # recursive call to check for multiple contained dates
    return format_date(formatted_name)


# copies everything and renames top level directories/files
for anyfile in os.listdir("data"):
    file_path = os.path.join("data", anyfile)
    if os.path.isdir(file_path):
        shutil.copytree(file_path, format_date(os.path.join("output", anyfile)))
    elif os.path.isfile(file_path):
        shutil.copy(file_path, format_date(os.path.join("output", anyfile)))
    else:
        print("Error")

for root, dirs, files in os.walk("output"):
    for directory in dirs:
        os.rename(os.path.join(format_date(root), directory), format_date(os.path.join(root, directory)))
    for old_file in files:
        os.rename(os.path.join(format_date(root), old_file), format_date(os.path.join(root, old_file)))
