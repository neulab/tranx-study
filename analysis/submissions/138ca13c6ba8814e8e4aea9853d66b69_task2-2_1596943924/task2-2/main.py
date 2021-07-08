import re, os
# If file has extension '.txt'
file_list = os.listdir('data/')
txt_list = []
for i in file_list:
    if '.txt' in i:
        txt_list.append(i)
for filename in txt_list:
    file_in = open('data/' + filename, 'r', encoding = "ISO-8859-15")
    file_contents = file_in.read()
    file_contents = file_contents.rstrip().lstrip() # Remove heading and trailing new lines.
    file_contents = file_contents.split('\n')
    file_out = open('output/' + filename, 'w', encoding = "UTF-8")
    for i in range(len(file_contents)):
        # j = i.strip()
        if i != len(file_contents) - 1:
            file_out.write(file_contents[i]+'\n')
        else:
            file_out.write(file_contents[i])
    file_in.close()
    file_out.close()