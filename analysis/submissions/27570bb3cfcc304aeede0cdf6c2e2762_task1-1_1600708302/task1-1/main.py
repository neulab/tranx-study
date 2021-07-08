# Example code, write your program here
import random
import string
a_num = []
a_char =[]
dic = {}
ascii_n =97 # a charactare
number = 100
for i in range(100):
    a_num.append(random.randint(1, 20))
    a_char.append(random.randint(97, 123))
a_num.sort()
a_char.sort()
for i in range(100):
    dic[chr(a_char[i])] = a_num[i]
print(dic)