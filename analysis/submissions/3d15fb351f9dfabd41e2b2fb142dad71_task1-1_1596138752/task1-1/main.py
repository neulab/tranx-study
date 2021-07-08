# Example code, write your program here
import random
import string
def task1():
    dic={}
    n=100
    i=1
    st="abcdegfhijklmnopqrstuvwxyz"
    while(i<=n):
        key=dic.keys()
        char=random.choice(st)
        x=random.randint(1,20)
        if char in key:
            dic[char].append(x)
        else:
            dic[char]=[x]
        i=i+1
    key=dic.keys()
    key=sorted(key)
    for i in key:
        lst=sorted(dic[i])
        print(i,' '.join([str(item) for item in dic[i]]))
task1()

