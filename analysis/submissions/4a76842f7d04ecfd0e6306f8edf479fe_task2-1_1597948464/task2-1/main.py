# Example code, write your program here
import csv
import os
path = "/vagrant/task2-1/data.csv"

if os.path.exists("/vagrant/task2-1/output"):
    None
else:
    os.mkdir("/vagrant/task2-1/output")

f1 = open("/vagrant/task2-1/output/output.csv", 'w')
with open(path,"r") as f:
    reader = csv.reader(f, delimiter=',')
    for i in reader:
        for j in range(1,5):
            f1.write(i[j])
            if j !=4:
                f1.write(",")
        f1.write("\n")
