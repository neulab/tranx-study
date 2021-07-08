# Example code, write your program here
import os
if not os.path.exists('output'):
    os.mkdir('output')
with open('data.csv') as f:
    with open('output/output.csv','w') as out:
        for line in f.readlines():
            start = line.find(',') + 1
            end = line.rfind(',')
            out.write(line[start:end])
            out.write('\n')