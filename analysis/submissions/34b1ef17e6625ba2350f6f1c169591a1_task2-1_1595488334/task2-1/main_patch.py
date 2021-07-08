# Example code, write your program here
import pandas as pd
import os

os.mkdir("output")
df = pd.read_csv('data.csv')
# If you know the name of the column skip this
first_col = df.columns[0]
last_col = df.columns[-1]
# Delete first
df = df.drop([first_col, last_col], axis=1)
df.to_csv('output/output.csv', index=False)