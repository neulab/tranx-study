# Example code, write your program here
import random
import string
import pprint

characters_list=[]
int_list=[]
for i in range(100):
    characters_list.append(random.choice(string.ascii_lowercase))
    int_list.append(random.randint(1, 21))
#print(characters_list)
#print(int_list)

dictionary = dict(zip(characters_list, int_list))
pprint.pprint(dictionary)




