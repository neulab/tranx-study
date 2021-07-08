# Example code, write your program here
import pandas as pd
import numpy as np

data = pd.read_csv('automobile_data.csv', usecols = ['company', 'price'])
final_data = data.groupby(['company']).mean().rename(columns = {'price' : 'avg_price'}).round(2)
final_data = final_data.merge(data.groupby(['company']).max(), left_on = 'company', right_on = 'company').rename(columns = {'price' : 'max_price'})
final_data = final_data.merge(data.groupby(['company']).min(), left_on = 'company', right_on = 'company').rename(columns = {'price' : 'min_price'})
final_data = final_data.merge(data.groupby(['company']).std(), left_on = 'company', right_on = 'company').rename(columns = {'price' : 'stddev_price'}).round(2)
final_data = final_data.merge(data.groupby(['company']).count(), left_on = 'company', right_on = 'company').rename(columns = {'price' : 'total_count'})
final_data.sort_values('avg_price', ascending=False).to_csv('output/price_by_company.csv')


data = pd.read_csv('automobile_data.csv', usecols = ['horsepower', 'price'])
final_data = data.groupby(pd.cut(data['horsepower'], np.arange(40, 300, 20)))['price'].aggregate(['mean', 'count']).round(2)
final_data = final_data.rename(columns = {'mean' : 'avg_price'})
final_data.to_csv('output/price_by_horsepower.csv')

data = pd.read_csv('automobile_data.csv', index_col='index')
data = data[data['price'] <= 15000]
data = data[data['length'] <= 180]
data['scores'] = (data['horsepower']/(data['average-mileage'] * data['price'])).round(7)
data.sort_values('scores', ascending=False).to_csv('output/for_john.csv')
