# Example code, write your program here
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

df = pd.read_csv('shampoo.csv')

plt.figure(figsize=(10, 6))

d1 = datetime.strptime(min(df['Date']), '%Y-%m-%d')
d2 = datetime.strptime(max(df['Date']), '%Y-%m-%d')
all_dates = [d1 + timedelta(days=x) for x in range((d2-d1).days + 1)]
for date in all_dates:
    d = datetime.strftime(date, '%Y-%m-%d')
    if d not in df['Date']:
        to_append = [d, np.nan]
        a_series = pd.Series(to_append, index=df.columns)
        df = df.append(a_series, ignore_index=True)

plt.scatter(df['Date'], df['Sales'], c='purple')
plt.xlabel('Date', fontsize=16)
plt.ylabel('Sales', fontsize=16)
plt.title('Shampoo Sales Trend', fontsize=20)
plt.xticks(fontsize=12)
plt.savefig('shampoo.png')

