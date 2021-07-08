# Example code, write your program here
import csv
import pandas as pd
#reader = csv.reader(open('data.csv', 'rb'))
with open("data.csv", 'r') as reader,open("output.csv", 'w') as outFile:
    out = csv.writer(outFile,delimiter=',',quotechar='"')
    for row in reader:
        col = row.split(',')
        if len(col) >=6:
            outFile.write(col[1].strip()+","+col[2].strip()+","+col[3].strip()+","+col[4].strip()+","+"\n")
    outFile.close()
    reader.close()

