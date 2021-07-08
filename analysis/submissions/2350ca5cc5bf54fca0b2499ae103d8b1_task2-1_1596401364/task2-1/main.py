# Example code, write your program here
import os
os.mkdir('output')
with open("data.csv") as file, open("output/output.csv", 'w+') as output:
    for line in file.readlines():
        output.write(','.join(line.split(",")[1:-1])+'\n')