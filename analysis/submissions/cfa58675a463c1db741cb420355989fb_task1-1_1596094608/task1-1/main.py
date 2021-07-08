# Example code, write your program here

import random
import string

DIGITS = [i for i in range(1,21)]
CHARS = string.ascii_lowercase

ran_ds = [random.choice(DIGITS) for _ in range(100)]
ran_cs = [random.choice(CHARS) for _ in range(100)]

result = dict()

for i in range(100):
    if ran_cs[i] not in result:
        result[ran_cs[i]] = list()
    result[ran_cs[i]].append(ran_ds[i])

for c in sorted(result.keys()):
    print('{c} {ns}'.format(c=c, ns=' '.join([str(d) for d in result[c]])))
