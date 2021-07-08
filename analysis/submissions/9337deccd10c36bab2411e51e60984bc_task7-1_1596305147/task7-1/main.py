# Example code, write your program here
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('shampoo.csv')
fig = plt.gcf()
fig.set_size_inches(10, 6)
plt.scatter(data['Date'].values, data['Sales'])
plt.xlabel('Date', size = 16)
plt.ylabel('Sales', size = 16)
plt.title('Shampoo sales trend', size = 20)
plt.tick_params(axis = 'both', labelsize = 12, labelrotation = 90)
fig.savefig('shampoo.png', bbox_inches = 'tight')