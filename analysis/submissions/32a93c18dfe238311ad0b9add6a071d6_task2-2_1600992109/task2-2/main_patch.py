# Example code, write your program here
import os
import chardet
for file in os.listdir("data"):
    try:
        opened_file = open(f"data/{file}")
        for line in opened_file:
            continue
        opened_file = open(f"data/{file}")
    except UnicodeDecodeError:
        opened_file = open(f"data/{file}", encoding='ISO-8859-15')

    line_arr = []
    header = True
    for line in opened_file:
        line = line.rstrip()
        if line is '' and header is True:
            continue
        else:
            line_arr.append(line)
            header = False
    footer = True
    for line in reversed(line_arr):
        line = line.rstrip()
        if line is '' and footer is True:
            del line_arr[-1]
        else:
            footer = False
            continue
    f = open(f"output/{file}","w")
    line_arr[0] = line_arr[0].strip()
    if opened_file.encoding is 'ISO-8859-15':
        f.encoding = 'UTF-8'
    for line in line_arr:
        line = line.replace('\r\n', '\n')
        f.write(line)
        if line is not line_arr[-1]:
            f.write('\n')
    opened_file.close()
    print(line_arr)
