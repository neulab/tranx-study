# Example code, write your program here
import pandas as pd

df=pd.read_csv("automobile_data.csv")
df.dropna()
df1=df[['company','price']]

max_price=df1.groupby('company')['price'].max()
avg_price=df1.groupby('company')['price'].mean().round(2)
min_price=df1.groupby('company')['price'].min()
stddev_price=df1.groupby('company')['price'].std().round(2)

df1=df1.drop_duplicates(subset='company',keep='first')

df1.insert(2,'max_price',max_price.values)
df1.insert(2,'min_price',min_price.values)
df1.insert(2,'stddev_price',stddev_price.values)
df1.insert(2,'avg_price',avg_price.values)

df1=df1.drop('price', axis=1)
df1=df1.sort_values('avg_price',ascending=False)
df1=df1.reset_index()

df1.to_csv(path_or_buf='output/price_by_company.csv')


df2=df[['horsepower','price']]
df2['horsepower_range']=pd.cut(df['horsepower'],bins=[40,60,80,100,120,140,160,180] )

df2.drop('horsepower',axis=1,inplace=True)
count=df2.groupby('horsepower_range').count()

avg_price=df2.groupby('horsepower_range')['price'].mean().round(2)

print((avg_price.values))
df2=pd.DataFrame()
df2.insert(0,'avg_price',avg_price)
df2.insert(0,'count',count)
df2.to_csv(path_or_buf='output/price_by_horsepoer.csv')
df=df.query('price < 15000')
df=df.reset_index()
print(df['price'])

df3=df[['price','horsepower','average-mileage']]
score= df3['horsepower']/(df3['price']*df3['average-mileage'])
score= round(score,5)
df3=df.drop('index',1)

df3.insert(10,'score',score)
df3=df3.sort_values('score').reset_index()
df3.to_csv(path_or_buf='output/for_john.csv')