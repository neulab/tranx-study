# Example code, write your program here
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
def transtime(t):
    y, m, d = t.split('-')
    m = m.rjust(2, '0')
    ret = datetime.strptime('{0}-{1}-{2}'.format(y, m, d), "%Y-%m-%d")
    return ret

data = pd.read_csv('shampoo.csv')
Date, Sales = data['Date'].values, data['Sales'].values
Date = list(map(transtime, Date))
plt.figure(figsize=[10, 6])
plt.xlabel('Date', fontsize = 16)
plt.ylabel('Sales', fontsize = 16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.scatter(Date, Sales, color = 'purple')
plt.title('Shampoo Sales Trend', fontsize = 20)
plt.savefig('./shampoo.png')