# Example code, write your program here

import os


def p(fi, fo):
    with open(fi, encoding='ISO-8859-15') as f:
        lines = f.readlines()
        with open(fo, 'w', encoding='utf8') as g:
            g.flush()
            for line in lines:
                l = line.replace('\n', '').strip()
                if len(l):
                    g.write('{l}{sep}'.format(l=l, sep='\n'))


for file in os.listdir('data'):
    ff = file.split('.')
    if 'txt' == ff[1]:
        p('data/' + file, 'output/' + file)
