# Example code, write your program here
import glob, os
import shutil
#os.chdir("data")
filenames = []
i = 0
target='output/'
for other_files in glob.glob("data/*.*"):
    filenames.append(other_files)
    if filenames[i][-3:] != 'txt':
        shutil.copy(filenames[i], target)
        # print(filenames[i][-3:])
        # print(filenames[i])
    i = i+1
for file in glob.glob("data/*.txt"):
    # print(file)
    # print(type(file))
    with open(file, 'r', encoding='ISO-8859-15') as inp, open (file.replace('data','output'), 'w+', encoding='UTF-8') as out:
        my_list=[]
        for line in inp:
            line = line.strip()
            #if line != "":
            my_list.append(line+'\n')
        a = 0
        b = len(my_list)
        # print(my_list)
        for a in range(0,len(my_list)):
            if my_list[a] != '\n':
                break
            a = a+1
        # print(a)
        for b in range(len(my_list)-1,0,-1):
            if my_list[b] != '\n':
                break
            b = b-1
        # print(b)

        my_list=my_list[a:b+1]
        my_list[-1]=my_list[-1].strip()

        # print(my_list)
        out.writelines(my_list)

