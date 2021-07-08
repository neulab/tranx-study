# Example code, write your program here

from string import ascii_lowercase
from random import choice
from collections import defaultdict

mapping = defaultdict(list)

alphabets = [choice(ascii_lowercase) for _ in range(100)]
nums = [choice(range(1, 21)) for _ in range(100)]

for _alphabet, _num in zip(alphabets, nums):
    mapping[_alphabet].append(_num)

for key, value in mapping.items():
    print(key, *value, sep=' ')
