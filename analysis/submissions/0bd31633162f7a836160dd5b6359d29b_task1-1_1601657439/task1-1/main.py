# Example code, write your program here
from numpy import random
import string
#Generate the random list of integers
int_arr  = random.randint(20 , size=100)

import random
#Generate the random list of character (String)
char_arr = ''.join(random.choices(string.ascii_lowercase , k = 100))

my_Dict = {}
sorted_Dict ={}

for i in range(0,99):
    my_Dict[char_arr[i]] = my_Dict.get(char_arr[i],[]) + [int_arr[i]]

for key in sorted(my_Dict):
    sorted_Dict[key] = sorted(my_Dict[key])
    print(str(key) + " : " + str(sorted_Dict[key]))


