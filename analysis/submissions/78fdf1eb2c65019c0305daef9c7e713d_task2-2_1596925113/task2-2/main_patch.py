# Example code, write your program here
import os
from shutil import copyfile


def Formatter():
    # Iterate over the input files
    for file in os.listdir('./data/'):
        if file.endswith(".txt"):   # Check if the file is a ".txt" file
            output_file = open("./output/" + file, encoding='utf-8', mode='w+')
            with open("./data/" + file, encoding='ISO-8859-15', mode="r") as current_file:
                # Remove white spaces at the beginning
                for line in current_file:
                    cleanedLine = line.lstrip()
                    if len(cleanedLine):
                        lines = [cleanedLine+ '\n']
                        break
                for line in current_file:
                    if len(line):
                        lines = lines + [line]
                output_file.seek(0)
                # Remove white spaces at the end
                for line in range(len(lines)-1,0,-1):
                    if len(lines[line].strip())<1:
                        continue
                    else:
                        break
                for l in range(0,line):
                    output_file.write(lines[l])
                # Write the output file
                output_file.write(lines[line].rstrip())
        else:
            copyfile("./data/" + file, "./output/" + file)

    return

if __name__ == '__main__':
    Formatter()