# Example code, write your program here
import re

import pandas as pd
import numpy as np
import os
out_path ="output"
df = pd.read_csv('automobile_data.csv')
company = df['company'].unique()
groupData = df.groupby('company')

avg_price = groupData['price'].mean()
max_price = groupData['price'].max()
min_price = groupData['price'].min()
stddev_price = groupData['price'].agg(np.std, ddof=0)
total_count = groupData['company'].count()

dict ={'company':company,'avg_price':avg_price,'max_price':max_price,
       'min_price':min_price, 'stddev_price':stddev_price, 'total_count':total_count}
Frame = pd.DataFrame(dict)
Frame = Frame.drop(Frame.columns[0], axis=1)  # df.columns is zero-based pd.Index
Frame = Frame.sort_values('avg_price',ascending=False)

Frame.to_csv(os.path.join(out_path,"price_by_company.csv"), float_format='%.2f')

# *************************** Second Require ***************
df_horse = df[df['horsepower'] > 80]
df_horse = df[df['horsepower'] < 100]

groupData = df_horse.groupby('company')

horsepower_range = groupData['horsepower'].apply(list)
avg_price = groupData['price'].mean()
count = groupData['company'].count()
company = df_horse['company'].unique()
dict ={'company':company, 'horsepower_range':horsepower_range
       ,'avg_price':avg_price,'count':count}

Frame = pd.DataFrame(dict)
Frame = Frame.drop(Frame.columns[0], axis=1)  # df.columns is zero-based pd.Index
Frame.to_csv(os.path.join(out_path,"price_by_horsepower.csv"), float_format='%.2f')

#****************************** Third Require ***************

df = pd.read_csv('automobile_data.csv')
df.to_csv(os.path.join(out_path,"for_john.csv"), float_format='%.7f')
df_john = pd.read_csv(os.path.join(out_path,"for_john.csv"))

NewCol = ( df_john['horsepower']/ (df_john['average-mileage'] + df_john['price'])).tolist()
#dict = {'score':NewCol}
print(NewCol)
#df_john = pd.DataFrame(dict)
df_john['score'] = NewCol
df_john = df_john.sort_values('score',ascending=False)
df_john = df_john.drop(df_john.columns[0], axis=1)  # df.columns is zero-based pd.Index
df_john.to_csv(os.path.join(out_path,"for_john.csv"), float_format='%.7f')
