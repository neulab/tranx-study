# Example code, write your program here
import random
import collections
d = collections.OrderedDict()
for i in range(100):
    c = chr(ord('a') + random.randint(0, 25))
    n = random.randint(1, 20)
    if c not in d:
        d[c] = []
    d[c].append(n)
for k,v in d.items():
    values = ' '.join(map(str,sorted(v)))
    print(k + ' ' + values)