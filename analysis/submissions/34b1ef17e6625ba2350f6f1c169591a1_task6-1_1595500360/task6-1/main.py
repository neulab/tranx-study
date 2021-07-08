# Example code, write your program here
import pandas as pd

df = pd.read_csv('automobile_data.csv', sep=',')
df.dropna(inplace=True)

group = df.groupby(["company"])
price_by_company = pd.DataFrame({
    'avg_price': group['price'].mean(),
    'max_price': group['price'].max(),
    'min_price': group['price'].min(),
    'stddev_price': group['price'].std(),
    'total_count': group.size(),
}).reset_index()
price_by_company.sort_values(by='avg_price', ascending=False, inplace=True)
price_by_company.to_csv('output/price_by_company.csv', index=False, float_format='%.2f')

ranges = range(0, max(df.horsepower), 20)
gp_horsepower = df.groupby(pd.cut(df.horsepower, ranges))
price_by_horsepower = pd.DataFrame({
    'avg_price': gp_horsepower['price'].mean(),
    'count': gp_horsepower.size(),
}).reset_index()
price_by_horsepower.rename(columns={'horsepower': 'horsepower_range'}, inplace=True)
price_by_horsepower.to_csv('output/price_by_horsepower.csv', index=False, float_format='%.2f')

for_john = df.drop(df[(df.price > 15000) | (df.length >= 180)].index)
for_john['score'] = for_john['horsepower'] / (for_john['average-mileage'] * for_john['price'])
for_john['score'] = for_john['score'].map(lambda x: '%.7f' % x)
for_john['price'] = for_john['price'].astype(int)
for_john.sort_values(by='score', ascending=False, inplace=True)
for_john.to_csv('output/for_john.csv', index=False)
