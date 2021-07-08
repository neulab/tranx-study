# Example code, write your program here
import os
import codecs
f = open("data/aaa.txt")
data = f.read().strip().rstrip()
newf = codecs.open("output/aaa.txt", "x", "utf-8")
newf.write(data)
f = open("data/bbb.txt")
data = f.read().strip().rstrip()
newf = codecs.open("output/bbb.txt", "x", "utf-8")
newf.write(data)
f = open("data/aaa.txt")
data = f.read().strip().rstrip()
newf = codecs.open("output/bbb.txt", "x", "utf-8")
newf.write(data)




