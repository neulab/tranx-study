# Example code, write your program here
import pandas as pd

df=pd.read_csv("data.csv")

df=df.drop('id',axis=1)
df=df.drop('ip_address',axis=1)

df.to_csv("example_output/output.csv")
