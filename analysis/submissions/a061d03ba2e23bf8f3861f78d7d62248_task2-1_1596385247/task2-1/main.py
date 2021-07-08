# Example code, write your program here
import pandas as pd

df = pd.read_csv('data.csv')

import os
if not os.path.exists('output'):
    os.makedirs('output')


df[df.columns[1:-1]].to_csv('output/output.csv', index=False)




