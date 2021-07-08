# Example code, write your program here
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import datetime
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import matplotlib.dates as dates
df = pd.read_csv("shampoo.csv")

fig, ax = plt.subplots(figsize=(10, 6))
plt_dates = dates.date2num(pd.to_datetime(df['Date'], format="%Y-%m-%d"))

ax.scatter(plt_dates, df['Sales'], color='purple')

ax.set(
       xlim=[datetime.datetime(2019, 12, 13), datetime.datetime(2020, 3, 31)]
       )

date_form = DateFormatter("%Y-%m-%d")
ax.xaxis.set_major_formatter(date_form)

ax.xaxis.set_major_locator(mdates.DayLocator(bymonthday=[1, 15]))

plt.title("Shampoo Sales Trend", fontsize=20)
plt.xlabel("Date", fontsize=16)
plt.ylabel("Sales", fontsize=16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.savefig(r'shampoo.png')
