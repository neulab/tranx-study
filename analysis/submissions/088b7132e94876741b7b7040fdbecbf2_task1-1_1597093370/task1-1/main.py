import string
import random
numbers = []
Ischar= []
dict = {}
temp = string.ascii_lowercase
for i in range(100):
    Ischar.append(random.choice(temp))
    numbers.append(random.randint(1,20))
for i in range(100):
    dict.setdefault(Ischar[i],[])
    dict[Ischar[i]].append(numbers[i])

sorting = sorted(dict.items())
for i in sorting:
    print(i[0],end=" ")
    i[1].sort()
    for j in i[1]:
        print(j,end=" ")
    print()
