
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("shampoo.csv")
df['Date']=pd.to_datetime(df['Date'])

x = df['Date']
y =df['Sales']


fig, ax = plt.subplots(figsize=(10,6))
df.plot(x='Date', y='Sales', kind='scatter', ax=ax, color='purple')

plt.title("Shampoo Sales Trend", fontsize=20)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Sales', fontsize=16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig('shampoo.png', dpi=110)




