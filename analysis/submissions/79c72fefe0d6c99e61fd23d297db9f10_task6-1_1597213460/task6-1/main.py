# Example code, write your program here
import pandas as pd
import numpy as np

df = pd.read_csv('automobile_data.csv')
df.dropna(inplace=True)

ans1 = df.groupby('company').agg({'price': ['mean', 'max', 'min', 'std', 'count']}).\
    reset_index(0)
ans1.columns = ['company', 'avg_price', 'max_price', 'min_price', 'stddev_price', 'total_count']
for col in ans1.columns:
    if col != 'company':
        ans1[col] = ans1[col].apply(lambda x: round(float(x), 2))

ans1 = ans1.sort_values(by='avg_price', ascending=False)
ans1.to_csv('output/price_by_company.csv', index=False)

ans2 = df.groupby(pd.cut(df['horsepower'], list(np.arange(0, max(df['horsepower']), 20))))\
    .agg({'price':'mean', 'index':'count'}).reset_index(0)
ans2.columns = ['horsepower_range', 'avg_price', 'count']
ans2['avg_price'] = ans2['avg_price'].apply(lambda x: round(float(x), 2))
ans2['avg_price'].fillna(0, inplace=True)
ans2.to_csv('output/proce_by_horsepower.csv', index=False)


#score = horsepower / (avg_mileage * price)
ans3 = df[(df['price'] <= 15000) & (df['length'] < 180)]
ans3['score'] = ans3.apply(lambda x: round(x['horsepower'] / x['average-mileage'] * x['price'], 7), axis=1)
ans3 = ans3.sort_values(by='score', ascending=False)
ans3.to_csv('output/for_john.csv', index=False)

