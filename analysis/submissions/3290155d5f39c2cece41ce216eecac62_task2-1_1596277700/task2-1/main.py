# Example code, write your program here
import csv
import os
try:
    os.makedirs("output")
except FileExistsError:
    # directory already exists
    pass

with open('output/output.csv','w') as out:
    with open("data.csv", "r") as f:
        reader = csv.reader(f, delimiter="\t")
        writer = csv.writer(out, delimiter=',')
        for i, line in enumerate(reader):
            writer.writerow(line[0].split(',')[1:-1])
