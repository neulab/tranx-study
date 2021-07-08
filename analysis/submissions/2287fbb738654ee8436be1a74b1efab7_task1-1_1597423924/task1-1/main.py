import string
import random
my_dict = dict()
nums = []
chars = []
sortedDict = dict()

for i in range(100):
    nums.append(random.randint(1, 20))
    chars.append(random.choice(string.ascii_lowercase))

for i in range(100):
    try:
        my_dict[chars[i]].append(nums[i])
    except:
        my_dict[chars[i]] = [nums[i]]

for i in sorted(my_dict.keys()):
    sortedDict[i] = my_dict[i]

print(sortedDict)

