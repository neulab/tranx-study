import os
import shutil
input_dir = "data/"
output_dir = "output/"
for root, dirs, files in os.walk(input_dir):
    for filename in files:
        if filename[-3::] == "txt":
            with open(os.path.join(input_dir, filename), "r", encoding="ISO-8859-15") as in_file, open(os.path.join(output_dir, filename), "w+", encoding="UTF-8") as out_file:
                lines_in = in_file.readlines()
                lines_out = []
                for line in lines_in:
                    if line.strip() != "":
                        lines_out.append(line.strip())
                out_file.write('\n'.join(lines_out) + '\n')
        else:
            shutil.copy(os.path.join(input_dir, filename), os.path.join(output_dir, filename))

