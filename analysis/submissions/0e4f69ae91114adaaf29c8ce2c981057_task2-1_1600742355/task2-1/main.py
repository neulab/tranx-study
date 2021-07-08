# Example code, write your program here
import pandas as pd
df = pd.read_csv('data.csv', sep=',')
output = df.drop('id', axis=1)
output = output.drop('ip_address', axis=1)
output.to_csv('output.csv', index=False)



