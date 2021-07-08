import os, glob
from shutil import copyfile
input_path = "data/"
output_path = "output/"
files_names = []
for filename in glob.glob(os.path.join(input_path, '*')):
    files_names.append (filename.split("/")[-1])
for file_name in files_names :
    if ".txt" in file_name :
        file_lines = []
        lines = []
        with open(input_path+file_name, 'rb') as file:

            for s in file.readlines() :
                s= s.decode('iso-8859-1', 'ignore')
                file_lines.append (s.replace ('\n'," "))
            for l in file_lines :
                if l.isspace() == False:
                    lines.append(l.strip())
        with open(output_path+file_name, 'w') as out:
            for line in lines :
                out.write(line+'\n')
    else:
        copyfile(input_path+file_name,output_path+file_name)