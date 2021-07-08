# Example code, write your program here
import pandas as pd
import numpy as np

df = pd.read_csv('automobile_data.csv')

a = df.groupby('company', as_index=False) \
      .agg({'price': ['mean', 'max', 'min', 'std', 'count']})

a.columns = ['company', 'avg_price', 'max_price', 'min_price', 'stddev_price', 'total_count']
a = a.sort_values('avg_price', ascending=False)

a.to_csv('output/price_by_company.csv', index=False, float_format = '%.2f')

minhp = round(df['horsepower'].min() / 20) * 20
maxhp = round(df['horsepower'].max() / 20) * 20

b = df.groupby(pd.cut(df['horsepower'], range(int(minhp), int(maxhp+1), 20))) \
      .agg({'price': ['mean', 'count']})


b.reset_index(level=0, inplace=True)
b.columns = ['horsepower_range', 'avg_price', 'count']

b.to_csv('output/price_by_horsepower.csv', index=False, float_format = '%.2f')

c = df[df['price'] <= 15000]
c = c[c['length'] < 180]
c = c.dropna()
c['score'] = c['horsepower'] / ( c['average-mileage'] * c['price'])
c['score'] = c['score'].map(lambda x: '%.7f' % x)
c = c.sort_values('score', ascending=False)
c['price'] = c['price'].astype(np.int64)

c.to_csv('output/for_john.csv', index=False)

print(c)