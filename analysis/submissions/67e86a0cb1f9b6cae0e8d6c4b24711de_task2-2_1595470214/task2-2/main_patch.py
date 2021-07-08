import os
import shutil
import codecs
for filename in os.listdir('data'):
    in_file = os.path.join('data', filename)
    out_file = os.path.join('output', filename)

    if filename.endswith('.txt'):
        with codecs.open(in_file, encoding='ISO-8859-15') as in_f:
            with codecs.open(out_file, encoding='UTF-8', mode='w') as out_f:
                for line in in_f.readlines():
                    has_newline = len(line) > 1 and line[-1] == '\n'
                    l = line.strip()
                    if l == '':
                        continue
                    else:
                        out_f.write(l)
                        if has_newline:
                            out_f.write('\n')
    else:
        shutil.copy2(in_file, out_file)
