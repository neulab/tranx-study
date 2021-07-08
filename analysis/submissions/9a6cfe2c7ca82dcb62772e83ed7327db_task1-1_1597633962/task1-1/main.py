# Example code, write your program here
import string
import random
random_dict =dict()
for i in range(100) :
    random_char = random.choice(string.ascii_lowercase)
    random_num = random.randint(1 , 20)
    random_dict.setdefault(random_char,[]).append(random_num)
for key in sorted(random_dict):
    print(key,' '.join(map(str, random_dict[key])))

