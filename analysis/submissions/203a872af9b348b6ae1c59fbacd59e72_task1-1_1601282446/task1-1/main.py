# Example code, write your program here
import string
import random

letters = []
integers = []

for i in range(100):

    letters.append(''.join(random.choices(string.ascii_lowercase, k=1)))
    integers.append(random.randint(1,20))

dic = {}
for i in range(100):
    letter = letters[i]
    num = integers[i]

    if letter in dic:
        dic[letter].append(num)
    else:
        dic[letter] = [num]

for key in sorted(dic.keys()):
    print(key, ' '.join(map(str, sorted(dic[key]))))

