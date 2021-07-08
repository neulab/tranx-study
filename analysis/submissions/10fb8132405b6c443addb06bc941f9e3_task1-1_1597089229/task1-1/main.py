# Example code, write your program here
import string
import random

num = []
num_paired = []
mydict = {}
letter = string.ascii_lowercase
res = ''.join(random.choice(letter) for i in range(100))
#print(res)
for i in range(100):
    num.append(random.randint(1, 20))
#print(num)

for i in range(100):
    for j in range(100):
        if res[i] == res[j]:
            num_paired.append(num[j])
    num_paired.sort()
    mydict[res[i]] = num_paired
    num_paired = []

sorted_dict=sorted(mydict.items())
#print(sorted_dict)

for i in sorted_dict:
    print(i[0], end=" ")
    for j in i[1]:
        print(j, end=" ")
    print()






