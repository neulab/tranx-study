# Example code, write your program here
import bisect
from collections import defaultdict
import random
import string


az_chars = string.ascii_lowercase
choice_numbers = list(range(1, 20+1))

def pick_with_replacement(seq, count):
    result_seq = []
    for _ in range(count):
        result_seq.append(random.choice(seq))
    return result_seq

hundred_characters = pick_with_replacement(az_chars, 100)
hundred_numbers = pick_with_replacement(choice_numbers, 100)

character_num_pairs = tuple(zip(hundred_characters, hundred_numbers))
character_num_map = defaultdict(list)
for character, num in character_num_pairs:
    character_num_map[character].append(num)

for key in sorted(character_num_map):
    sorted_num_string = map(str, sorted(character_num_map[key]))
    print(key, ' '.join(sorted_num_string))
