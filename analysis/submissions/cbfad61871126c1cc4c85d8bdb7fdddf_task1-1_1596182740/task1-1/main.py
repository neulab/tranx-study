from random import choice
from random import randint
from string import ascii_lowercase
n_rec = 100  # numbers of records
n_max = 20  # random upper limit

dict_res = {}
keys = [choice(ascii_lowercase) for _ in range(n_rec)]
vals = [randint(1, n_max - 1) for _ in range(n_rec)]

for i, key in enumerate(keys):
    if not dict_res.get(key):
        dict_res[key] = []
    dict_res[key].append(vals[i])

for key, values in sorted(dict_res.items()):
    print(key, end=" ")
    print(*sorted(values), sep=" ")

