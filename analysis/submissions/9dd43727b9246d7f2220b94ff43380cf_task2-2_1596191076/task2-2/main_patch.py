# ---- BEGIN AUTO-GENERATED CODE ----
# ---- 9s6vn77ntdfzb408h8w000e6k ----
# query: traverse a directory
# to remove these comments and send feedback press alt-G
import os

from idna import unicode

directory = "data"
arr = os.listdir(directory)
# ---- BEGIN AUTO-GENERATED CODE ----
# ---- 4n9lw6kjdwxmswobv36w1vsw5 ----
# query: open file
# to remove these comments and send feedback press alt-G
# ---- END AUTO-GENERATED CODE ----


for x in arr:
    if x.endswith(".txt"):
        file = open((directory + '/' + x), 'rb')
        outputname =  (file.name[5:])
        outputfile = open( ('output/' + outputname) , 'w', encoding='utf-8')
        mylist = list(file)
        for i in mylist:
            i = i.decode("latin-1")
            if i.isspace() == False:
                i = i.split()
                for j in i:
                    outputfile.write(j + ' ')
                outputfile.write('\n')
        file.close()

