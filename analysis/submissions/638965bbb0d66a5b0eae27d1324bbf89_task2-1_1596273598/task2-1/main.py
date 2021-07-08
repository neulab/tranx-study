import os
import pandas as pd

df = pd.read_csv("data.csv", sep=',', header=None)

no_columns = len(df.columns)

output_f = df[range(1, no_columns-1)]

if not os.path.exists("output"):
    os.makedirs("output")

output_f.to_csv('output/output.csv', sep=',', header=None, index=False)



