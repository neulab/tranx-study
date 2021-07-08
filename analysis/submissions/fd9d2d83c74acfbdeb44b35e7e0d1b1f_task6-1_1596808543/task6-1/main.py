# Example code, write your program here

import pandas as pd
import numpy as np

csvFile = pd.read_csv('automobile_data.csv')

stat1 = csvFile.groupby('company').agg({'price': ['mean', 'max', 'min', 'std']}).round(2)
stat1.columns = ['avg_price', 'max_price', 'min_price', 'stddev_price']
stat1 = stat1.sort_values(by=['avg_price'], ascending=False)
stat1.to_csv('output/price_by_company.csv')

stat2 = csvFile.groupby(pd.cut(csvFile['horsepower'], np.arange(0, csvFile['horsepower'].max(), 20))).agg({'price': ['mean'], 'index': ['count']}).round(2)
stat2.columns = ['avg_price', 'count']
stat2.to_csv('output/price_by_horsepower.csv')

stat3 = csvFile[csvFile['price'] < 15000]
stat3 = stat3[stat3['length'] < 180]
stat3['score'] = stat3['horsepower'] / (stat3['average-mileage'] * stat3['price'])
stat3['score'].round(7)
stat3 = stat3.sort_values(by=['score'], ascending=False)
stat3.to_csv('output/for_john.csv')
