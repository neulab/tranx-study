# Example code, write your program here
import csv
file = open ("data.csv", "r")
output  = open ("output.csv", 'w')
csv_file = csv.reader(file)
mylist = []
for i in csv_file:
    mylist.append(i)

for i in range (0, len(mylist)):
    for j in range (1, 5):
        output.write(mylist[i][j])
        if j !=4:
            output.write(",")
    output.write('\n')

