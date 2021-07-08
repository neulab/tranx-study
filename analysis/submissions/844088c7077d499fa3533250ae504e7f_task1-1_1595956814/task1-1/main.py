import random
import string

char_num = 100
dig_num = 100
chars = random.choices(string.ascii_lowercase, k=char_num)
digs = random.choices(list(range(1,21)), k=dig_num)

res = {}

for c, d in zip(chars, digs):
    if c not in res:
        res[c] = [d]
    else:
        res[c].append(d)

for c in sorted(res.keys()):
    print(c, ' '.join(map(str, sorted(res[c]))))
