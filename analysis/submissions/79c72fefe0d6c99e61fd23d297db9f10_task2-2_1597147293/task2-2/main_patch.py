# Example code, write your program here
import os
import chardet
import shutil

for file in os.listdir('data'):
    if file.split('.')[-1] != 'txt':
        shutil.copy2(os.path.join('data', file), os.path.join('output', file))
        continue
    else:
        writer = open(os.path.join('output', file), 'w')
        text = open(os.path.join('data', file), 'rb').read()
        encoding = (chardet.detect(text)['encoding'])
        print(file, encoding)
        string_text = open(os.path.join('data', file))
        while True:
            if encoding == 'ISO - 8859 - 15':
                l = string_text.readline().decode('iso-8859-15').encode('utf8')
                if l != '\n':
                    writer.write(l.lstrip())
                    break
            else:
                l = string_text.readline()
                if l != '\n':
                    writer.write(l.lstrip())
                    break
        if encoding == 'ISO - 8859 - 15':
            for line in string_text.readlines(string_text.tell()):
                s = line.decode('iso-8859-15').encode('utf8')
                writer.write(s)

        else:
            for line in string_text.readlines():
                writer.write(line)



