# Example code, write your program her
import os
import pandas as pd
if not os.path.exists('output') : os.makedirs('output')
for fname in ['aaa', 'bbb', 'ccc']:
    # data = pd.read_csv('data/%s.txt'%(fname), encoding = 'iso-8859-15', na_filter = False)
    # print(data)
    # data.set_index(data.columns[0]).to_csv('output/%s.txt'%fname, encoding = 'utf-8')




    try :
        fin = open('data/%s.txt'%fname, 'r')
        findata = fin.readlines()
        fout = open('output/%s.txt'%fname, 'w')
        i = 0
        out = []
        flag = False
        for line in findata:
            if len(line.strip().replace(' ', '')) : flag = True
            if flag:
                out.append(line)
        _len = len(out)
        for i in range(_len):
            if len(out[_len - 1 - i].strip().replace(' ', '')) > 0: break
            else: del out[_len - 1 - i]
        for i in range(len(out)):
            try :
                fout.write(out[i].decode('iso-8859-15').encode('utf-8'))
            except: fout.write(out[i])
    except: pass
    fin.close()
    fout.close()


import matplotlib.pyplot as plt
img = plt.imread('data/ddd.png')
plt.imsave('output/ddd.png', img)