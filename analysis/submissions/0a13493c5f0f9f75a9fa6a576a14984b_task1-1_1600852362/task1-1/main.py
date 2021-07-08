# Example code, write your program here
import string
import random
from _collections import OrderedDict
d = dict()
d1 = dict()
d2 = {}
key = ''
value = ''
number = 0
number_of_ints = 0
number_of_chars=[]
def get_random_char(length):
    letters = string.ascii_lowercase
    res = random.sample(letters,length)
    if res in number_of_chars:
        get_random_char(1)
    else:
        number_of_chars.append(res)
    return res
def get_random_integer():
    for j in range(1):
        val = random.randint(1,20)
    return str(val)
def number_of_integers():
    for i in range(1):
        number = random.randint(1,5)
    return number
for x in range(1,27):
    number_of_chars.clear()
    key = get_random_char(1)
    number_of_ints = number_of_integers()
    value=''
    for l in range(0,number_of_ints):
        value += ' ' +get_random_integer()
    a = value.split()
    b = sorted(a, key=int)
    value =''
    for m in b:
        value += (m +' ')
    d.update({tuple(key):value})

    for key,value in d.items():
        d1[key[0]]= d[key]

    for key,value in d1.items():
        if key not in d2.keys():
            d2[key] = value

    sorted_d2 =OrderedDict(sorted(d2.items()))
for key,value in sorted_d2.items():
    print("{} {}".format(key,value))
