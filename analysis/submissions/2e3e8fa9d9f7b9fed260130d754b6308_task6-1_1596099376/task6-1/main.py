# Example code, write your program here

import pandas as pd
file=pd.read_csv("automobile_data.csv")
file.dropna(axis=0,inplace=True)
x=file.groupby('company')
y=pd.DataFrame({'avg_price':x.mean()['price'],"max_price":x.max()['price'],
                    "min_price":x.min()['price'],"stddev_price":x.std()['price'],
                    "total_counts":x.count()['price']})
y.reset_index(inplace=True)
y.sort_values(by='avg_price',ascending=False,inplace=True)
y.to_csv("output/price_by_company.csv")
price=[]
count=[]
y=pd.DataFrame({'horsepower_range'"avg_price":[],"count":[]})
file['score']=file['horsepower']/ (file['average-mileage']* file['price'])
file.to_csv('output/for_john.csc')