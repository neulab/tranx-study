# Example code, write your program here
import random
import string

def Random():
    # Creating 100 random characters
    # Creating 100 random numbers from 1 to 20
    letters = [random.choice(string.ascii_lowercase)]
    numbers = str(random.randint(1,20))
    for i in range(99):
        letters = letters + [random.choice(string.ascii_lowercase)]
        numbers = numbers + str(random.randint(1,20))
    # Creating a dictionary from the characters and numbers
    result = {}
    for i in range(100):
        if letters[i] in result:
            result[letters[i]] += numbers[i]
        else:
            result[letters[i]] = numbers[i]
    # Printing the dictionary in a sorted order
    result_keys = sorted(result.keys())
    for i in range(len(result)):
        print(result_keys[i], end = ' ')
        for j in sorted(result.get(result_keys[i])):
            print(j, end = ' ')
        print()

    return

if __name__ == '__main__':
    Random()