# Example code, write your program here
import os
import sys
import re
import shutil
for root, folder, file in os.walk("./data"):
    print(root, folder, file)
    for fname in file:
        x = re.finditer(r'(\d\d\d\d)-(\d\d)-(\d\d)', fname)
        new_file = fname
        for xx in x:
            new_file = fname.replace(fname[xx.start(): xx.end()], f"{xx.group(2)}-{xx.group(3)}-{xx.group(1)}")
        save_dir = os.path.join(root.replace("./data", "./output"))

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        shutil.copy2(os.path.join(root, fname), os.path.join(save_dir, new_file))



