# Example code, write your program here
import string
import random

rand_numbers = []
dict = {}
letter = string.ascii_lowercase
rand_letters = ''.join(random.choice(letter) for i in range(100))
print(rand_letters)

for i in range(100):
    rand_numbers.append(random.randint(1,20))
print(rand_numbers)

for i in range(100):
    dict.setdefault(rand_letters[i], [])
    dict[rand_letters[i]].append(rand_numbers[i])

dict = sorted(dict.items())

for i in dict:
    print(i[0], end=" ")
    i[1].sort()
    for j in i[1]:
        print(j, end=" ")
    print()


