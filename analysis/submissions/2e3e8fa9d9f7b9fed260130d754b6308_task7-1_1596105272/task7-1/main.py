# Example code, write your program here
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("shampoo.csv")
fig,ax=plt.subplots(figsize=(10,6))
ax.scatter(x=data['Date'],y=data['Sales'],color='#800080')
ax.set_title('Shampoo Sales Trend',fontsize=20)
ax.set_ylabel("sale",fontsize=16)
ax.set_xlabel("sale",fontsize=16)
ax.set_xticklabels(data['Date'],fontsize=12)
ax.set_yticklabels(data['Sales'],fontsize=12)
fig.savefig("shampoo.png")