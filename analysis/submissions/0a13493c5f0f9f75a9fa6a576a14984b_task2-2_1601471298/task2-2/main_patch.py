# Example code, write your program here
import chardet
import codecs

# aaa.txt
flag1 = 0
flag2 = 0

with open("data/aaa.txt", 'rb') as f11:
    result = chardet.detect(f11.read())

if result['encoding'] == 'ISO-8859-9':
    sourceEncoding = 'ISO-8859-9'
    targetEncoding = 'UTF-8'
    source = open('data/aaa.txt', 'rb')
    target = open('output/aaa.txt', 'wb')
    target.write(str(source.read(), sourceEncoding).encode(targetEncoding))

with open("output/aaa.txt", 'r') as f1:
    file_out = []
    lines = f1.readlines()
    for line in lines:
        if line == '\n' and flag1 == 0:
            continue
        elif flag2 == 0 and line != '\n':
            flag1 = 1
            flag2 = 1
            first_line = line.lstrip()
            print(first_line, end="")
            file_out.append(first_line)
        else:
            next_line = line
            print(next_line, end="")
            file_out.append(next_line)
f1.close()

file_out[-1] = file_out[-1].strip('\n')
file_out[-1] = file_out[-1].rstrip()

with open("output/aaa.txt", 'w') as f111:
    f111.write(''.join(file_out))

if result['encoding'] != 'ASCII':
    BLOCKSIZE = 1048576
    with codecs.open('data/aaa.txt', 'r', 'ISO-8859-15')as sourceFile:
        with codecs.open('output/aaa.txt', 'w', 'utf-8')as targetFile:
            while True:
                contents = sourceFile.read(BLOCKSIZE)
                if not contents:
                    break
                targetFile.write(contents)
# bbb.txt
flag1 = 0
flag2 = 0

with open("data/bbb.txt", 'rb') as f2222:
    result = chardet.detect(f2222.read())
f2222.close()

with codecs.open("data/bbb.txt", 'rb', encoding=result['encoding']) as f22:
    file_out_2 = []
    lines = f22.readlines()
    for line in lines:
        if line == '\n' and flag1 == 0:
            continue
        elif flag2 == 0 and line != '\n':
            flag1 = 1
            flag2 = 1
            first_line = line.lstrip()
            print(first_line, end="")
            file_out_2.append(first_line)
        else:
            next_line = line
            print(next_line, end="")
            file_out_2.append(next_line)
f22.close()
file_out_2[-1] = file_out_2[-1].strip('\n')
file_out_2[-1] = file_out_2[-1].rstrip()

with codecs.open("data/bbb.txt", 'wb', encoding='UTF-8') as f222:
    f222.write(''.join(file_out_2).replace('\\r\\n', ''))
f222.close()

if result['encoding'] != 'ASCII':
    BLOCKSIZE = 1048576
    with codecs.open('data/bbb.txt','r',result['encoding'])as sourceFile:
        with codecs.open('output/bbb.txt','w','utf-8')as targetFile:
            while True:
                contents = sourceFile.read(BLOCKSIZE)
                if not contents:
                    break
                targetFile.write(contents)


# ccc.txt
flag1 = 0
flag2 = 0

with open("data/ccc.txt", 'rb') as f3333:
    result = chardet.detect(f3333.read())
f3333.close()

with codecs.open("data/ccc.txt", 'rb', encoding=result['encoding']) as f33:
    file_out_2 = []
    lines = f33.readlines()
    for line in lines:
        if line == '\n' and flag1 == 0:
            continue
        elif flag2 == 0 and line != '\n':
            flag1 = 1
            flag2 = 1
            first_line = line.lstrip()
            print(first_line, end="")
            file_out_2.append(first_line)
        else:
            next_line = line
            print(next_line, end="")
            file_out_2.append(next_line)
f33.close()

with codecs.open("data/ccc.txt", 'wb', encoding='UTF-8') as f333:
    f333.write(''.join(file_out_2).replace('\\r\\n', ''))
f333.close()

if result['encoding'] != 'ASCII':
    BLOCKSIZE = 1048576
    with codecs.open('data/ccc.txt', 'r', 'ISO-8859-15')as sourceFile:
        with codecs.open('output/ccc.txt', 'w', 'utf-8')as targetFile:
            while True:
                contents = sourceFile.read(BLOCKSIZE)
                if not contents:
                    break
                targetFile.write(contents)