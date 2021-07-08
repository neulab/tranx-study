# Example code, write your program here

# Import OS
import os

# Import io
import io

# Import copy
import shutil

# Path definition
path = 'data'

# List of filenames
lst_fileNames = os.listdir(path)

# Loop over files
for file in lst_fileNames:

    # Check the extension - Text file
    if file.endswith('.txt'):

        # Open file
        fo = io.open(path+'/'+file, mode='r', encoding="ISO-8859-15")

        # Read content
        content = fo.read()

        # Remove heading of the string
        content = content.strip()

        # Write to file
        fw = io.open('output/'+file, mode='w', encoding="utf-8")

        # Write content
        fw.write(content)

    else:

        # Copy file
        shutil.copy(path+'/'+file, 'output/'+file)
