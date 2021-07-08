# Example code, write your program here

import pandas as pd
import os

df = pd.read_csv('data.csv').drop(columns=['id', 'ip_address'])

os.makedirs('output', exist_ok=True)
df.to_csv('output/output.csv', index=False)

