# Example code, write your program here
import random
import string
letters = string.ascii_lowercase
resultc = [random.choice(letters) for i in range(100)]
resultn = [random.randrange(1, 21) for i in range(100)]
newlist = []
for i in range(100):
    newlist.append((resultc[i], resultn[i]))
newdic = {}
for i, j in newlist:
    if i not in newdic.keys():
        newdic[i] = [j]
    else:
        newdic[i].append(j)

for key in sorted(newdic):
    newstring = ""
    newstring = newstring + key + " "
    for i in sorted(newdic[key]):
        newstring = newstring + str(i) + " "
    print(newstring)


