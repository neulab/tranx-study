# Example code, write your program here
import random

nums = []
for i in range(100):
    nums.append(random.randint(1, 20))

chars = []
for i in range(100):
    chars.append(chr(random.randint(97, 122)))


pairs = list(zip(chars, nums))
d = {}
for c,n in pairs:
    if c not in d:
        d[c] = [n]
    else:
        l = d[c]
        l.append(n)
        d[c] = l

#sorted_d = OrderedDict(sorted(OrderedDict(sorted(d.items(), key=lambda x: x[0])).items(), key=lambda x: x[1]))
sorted_d = dict(sorted(d.items(), key=lambda x: x[0]))

for k, v in sorted_d.items():
    print(k, str(sorted(v))[1:-1].replace(',', ' '))