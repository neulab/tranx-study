import shutil

files = ["aaa.txt", "bbb.txt", "ccc.txt"]

for file in files:
    f = open("./data/"+file, 'r', encoding='ISO-8859-15')
    out = open("./output/"+file, '+w', encoding='utf-8')

    fh = f.readlines()
    fh = filter(lambda x: not x.isspace(), fh)
    f
    out.writelines(fh)
    f.close()
    out.close()

shutil.copy('./data/ddd.png', './output/ddd.png')
