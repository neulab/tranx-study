# Example code, write your program here
import glob
import os

iso8 = False
for fname in glob.glob('data/*.txt'):
    try:
        lines = open(fname).readlines()
    except:
        lines = open(fname, encoding='ISO-8859-15').readlines()
        iso8 = True
    newlines = ''.join(lines).strip().replace('\r', '\n')
    if iso8:
        open('output/' + fname.split('/')[1], 'w', encoding='UTF-8').writelines(newlines)
    else:
        open('output/' + fname.split('/')[1], 'w').writelines(newlines)