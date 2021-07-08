# Example code, write your program here
import pandas as pd
df = pd.read_csv("data.csv")

df = df.drop(df.columns[[0, -1]], axis=1)

df.to_csv("output/output.csv",index=False)

