# Example code, write your program here
import json
import os

tfs = os.listdir("./data/filelist")
tfs = sorted(tfs)

with open("./output/filelist", "w+") as fout:
    for fname in tfs:
        with open(os.path.join("data/filelist/", fname), "r") as fin:
            d = fin.read()
            fout.write(d)

all_d = []
for i in range(2020, 2023):
    d = json.load(open(f"data/roster/{i}.json", "r"))
    all_d += d
for idx, dd in enumerate(all_d):
    dd["id"] = idx + 1

json.dump(all_d, open("./output/roster.json", "w+"), indent=4)