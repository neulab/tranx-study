import os
from shutil import copy


def normalize(content):
    # trim leading and trailing whitespaces and normalize newlines
    return str.lstrip(str.rstrip(content)).replace('\r\n', '\n').replace('\r', '\n')


for root, dirs, files in os.walk("data"):
    for file in files:
        if file.endswith(".txt"):
            try:
                # converting format
                file_content = normalize(open(os.path.join(root, file), 'r', encoding="ISO-8859-15").read())
                open(os.path.join("output/", file), 'w', encoding="UTF-8").write(file_content)
            except:
                file_content = normalize(open(os.path.join(root, file), 'r').read())
                open(os.path.join("output/", file), 'w').write(file_content)
        else:
            copy(os.path.join(root, file), "output")