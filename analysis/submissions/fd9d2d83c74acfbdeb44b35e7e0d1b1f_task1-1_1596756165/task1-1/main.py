# Example code, write your program here
import random

rInts = []
rLetters = []

for i in range(100):
    rInts.append(random.randint(1, 20))
    rLetters.append(chr(random.randint(97, 122)))

mapping = dict()

for i in range(100):
    if rLetters[i] not in mapping:
        mapping[rLetters[i]] = []
    mapping[rLetters[i]].append(rInts[i])
letters = sorted(list(mapping.keys()))
for c in letters:
    print(c, end=" ")
    for i in mapping[c]:
        print(i, end=" ")
    print()
