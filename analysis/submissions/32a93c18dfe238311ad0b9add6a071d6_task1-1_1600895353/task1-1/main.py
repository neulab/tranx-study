# Example code, write your program here
import random
import string
mydict = {

}
for i in range(100):
    rand_letter = random.choice(string.ascii_lowercase)
    rand_num = random.randint(1,20)
    if not mydict.__contains__(rand_letter):
        mydict[rand_letter] = []
    mydict[rand_letter].append(rand_num)
sort = sorted(mydict)
values = []
for key in sort:
    print(key, str(mydict[key])[1:-1])
