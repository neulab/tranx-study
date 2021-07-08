# Example code, write your program here
import random

d = {}
for _ in range(100):
    s = random.choice([x for x in 'abcdefghijklmnopqrstuvwxyz'])
    if s not in d:
        d[s] = []
    i = random.randint(1, 100)
    d[s].append(i)

for c in sorted(d.keys()):
    print(c, ' '.join([str(x) for x in sorted(d[c])]))