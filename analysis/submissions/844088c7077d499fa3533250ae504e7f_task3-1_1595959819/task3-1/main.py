import os
import pathlib
import re
import shutil


def change_dates(s):
    return re.sub(r'([0-9]{4})-([0-9]{2})-([0-9]{2})', '\\3-\\2-\\1', s)


for (dirpath, dirnames, fnames) in os.walk('data/'):
    old_path = pathlib.Path(dirpath)
    new_path = pathlib.Path('output/', *map(change_dates, old_path.parts[1:]))
    if not new_path.exists():
        new_path.mkdir()
    for fname in fnames:
        shutil.copy(old_path.joinpath(fname), new_path.joinpath(change_dates(fname)))
