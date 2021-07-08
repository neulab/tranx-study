# Example code, write your program here
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
data = pd.read_csv("shampoo.csv", parse_dates=['Date'], index_col=['Date'])
data.head()
f = plt.figure(figsize=(10, 6))
ax = f.add_subplot('111')
ax.scatter(data.index.values, data['Sales'], color='purple')
ax.set(xlabel='Date', ylabel='Sales', title='Shampoo Sales Trend')
plt.xlabel('Date', fontsize=16)
plt.ylabel('Sales', fontsize=16)
plt.title("Shampoo Sales Trend", fontsize=20)
plt.savefig('shampoo.png')

