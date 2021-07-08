import random
import string

# Example code, write your program here
res=[[] for i in range(26)]
dictt = {}
for i in range(0,100):
    # print(chr(random.randint(0, 25)+ord('a')))
    letter=random.randint(0,25)
    num=random.randint(1,20)
    # print(str(num)+' '+chr(letter+ord('a')))
    res[letter].append(num)

for i in range(0,26):
    dictt[chr(i+ord('a'))]=sorted(res[i])
for i in dictt:
    print(i,*dictt[i])