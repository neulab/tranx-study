# Example code, write your program here
import csv
import os
if not os.path.exists("output"):
    os.mkdir("output")
with open("data.csv","r") as data:
    rdr=csv.reader(data)
    with open("output/output.csv","w") as op:
        wtr=csv.writer(op)
        for r in rdr:
            wtr.writerow( (r[1],r[2],r[3],r[4]) )
