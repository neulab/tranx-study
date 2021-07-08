# Example code, write your program here
import os,re

def Delete():
    if not os.path.exists("./output"):
        os.mkdir("./output")
    original = open("data.csv","r")
    new = open("./output/output.csv","w")
    for lines in original:
        x = re.search(",(.+),", lines)
        new.write(x[1])
        new.write('\n')
    return

if __name__ =='__main__':
    Delete()