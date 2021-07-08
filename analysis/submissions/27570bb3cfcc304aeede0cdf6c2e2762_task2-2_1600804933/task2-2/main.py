# Example code, write your program here
import os
import string
path = 'data1'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))

# Remove Space for unicode
for i in range(len(files)):
  if i != 0:
      with open(files[i],encoding="ISO-8859-15") as f:
        lines = f.readlines()
    # remove spaces
      f.close()
      out = open(os.path.join("try", files[i]), "w+")
  else:
      with open(files[i], 'r') as f:
          lines = f.readlines()
          # remove spaces
      f.close()
      out = open(os.path.join("output", files[i]), "w+")
  count =0
  for line in lines:
     if(len(line.strip()) == 0 ) and count ==0:
         del line
     else :
         if count == 0:
             line=line.strip()
         count =1
         out.write(line)
  out.close()

# convert to unicode
for i in range(1,len(files)):
    with open(os.path.join("try",files[i]),encoding="ISO-8859-15") as f, open( os.path.join("output" ,files[i]), "wb") as target:
        reading =f.read()
        reading = reading.encode("UTF-8","replace")
        target.write(reading)
    target.close()
    f.close()

