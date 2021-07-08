# Example code, write your program here
import random
import string
random_letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(100))
random_numbers = [random.randint(1, 20) for _ in range(100)]
dic = dict((key, value) for key, value in zip(random_letters, random_numbers))
for key in dic.keys():
    start = random.randint(1, 90)
    dic[key] = random_numbers[start:start+random.randint(1,9)]

sorted_dic = sorted(dic)
for key in sorted_dic:
    print(key, ' '.join([str(x) for x in sorted(dic[key])]))





