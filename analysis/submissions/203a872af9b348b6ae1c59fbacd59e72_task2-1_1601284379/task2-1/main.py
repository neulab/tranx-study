import pandas as pd
import os

df = pd.read_csv('data.csv', sep=',', index_col='id')

df = df.iloc[1:len(df)-1]
print(df)

outdir = './output'
if not os.path.exists(outdir):
    os.mkdir(outdir)

file_name = os.path.join(outdir, 'output.csv')
df.to_csv(file_name, sep=',')


