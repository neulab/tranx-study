# Example code, write your program here
import random
import string
from collections import OrderedDict
letters = string.ascii_lowercase
rl = [random.choice(letters) for _ in range(100)]
rl = sorted(rl)

rn = [random.choice(range(1, 21)) for _ in range(100)]
d = OrderedDict()

for l, n in zip(rl, rn):
    if l not in d:
        d[l] = [n]
    else:
        d[l].append(n)

for k, v in d.items():
    print(k, ' '.join([str(x) for x in sorted(v)]))
