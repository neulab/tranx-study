# Example code, write your program here
import random

ch2nb = {}
for idx in range(100):
    ch = chr(random.randrange(26) + ord('a'))
    if ch not in ch2nb:
        ch2nb[ch] = []
    nb = random.randrange(20) + 1
    ch2nb[ch].append(nb)

for idx in range(26):
    ch = chr(idx + ord('a'))
    if ch in ch2nb:
        nblist = [str(x) for x in sorted(ch2nb[ch])]
        st = ch + ' ' + ' '.join(nblist)
        print(st)