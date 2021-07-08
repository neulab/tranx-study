import pandas
import os

file = pandas.read_csv("./data.csv")
del file['id']
del file['ip_address']

if not os.path.exists('./output/'):
    os.mkdir('output')

output = open("./output/output.csv", "w+")
file.to_csv(output, index=False)

output.close()

