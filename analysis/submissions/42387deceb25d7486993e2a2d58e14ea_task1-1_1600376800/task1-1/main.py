# Example code, write your program here

import random
import collections
characters = []
numbers = []
for i in range(100):
    j = random.randint(0, 25)
    characters.append(chr(ord('a') + j))

for i in range(100):
    j = random.randint(1, 20)
    numbers.append(j)
pairs = list(zip(characters, numbers))
dic = collections.defaultdict(list)
for c, n in pairs:
    dic[c].append(str(n))

for k in sorted(dic.keys()):
    print(k, ' '.join(sorted(dic[k])))
