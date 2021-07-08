# Example code, write your program here
import os

csvFile = open('data.csv', 'r')
if not os.path.exists('output/'):
    os.mkdir('output/')
outFile = open('output/output.csv', 'w')

for line in csvFile.readlines():
    cells = line.split(',')
    outFile.write(','.join(cells[1:-1]) + '\n')

outFile.flush()
outFile.close()
