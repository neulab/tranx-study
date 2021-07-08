# Example code, write your program here

# Import library
import random

# Import string
import string

# Import collection
import collections

# List of chars
chars = string.ascii_lowercase

# List initialization
lst_numbers = []
lst_chars = []

# List of 100 random numbers until 20 inclusively
for i in range(0, 100):

    # List of random numbers between 1 and 20 inclusively
    lst_numbers.append(random.randint(1, 20))

    # List of random char between a and z inclusively
    lst_chars.append(random.choice(chars))

# Define a default dictionary
dictionary = collections.defaultdict(set)

# Loop over dictionary
for char, number in zip(lst_chars, lst_numbers):

    # Add duplicate entity
    dictionary[char].add(number)

# Ordered dictionary
dictionary = collections.OrderedDict(sorted(dictionary.items()))

# Print dictionary
for key in dictionary:

    # Get char
    output = key + ' '

    # Get list of numbers
    output += ' '.join(str(e) for e in sorted(dictionary[key]))

    # Print output
    print(output)