# Example code, write your program here
import csv
import os

path = os.path.join("/vagrant/task2-1", "output")
check_directory = os.path.isdir(path)
if not check_directory:
    os.mkdir(path)
filecsv = open(path+'/output.csv', 'w+')

with open('data.csv')as csvfile:
    read = csv.reader(csvfile, delimiter=',')
    for i in read:
        for j in range(1, 5):
            if j == 4:
                filecsv.write(i[j])
            else:
                filecsv.write(i[j]+',')
        filecsv.write('\n')

