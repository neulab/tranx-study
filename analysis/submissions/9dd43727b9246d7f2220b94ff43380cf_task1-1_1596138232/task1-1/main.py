# Example code, write your program here
import string
import random
from collections import defaultdict

dict = defaultdict(list)

def random_char():
    letter = string.ascii_lowercase
    result = ''.join(random.choice(letter))
    return result

for i in range (1, 100):
    tempkey = random_char()
    tempval = random.randint(1, 20);
    dict[tempkey].append(tempval)

print (dict)
dict2 = dict.items()
sorted_dict = sorted(dict2)
for x in range(0,len(sorted_dict)):
    sorted_dict[x][1].sort()
for x in range(0,len(sorted_dict)):
    print (sorted_dict[x][0], end= " ")
    for y in range (0, len(sorted_dict[x][1])):
        print (sorted_dict[x][1][y], end = " ")
    print()