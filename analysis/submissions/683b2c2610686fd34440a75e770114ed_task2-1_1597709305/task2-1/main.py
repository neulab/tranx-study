# Example code, write your program here
import os

try:
    os.mkdir('output/')
except:
    pass

with open('data.csv') as fin, open('output/output.csv', 'w') as fout:
    for line in fin:
        data = line.strip().split(',')
        fout.write(','.join(data[1:-1])+'\n')
