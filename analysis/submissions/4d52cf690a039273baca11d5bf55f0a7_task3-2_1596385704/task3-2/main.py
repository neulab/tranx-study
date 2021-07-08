# Example code, write your program here
import json
import os
from pathlib import Path
from operator import attrgetter


def order_files(directory):
    sorted_entries = sorted(os.scandir(directory), key=attrgetter("name"))
    return [entry.path for entry in sorted_entries]

def concatenate_textfiles(files, output_filepath):
    with open(output_filepath, 'w') as fh_out:
        for in_file in files:
            with open(in_file) as fh_in:
                fh_out.write(fh_in.read())


textfile_sourcedir = "filelist"
ordered_textfiles = order_files(f"data/{textfile_sourcedir}")
concatenate_textfiles(ordered_textfiles, f"output/{textfile_sourcedir}.txt")

json_sourcedir = "roster"
ordered_json_filepaths = order_files(f"data/{json_sourcedir}")

json_list = []
for file_ in ordered_json_filepaths:
    with open(file_) as fh:
        list_ = json.load(fh)
    json_list.extend(list_)

for index, item_dict in enumerate(json_list):
    # Id starts from 1
    item_dict["id"] = index+1


with open(f"output/{json_sourcedir}.json", 'w') as fh:
    json.dump(json_list, fh)