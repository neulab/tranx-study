# Example code, write your program here

import csv
with open("data.csv","r") as source:
    rdr= csv.reader( source )
    with open("example_output/output.csv","w") as result:
        wtr= csv.writer( result )
        for r in rdr:
            wtr.writerow(tuple(r[1:-1]))
