# Example code, write your program here
import random
import string
from collections import defaultdict


def main():
    letters = [random.choice(string.ascii_lowercase) for _ in range(100)]
    numbers = [random.randint(1, 20) for _ in range(100)]
    d = defaultdict(list)
    for c, x in zip(letters, numbers):
        d[c].append(x)
    print("\n".join(f"{c} {' '.join(map(str, xs))}" for c, xs in sorted(d.items())))


if __name__ == '__main__':
    main()
