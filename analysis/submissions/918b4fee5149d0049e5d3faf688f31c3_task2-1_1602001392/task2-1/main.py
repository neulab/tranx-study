# Example code, write your program here
import pandas as pd
df = pd.read_csv('data.csv')
cols = list(df.columns)

df[cols[1:-1]].to_csv('output.csv')

