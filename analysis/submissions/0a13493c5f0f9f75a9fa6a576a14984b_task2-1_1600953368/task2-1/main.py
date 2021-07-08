import csv
import shutil
with open("data.csv","r") as source:
    rdr= csv.reader(source)
    with open("output.csv","w") as out:
        wtr= csv.writer(out)
        for c in rdr:
            del c[0],c[-1]
            wtr.writerow(c)

    f=open("output.csv","r")
    rdr2= csv.reader(f)
    for r in rdr2:
        print(r)
f.close()
new_path = shutil.move('output.csv','output')
print(new_path)