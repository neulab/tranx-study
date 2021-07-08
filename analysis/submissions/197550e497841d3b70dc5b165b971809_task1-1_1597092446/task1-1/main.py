# Example code, write your program here
import random
import string

dig=[]
def randStr(chars = string.ascii_lowercase, N=100):
    return ''.join(random.choice(chars) for _ in range(N))
str=randStr()
for i in range(100) :
    dig.append(random.randint(1,20))
print(dig)
dic = {}
newDic={}
for i in range(100) :
    dic.setdefault(str[i],[])
    dic[str[i]].append(dig[i])

print(dic)
dicItems = dic.items()
dicSorted = sorted(dicItems)
print(dicSorted)

for a in dicSorted :
 print(a[0], end=" ")
 a[1].sort()
 for n in a[1] :
     print(n,end=" ")
 print()