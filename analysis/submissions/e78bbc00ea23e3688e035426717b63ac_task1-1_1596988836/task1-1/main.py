# Example code, write your program here
import random
import string

#generate list of random letters
letters = []
for val in range(0,100):
    char = random.choice(string.ascii_letters.lower())
    letters.append(char)

#generate list of random numbers
numbers = []
for num in range(0,100):
    val = random.randint(1,20)
    numbers.append(val)

#make dictionary from the 2 lists
dictionary = {}
i = 0
for char in letters:
    #Character not in dictionary so value can be stored
    if char not in dictionary:
        entry = {char: numbers[i]}
        dictionary.update(entry)
    else:
        #Only one value is stored for character, this stores a second one
        if isinstance(dictionary[char], int) == True:
            dict_vals = [dictionary[char], numbers[i]]
            dictionary[char] = dict_vals
        #More than one value is stored for character, all previous values are pulled in a for loop and stored with the latest one
        else:
            dict_vals = []
            for num in dictionary[char]:
                dict_vals.append(num)
            dict_vals.append(numbers[i])
            dictionary[char] = dict_vals


    i += 1

#print required output
sortedkey=sorted(dictionary.keys(), key=lambda x:x.lower())
for letter in sortedkey:
    values = dictionary[letter]
    #Check if the value is an integer or a list, only lists need sorting
    if isinstance(values, int) == False:
        values.sort()
    print(letter + ': ' + str(values))










