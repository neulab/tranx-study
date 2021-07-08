# Example code, write your program here

aaa=open('data/aaa.txt','r')
aaa=aaa.read().strip()
aaa=aaa.splitlines()
aaa="\n".join(filter(None,aaa))
aaa.encode('utf8')
textfile=open("output/aaa.txt",'w')
textfile.write(aaa)


import string
bbb=open('data/bbb.txt','r',encoding='latin-1')

bbb=bbb.read().rstrip()
bbb=bbb.splitlines()
bbb="\n".join(filter(None,bbb))
bbb=bbb.strip(string.whitespace)
bbb=bbb.strip()
textfile=open("output/ccc.txt",'w',encoding='utf8')
textfile.write(bbb)

ccc=open('data/ccc.txt','r',encoding='latin-1')
ccc=ccc.read().strip()
ccc=ccc.splitlines()
ccc="\n".join(filter(None,ccc))
textfile=open("output/ccc.txt",'w',encoding='utf8')
textfile.write(ccc)
