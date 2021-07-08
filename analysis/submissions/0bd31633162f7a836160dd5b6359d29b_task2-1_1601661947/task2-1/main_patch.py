import pandas as pd


columns_needed = ["first_name","last_name","email","gender"]
df = pd.read_csv('data.csv',  usecols = columns_needed)
df.to_csv(r'example_output/output.csv')
print(df)