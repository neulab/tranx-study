# Example code, write your program here
import csv
fname_in = '/vagrant/task2-1/data.csv'
fname_out = '/vagrant/task2-1/output.csv'

with open(fname_in, 'r') as fin , open(fname_out, 'w') as fout :
    reader = csv.reader(fin ,delimiter=',')

    for row in reader:
        for i in range(1,5):
            if i == 4 :
                fout.write(row[i])
            else:
                fout.write(row[i])
                fout.write(",")
        fout.write("\n")


