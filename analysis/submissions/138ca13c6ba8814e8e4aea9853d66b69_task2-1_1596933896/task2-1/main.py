# Read from a CSV file and write the output to another CSV file after removing the first and the last columns..
# Output file is in a directory that does not exist yet -- have to create that directory.
import csv
import os

input_file = open("data.csv","r")
os.mkdir('output')
out_file = open("./output/output.csv", "w")
input_reader = csv.reader(input_file)
output_writer = csv.writer(out_file)
for i in input_reader:
    output_writer.writerow(i[1:-1])
input_file.close()
out_file.close()