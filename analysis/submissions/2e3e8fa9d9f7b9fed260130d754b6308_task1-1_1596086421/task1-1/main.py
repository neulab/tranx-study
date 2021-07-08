# Example code, write your program here
import random
value={}
for i in range(100):
    keys=random.randint(0,25)
    values=random.randint(1,20)
    if keys not in value:
        value[keys]=[]
    value[keys].append(values)
keys=list(value.keys())
keys.sort()
for i in keys:
    values=value[i]
    values.sort()
    print(chr(97+i),end=' ')
    for k in values:
        print(k,end=' ')
    print()

