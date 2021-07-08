# Example code, write your program here

import datetime
import re
import os
import pathlib
import shutil

rootdir = 'data'

def list_filepaths(rootdir):
    def _():
        for subdir, dirs, files in os.walk(rootdir):
            for directory in dirs:
                yield pathlib.Path(os.path.join(subdir, directory))
            for file in files:
                yield pathlib.Path(os.path.join(subdir, file))
    return tuple(_())


def list_new_filepaths(filepaths):
    def _():
        for filepath in filepaths:
            match_groups = re.findall(r'(?P<date>(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2}))', str(filepath))
            new_filepath = str(filepath)
            if match_groups:
                for match_group in match_groups:
                    datestring, year, month, day = match_group
                    new_filepath = new_filepath.replace(datestring, f"{day}-{month}-{year}")
            output_filepath_parts = ["output"] + list(pathlib.Path(new_filepath).parts[1:])
            output_filepath = os.path.join(*output_filepath_parts)
            yield pathlib.Path(output_filepath)
    return tuple(_())

filepaths = list_filepaths(rootdir)
output_filepaths = list_new_filepaths(filepaths)

for input_filepath, output_filepath in zip(filepaths, output_filepaths):
    if input_filepath.is_dir():
        output_filepath.mkdir()
    else:
        shutil.copy(input_filepath, output_filepath)