# Example code, write your program here
import os
import csv
if not os.path.exists('output'):
    os.mkdir("output")
with open("data.csv",'r') as file:
    reader=csv.reader(file)
    lines=list(reader)
with open("output/output.csv",'w') as file:
    writer=csv.writer(file)
    for i in lines:
        del i[0]
        del i[len(i)-1]
        writer.writerow(i)