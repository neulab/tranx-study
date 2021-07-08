# Example code, write your program here
import pandas as pd
import os
df = pd.read_csv('data.csv')
headers = df.columns.values
df = df.drop([headers[0], headers[-1]], axis = 1)
if not os.path.exists('output'):
    os.makedirs('output')
df.to_csv('./output/output.csv', index = None)

