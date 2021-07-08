import random

output = {}

# generate random chars and ints and add them to a dictionary
for i in range(100):
    character = (chr(random.randint(97, 122)))
    integer = random.randint(1, 20)
    if character in output:
        output[character].append(integer)
    else:
        output[character] = [integer]

# sort dictionary
for key in output:
    output[key] = sorted(output[key])
letters_sorted = sorted(output.items())
for (key,list) in letters_sorted:
    pair = str(key)
    for num in list:
        pair = pair + " " + str(num)
    print(pair)

