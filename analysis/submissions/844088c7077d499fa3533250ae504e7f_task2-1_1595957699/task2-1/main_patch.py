# Example code, write your program here
import csv
import os

new_lines = []
with open('data.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for i, line in enumerate(reader):
        new_lines.append(line[1:-1])

if not os.path.exists('output/'):
    os.makedirs('output/')

with open('output/output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(new_lines)
