# Example code, write your program here
import os
import subprocess
import codecs

for file in os.listdir('data'):
    start = False
    terminal_output = str(subprocess.check_output(['file', 'data/'+file]))
    if 'text' in terminal_output:
        if 'ISO-8859' in terminal_output:
            with codecs.open('data/'+file, 'r', 'iso-8859-1') as infile:
                with open('output/'+file, 'w') as outfile:
                    lines = ''.join([line for line in infile.readlines()]).strip()
                    outfile.write(lines)
        else:
            with open('data/'+file) as infile, open('output/'+file, 'w') as outfile:
                lines = ''.join([line for line in infile.readlines()]).strip()
                outfile.write(lines)
