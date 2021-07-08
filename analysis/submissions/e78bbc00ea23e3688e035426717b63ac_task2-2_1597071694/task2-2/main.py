import os.path
#Open files
files = ['aaa.txt', 'bbb.txt', 'ccc.txt']
for file in files:
  data_folder = os.path.join('data')
  file_to_open = os.path.join(data_folder, file)
  with open(file_to_open, 'r', encoding='latin-1') as fr:
    contents = fr.readlines()

  newcontents = [' ']
  #Break the lines up into words to remove whitespace and store them as the sole element in a new list
  for item in contents:
    string = (item.split(' '))
    for word in string:
      if any(c.isalpha() for c in word):
        newcontents[0] = (newcontents[0] + word + ' ')

  #Remove space at the end and then split the string into a list, with each line of text being an element in the list
  newcontents[0] = newcontents[0][0:-1]
  contentslist = newcontents[0].split('\n')

  #Open the file for writing
  data_folder = os.path.join('output')
  file_to_open = os.path.join(data_folder, file)
  with open(file_to_open, 'w') as fw:
    #Remove the space at the start of each line and store in the text file
    i = 0
    for item in contentslist:
      index = len(item)
      newitem = item[1:index]
      fw.write(newitem + '\n')
      i += 1

