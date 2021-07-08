# Example code, write your program here
# ---- BEGIN AUTO-GENERATED CODE ----
# ---- ubzkov3ptgn8yjgu5z3rmbeu4 ----
# query: copy a file
# to remove these comments and send feedback press alt-G
import shutil, errno, os
import pandas as pd
# ---- END AUTO-GENERATED CODE ----
for root, dirs, files in os.walk('data'):  # replace the . with your starting directory
    dest_root = root.replace('data', 'output')
    print('dest_root')
    for i in range(len(dest_root) - 10):
        date = ''
        try:
            date = pd.Timestamp(dest_root[i:i + 10]).strftime('%m-%d-%Y')
            dest_root = dest_root[:i] + date + dest_root[i + 10:]
        except: pass
        if date != '': break

    for file in files:
        path_file = os.path.join(root,file)
        dest = file
        for i in range(len(dest) - 10):
            date = ''
            try :
                date = pd.Timestamp(dest[i:i+10]).strftime('%m-%d-%Y')
                dest = dest[:i] + date + dest[i+10:]
            except: pass
            if date != '': break
        if not os.path.exists(dest_root): os.makedirs(dest_root)
        shutil.copy2(path_file, dest_root) # change you destination dir
        path = os.path.join(dest_root, file)
        os.rename(path, os.path.join(dest_root, dest))
