# Example code, write your program here
import csv

import pandas as pd
df = pd.read_csv('data.csv', sep=',')
df1 = df.iloc[:, 1:-1] # Remember that Python does not slice inclusive of the ending index.

df1.to_csv("./example_output/output.csv", index=False)



