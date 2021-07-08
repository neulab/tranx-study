# Example code, write your program here

import random
from collections import defaultdict

l_key = list(map(chr, range(97, 123)))

sampled_keys = random.choices(l_key, k=100)
sampled_values = random.choices(range(1, 21), k=100)

dictionary = defaultdict(list)
for k, v in zip(sampled_keys, sampled_values):
    dictionary[k].append(v)

for k, v in sorted(list(dictionary.items()), key=lambda x: x[0]):
    print(k, " ".join(list(map(str, v))))




