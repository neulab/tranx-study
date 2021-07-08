# Example code, write your program here
from random import seed
import random
import string

ints = []
chars = []
sDict = dict()
seed(1)
for i in range(100):
    ints.append(int(random.random()*100))
    chars.append(random.choice(string.ascii_letters.lower()))
for i in range(100):
    if chars[i] in sDict:
        sDict[chars[i]].append(ints[i])
    else:
        l = []
        l.append(ints[i])
        sDict[chars[i]] = l

for key in sorted(sDict):
    string = ''
    for i in sDict[key]:
        string += str(i) + ' '
    print(key, string)