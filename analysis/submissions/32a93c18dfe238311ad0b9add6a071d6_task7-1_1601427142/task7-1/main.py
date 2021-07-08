import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('shampoo.csv',parse_dates=['Date'])
plt.figure(figsize=(10,6),dpi=100)
plt.scatter(data['Date'],data['Sales'],c='purple')
plt.title('Shampoo Sales Trend',fontsize=20)
plt.xlabel("Date",fontsize=16)
plt.ylabel("Sales",fontsize=16)
plt.tick_params(labelsize=12)
plt.savefig('shampoo1.png')