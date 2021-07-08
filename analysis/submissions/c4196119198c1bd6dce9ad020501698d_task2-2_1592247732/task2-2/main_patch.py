# Example code, write your program here

import os
import shutil

files = os.listdir("./data")
for filename in files:
    src_filepath = os.path.join("./data", filename)
    tgt_filepath = os.path.join("./output", filename)
    if not filename.endswith(".txt"):
        shutil.copy2(src_filepath, tgt_filepath)
    else:
        try:
            with open(src_filepath, "r") as f:
                lines = f.readlines()
        except:
            with open(src_filepath, "r", encoding="ISO-8859-15") as f:
                lines = f.readlines()

        full_txt = "".join(lines)
        full_txt = full_txt.strip()
        new_lines = full_txt.split("\n")
        new_full_txt = ""
        for line in new_lines:
            line = line.rstrip()
            new_full_txt += line + "\n"
        new_full_txt = new_full_txt.rstrip()

        with open(tgt_filepath, "w") as f:
            f.write(new_full_txt)


