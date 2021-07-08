# Example code, write your program here
import string

import numpy as np
import random

letters=string.ascii_lowercase
chars=' '.join(random.choice(letters) for _ in range(100))
#print(chars[0])
from random import randrange
print(randrange(20))
randnumbers = []
for i in range (100):
    r= randrange(1, 6)
    smalllist=[]
    for x in range(r):
        smalllist.append(randrange(20))
        smalllist.sort()
    randnumbers.append(smalllist)
#print(randnumbers)
chars=chars.split()
#chars=chars.sort()
randnumbers=np.array(randnumbers)
d={}
chars=sorted(chars)
for i in range (100):
    d.update({chars[i]:randnumbers[i]})

print(d)