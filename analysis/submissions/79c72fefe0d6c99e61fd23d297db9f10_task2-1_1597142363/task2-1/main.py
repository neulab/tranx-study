# Example code, write your program here
import pandas as pd

df = pd.read_csv('data.csv')
subset_df = df.iloc[:, 1:-1]
subset_df.to_csv('output/output.csv')