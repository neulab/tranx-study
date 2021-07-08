# Example code, write your program here
import pandas as pd
pd.options.display.float_format = "{:,.7f}".format
df = pd.read_csv('automobile_data.csv')
grouped = df.groupby('company')['price']
df_new= grouped.agg(['mean', 'max', 'min', 'std', 'count'])
df_new2 = df_new.rename(columns={'mean':'avg_price','max':'max_price','min':'min_price', 'std':'stddev_price','count':'total_count'})
df_new2 = df_new.sort_values('mean', ascending=False)
df_new2.to_csv('output/price_by_company', sep=',', float_format="%.2f")
grouped1 = df.groupby(pd.cut(df['horsepower'], range(0, 281, 20)))['price']
df_new3 = grouped1.agg(['mean', 'count'])
df_new3 = df_new3.rename(columns={'mean':'avg_price' ,'count':'count'})
df_new3.to_csv('output/price_by_horsepower', sep=',', float_format="%.2f")
price = df['price'] <= 15000
length = df['length'] < 180
df['score'] = df['horsepower']/(df['average-mileage'] * df['price'])
df[price & length].to_csv('output/for_john.csv', sep=',', float_format="%.7f")