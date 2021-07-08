# Example code, write your program here
from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import date2num


def main():
    df = pd.read_csv("shampoo.csv")
    dates = date2num([datetime.strptime(date, "%Y-%m-%d") for date in df['Date']])
    fig = plt.figure(figsize=(10, 6))
    plt.plot_date(dates, df['Sales'], c='purple')
    plt.xlabel('Date', fontsize=16)
    plt.ylabel('Sales', fontsize=16)
    plt.title("Shampoo Sales Trend", fontsize=20)
    plt.tick_params(axis='both', which='major', labelsize=12)
    fig.savefig('shampoo.png')


if __name__ == '__main__':
    main()
