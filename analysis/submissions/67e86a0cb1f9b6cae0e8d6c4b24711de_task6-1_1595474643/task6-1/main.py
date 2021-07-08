# Example code, write your program here
import pandas
df = pandas.read_csv('automobile_data.csv')
price_df = df.groupby('company')['price']
avg_price = price_df.mean()
max_price = price_df.max()
min_price = price_df.min()
stddev_price = price_df.std()
total_count = price_df.count()

with open('output/price_by_company.csv','w')as f:
    f.write(pandas.concat([avg_price,max_price,min_price,stddev_price,total_count],keys=['avg_price','max_price','min_price','stddev_price','total_count'],axis=1).to_csv())
hp_max = df['horsepower'].max()
bins=[0]
i=0
while i < hp_max:
    i+=20
    bins.append(i)
cut_group=df.groupby(pandas.cut(df['horsepower'], bins=bins,right=True))
avg_price = cut_group['price'].mean()
count = cut_group['price'].count()
with open('output/price_by_horsepower.csv','w')as out:
    out.write(pandas.concat([avg_price,count],keys=['avg_price','count'],axis=1).to_csv())

df = df[df['length'] <= 180]
df = df[df['price']<=15000]

df['score'] = df['horsepower']/(df['average-mileage']*df['price'])
df.sort_values('score',ascending=False)
with open('output/for_john.csv','w')as out:
    out.write(df.to_csv())