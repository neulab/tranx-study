# Example code, write your program here

import os
import csv
import math

def findItem(theList, item):
    return [(ind, theList[ind].index(item)) for ind in range(len(theList)) if item in theList[ind]]


for root, subdir, files in os.walk('output'):
    for file in files:
        os.remove(os.path.join(root, file))

with open('automobile_data.csv', newline='') as inp:
    reader = csv.reader(inp)
    data = list(reader)

comp = []#[['company', 'avg_price', 'max_price', 'min_price', 'stddev_price', 'total_count']]
count = []#[['company', 'true_count']]

for i in data:
    if i[0] != 'index':
        try:
            fN = float(i[9])
        except:
            fN = None
        if not any(i[1] in sublist[0] for sublist in comp):
            if fN is None:
                comp.append([i[1], fN, fN, fN, fN, 1])
                count.append([i[1], 0])
            else:
                comp.append([i[1], fN, fN, fN, 0.0, 1])
                count.append([i[1], 1])
        else:
            ind = findItem(comp, i[1])[0][0]
            comp[ind][5] += 1
            if fN is not None:
                count[ind][1] += 1
                if comp[ind][1] is not None:
                    comp[ind][4] = 0.0
                    comp[ind][1] += fN
                    if fN > comp[ind][2]:
                        comp[ind][2] = fN
                    if fN < comp[ind][3]:
                        comp[ind][3] = fN
                else:
                    comp[ind][1] = fN
                    comp[ind][2] = fN
                    comp[ind][3] = fN

for i in range(len(comp)):
    ind = findItem(comp, comp[i][0])[0][0]
    if count[i][1] != 0:
        comp[ind][1] = float(comp[i][1]) / float(count[i][1])

for i in data:
    if i[0] != 'index':
        ind = findItem(comp, i[1])[0][0]
        if count[ind][1] != 0 and i[9] != '':
            comp[ind][4] += ((float(i[9]) - comp[ind][1])**2)/count[ind][1]

for i in range(len(comp)):
    ind = findItem(comp, comp[i][0])[0][0]
    if comp[ind][4] is not None:
        comp[ind][4] = math.sqrt(comp[ind][4])

comp = sorted(comp, key = lambda x: x[1], reverse=True)

for i in range(len(comp)):
    ind = findItem(comp, comp[i][0])[0][0]
    comp[ind][2] = "{:.2f}".format(comp[ind][2])
    comp[ind][3] = "{:.2f}".format(comp[ind][3])
    comp[ind][5] = int(comp[ind][5])
    if comp[ind][1] is not None:
        comp[ind][1] = "{:.2f}".format(comp[ind][1])
        comp[ind][4] = "{:.2f}".format(comp[ind][4])
comp.insert(0,['company', 'avg_price', 'max_price', 'min_price', 'stddev_price', 'total_count'])
print(comp)
with open('output/price_by_company.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(comp)

###################################################

horse = []#[['horse', 'avg_price', count]]
horseC = []#[['horse', 'true_count']]

num = int(data[1][7])
minH = num - (num%20)
maxH = num - (num%20)

for i in data:
    if i[0] != 'index':
        num = int(i[7])
        if (num - (num%20)) < minH:
            if num%20 == 0:
                minH = num - 20
            else:
                minH = num - (num%20)
        if (num - (num%20)) > maxH + 20:
            maxH = num - (num%20)


for i in data:
    if i[0] != 'index':
        try:
            fN = float(i[9])
        except:
            fN = None
        num = int(i[7])
        if num%20 == 0:
            num = num - 20
        else:
            num = num - (num % 20)
        if not any(num == sublist[0] for sublist in horse):
            horse.append([num, fN, 1])
            if fN is None:
                horseC.append([num, 0])
            else:
                horseC.append([num, 1])
        else:
            ind = findItem(horse, num)[0][0]
            horse[ind][2] += 1
            if fN is not None:
                horseC[ind][1] += 1
                if horse[ind][1] is not None:
                    horse[ind][1] += fN
                else:
                    horse[ind][1] = fN

for i in range(len(horse)):
    ind = findItem(horse, horse[i][0])[0][0]
    if horseC[i][1] != 0:
        horse[ind][1] = float(horse[i][1]) / float(horseC[i][1])

for i in range(minH, maxH+20,20):
    if not any(i == sublist[0] for sublist in horse):
        horse.append([i, None, 0])

horse = sorted(horse, key = lambda x: x[0])


for i in range(len(horse)):
    ind = findItem(horse, horse[i][0])[0][0]
    horse[ind][0] = '('+str(horse[ind][0]) + ', ' + str(horse[ind][0]+20) + ']'
    try:
        horse[ind][1] = "{:.2f}".format(horse[ind][1])
    except:
        None


horse.insert(0, ['horsepower_range', 'avg_price','count'])

print(horse)

with open('output/price_by_horsepower.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(horse)

data[0].append('score')
tmp = data[0]
for i in reversed(range(len(data))):
    try:
        fN = float(data[i][9])
        fL = float(data[i][4])
        if fN <= 15000 and fL < 180:
            score = float(data[i][7]) / (float(data[i][8]) * fN)
            data[i].append("{:.7f}".format(score))
        else:
            data.pop(i)
    except:
        data.pop(i)

data = sorted(data, key = lambda x: x[10], reverse=True)
data.insert(0,tmp)

with open('output/for_john.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(data)
