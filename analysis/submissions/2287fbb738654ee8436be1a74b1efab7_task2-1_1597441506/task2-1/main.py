# Example code, write your program here

# ---- BEGIN AUTO-GENERATED CODE ----

# ---- BEGIN AUTO-GENERATED CODE ----
# ---- wr7o9083179opourpn5xuhhye ----


# ---- BEGIN AUTO-GENERATED CODE ----
# ---- amg13d9qckp6p3xg6y7o0fn6d ----
# query: remove first column from csv file
# to remove these comments and send feedback press alt-G
import csv
import os
from collections import defaultdict

input_file = 'data.csv'
os.mkdir('/output')
output_file = '/output/output.csv'
cols_to_remove = [0, 5]

cols_to_remove = sorted(cols_to_remove, reverse=True)
row_count = 0

with open(input_file, "r") as f:
    reader = csv.reader(f) # read rows into a dictionary format
    with open(output_file, "w", newline='') as result:
        writer = csv.writer(result)
        for row in reader: # read a row as {column1: value1, column2: value2,...}
            row_count += 1
            print('\r{0}'.format(row_count), end='')
            for col_index in cols_to_remove:
                del row[col_index]
            writer.writerow(row)



