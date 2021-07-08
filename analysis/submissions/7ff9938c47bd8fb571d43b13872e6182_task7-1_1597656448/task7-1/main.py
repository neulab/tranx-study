# Example code, write your program here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("shampoo.csv")
x=df[['Date']]
y=df[['Sales']]
#x=x.values
#y=np.array(y)
#print(type(x[1][0]))
fig,ax=plt.subplots(figsize=(10,10))
ax.scatter(df['Date'],df['Sales'],color='purple')
#ax.set(xlabel='Date',ylabel='Sales',title='shampoo sale trend')
plt.xlabel("Date", fontsize=20)
plt.ylabel("Sales", fontsize=20)
plt.title('shampoo sales trend',fontsize=20)
ax.tick_params(axis='x',labelsize=16,rotation=60)
ax.tick_params(axis='y',labelsize=12)
#plt.plot_date(x,y)
plt.savefig('shampoo')
