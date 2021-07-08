import random

keys = 'abcdefghijklmnopqrstuvwxyz'
values = [i for i in range(21)]

n = 100
dicts = {}
for i in range(n):
    char = random.choice(keys)
    val = random.choice(values)
    if char in dicts: dicts[char].append(val)
    else: dicts[char] = [val]
for c in keys:
    if c in dicts:
        print(c, end = " ")
        for i in sorted(dicts[c]): print(i, end = ' ')
        print()