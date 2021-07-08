import random
import string


def generate_keys(max_range):
    key = []
    for counter in range(max_range):
        key.append(random.choice(string.ascii_lowercase))
    key.sort()
    return key


def generate_values(max_range, start, end):
    val = []
    for counter in range(max_range):
        val.append(random.randint(start, end))
    return val


def create_dictionary(max_range, keys_list, values_list):
    paired_dict = {}
    value = []
    for count in range(max_range):
        if keys_list[count] in paired_dict:
            value.extend(paired_dict[keys_list[count]])
            value.append(values_list[count])
        else:
            value.append(values_list[count])
        if [] in value:
            value.remove([])
        paired_dict[keys_list[count]] = value.copy()
        value.clear()
    return paired_dict


def main():
    keys = generate_keys(100)
    values = generate_values(100, 1, 20)
    dictionary = create_dictionary(100, keys, values)

    for i in dictionary:
        print(i, *dictionary[i])


if __name__ == '__main__':
    main()
