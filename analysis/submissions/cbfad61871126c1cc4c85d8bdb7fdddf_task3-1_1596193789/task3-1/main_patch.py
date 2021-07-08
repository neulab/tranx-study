import os
import re
import shutil
import errno

input_dir = 'data'
output_dir = 'output'
for root, dirs, files in os.walk(input_dir):
    for filename in files:
        filename_out = filename
        match = re.search(r'\d\d\d\d-\d\d-\d\d', filename)
        if match:
            date_in = match.group(0)
            date_out = date_in[8:10:] + "-" + date_in[5:7:] + "-" + date_in[0:4:]
            filename_out = filename.replace(date_in, date_out)

        if not os.path.exists(root.replace(input_dir, output_dir)):
            try:
                os.makedirs(root.replace(input_dir, output_dir))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        shutil.copy(os.path.join(root, filename), os.path.join(root.replace(input_dir, output_dir), filename_out))

for root, dirs, files in os.walk(output_dir):
    for dirname in dirs:
        dirname_out = dirname
        match = re.search(r'\d\d\d\d-\d\d-\d\d', dirname)
        if match:
            date_in = match.group(0)
            date_out = date_in[8:10:] + "-" + date_in[5:7:] + "-" + date_in[0:4:]
            dirname_out = dirname.replace(date_in, date_out)
        os.rename(os.path.join(root, dirname), os.path.join(root, dirname_out))
