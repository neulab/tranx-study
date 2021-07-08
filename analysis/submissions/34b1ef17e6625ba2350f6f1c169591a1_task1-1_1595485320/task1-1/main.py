# Example code, write your program here
import string
import random
from collections import defaultdict

characters = []
digits = []
for i in range(100):
    characters.append(random.choice(string.ascii_lowercase))
    digits.append(random.randint(1, 20))
dic = {}

dic = defaultdict(list)
for i in range(100):
    dic[characters[i]].append(digits[i])

keySorted = sorted(list(dic.keys()))

for key in keySorted:
    print(key, *dic[key], sep=' ')

