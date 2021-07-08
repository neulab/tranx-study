# Example code, write your program here
import random
print("starting")
dictionary = dict()
count = 0
while count != 100:
    count += 1
    letter = random.choice('abcdefghijklmnopqrstuvwxyz')
    digit = random.randint(1, 20)
    if letter not in dictionary:
        dictionary[letter] = [digit]
        continue
    dictionary[letter].append(digit)

for key in sorted(dictionary):
    values = sorted(dictionary[key])
    print(key, end=' ')
    for v in sorted(values)[:-1]:
        print(v, end=' ')
    print(values[len(values)-1])
