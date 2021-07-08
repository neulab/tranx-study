# Example code, write your program here
import os

file_encoding={"aaa": "utf-8", "bbb": "ISO-8859-15", "ccc": "ISO-8859-15"}
for fname in os.listdir("./data"):
    print(fname)
    filename, file_extension = os.path.splitext(fname)
    if file_extension == ".txt":
        encoding = file_encoding.get(filename, "utf-8")
        with open(os.path.join("./data", fname), "r", encoding=encoding) as fin, \
            open(os.path.join("./output", fname), "w+", encoding="utf-8") as fout:
            x = fin.read().strip()
            fout.write(x + "\n")
    else:
        import shutil
        shutil.copy2(os.path.join("./data", fname), os.path.join("./output", fname))

