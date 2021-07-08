# Example code, write your program here
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

x = []
y = []
with open('shampoo.csv') as fin:
    for idx, line in enumerate(fin):
        if idx == 0:
            continue
        data = line.strip().split(',')
        x.append(datetime.datetime.strptime(data[0].strip('\"'),'%Y-%m-%d').date())
        y.append(float(data[1]))

plt.figure(figsize=(10,6))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=15))
plt.scatter(x,y,color='purple')
plt.suptitle('Shampoo Sales Trend', fontsize=20)
plt.xlabel('Sales', fontsize=18)
plt.ylabel('Date', fontsize=18)
plt.savefig('shampoo.png')