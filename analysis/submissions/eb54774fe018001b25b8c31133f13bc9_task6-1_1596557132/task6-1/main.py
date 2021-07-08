# Example code, write your program here
import numpy
import pandas
import os

if not os.path.exists("output"):
    os.mkdir("output")

p = pandas.read_csv("automobile_data.csv")
p = p.dropna()
x = p.groupby("company")
price_by_company = pandas.DataFrame(columns=["company", "avg_price","max_price","min_price","stddev_price","total_count"])

for name, group in x:
    df = pandas.DataFrame(x.get_group(name))
    new_entry = pandas.DataFrame([[ name,
                                    float(format(df['price'].to_numpy().mean(), ".2f")),
                                    float(format(df['price'].to_numpy().max(), ".2f")),
                                    float(format(df['price'].to_numpy().min(), ".2f")),
                                    float(format(df['price'].to_numpy().std(), ".2f")),
                                    df['price'].to_numpy().size]],
                                 columns=["company", "avg_price","max_price","min_price","stddev_price","total_count"])

    price_by_company = price_by_company.append(new_entry, ignore_index=True)
# print(price_by_company.sort_values("avg_price",ascending=False))
price_by_company.sort_values("avg_price", ascending=False).to_csv("output/price_by_company.csv", index=False)

price_by_company = pandas.DataFrame(columns=["horsepower_range", "avg_price", "count"])
for i in range(40,280,20):
    df = pandas.DataFrame(p[(p['horsepower'] >= i+1) & (p['horsepower'] <= (i+20))])
    Range = "("+str(i)+", "+str(i+20)+"]"
    if df.empty:
        new_entry = pandas.DataFrame([[Range,
                                       "",
                                       df['price'].to_numpy().size]],columns=["horsepower_range", "avg_price", "count"])
    else:
        new_entry = pandas.DataFrame([[Range,
                                       float(format(df['price'].to_numpy().mean(), ".2f")),
                                       df['price'].to_numpy().size]],
                                     columns=["horsepower_range", "avg_price", "count"])
    price_by_company = price_by_company.append(new_entry, ignore_index=True)
    # print(new_entry)
    # print(p['horsepower'].to_numpy().min())
price_by_company.to_csv("output/price_by_horsepower.csv", index=False)

price_by_company = pandas.DataFrame(columns=["index","company","body-style","wheel-base","length","engine-type",
                                             "num-of-cylinders","horsepower","average-mileage","price","score"])

df = pandas.DataFrame(p[(p['price'] <= 15000) & (p['length'] <= 180)])
df['score']=0
# print(df)
for index, row in df.iterrows():
    df['score'][index] = format(row['horsepower']/(row['average-mileage']*row['price']), ".7f")

df.sort_values("score", ascending=False).to_csv("output/for_john.csv", index=False)
