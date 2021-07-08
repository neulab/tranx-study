# Example code, write your program here
import csv
import os
directory = "output"
parent_dir = "/vagrant/task2-1"
path = os.path.join(parent_dir,directory)
os.mkdir(path)
file = "data.csv"
output_file = "/vagrant/task2-1/output/output.csv"
csv_file = open(file,'r')
with open(output_file,'w') as fh:
    Reader = csv.reader(csv_file,delimiter=',')
    for row in Reader:
        tmp_row= []
        for col_inx in range(1,5):
            tmp_row.append(row[col_inx])
        fh.write(','.join(tmp_row))
        fh.write("\n")
