# Example code, write your program here
import random
import string
# First generate 100 lower case characters between a and z.
x = []
for _ in range(100):
    x.append(random.choice(string.ascii_lowercase))
y = []
# Then generate 100 integers between 1 and 20
for _ in range(100):
    y.append(random.randint(1, 20))
# print(x)
# print(y)
# Now pair the characters with their corresponding integers in a dictionary.
combined_dic = {}
for i in range(len(x)):
    if x[i] not in combined_dic.keys():
        combined_dic[x[i]] = [y[i]]
    else:
        combined_dic[x[i]].append(y[i])
# print(combined_dic)
# Now sort the values in the dictionary
for i in combined_dic.keys():
    combined_dic[i].sort()
# print(combined_dic)
# Now print in the required output format.
sorted_key_list = list(combined_dic.keys())
sorted_key_list.sort()
for i in sorted_key_list:
    x = " ".join(str(y) for y in combined_dic[i])
    # ---- END AUTO-GENERATED CODE ----
    print(i, x)
