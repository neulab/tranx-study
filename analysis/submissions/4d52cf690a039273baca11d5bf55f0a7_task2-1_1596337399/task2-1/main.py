# Example code, write your program here
import os

import pandas as pd

df = pd.read_csv("data.csv")
del df[df.columns[0]]
del df[df.columns[-1]]

try:
    os.mkdir("output")
except FileExistsError:
    pass
df.to_csv("output/output.csv")