# Example code, write your program here
import pandas as pd
import os
data = pd.read_csv("data.csv")
data = data.drop(data.columns[[0, 5]], 1)
os.makedirs('output')
data.to_csv("output/output.csv", encoding='utf-8', index=False)