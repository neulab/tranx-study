# Example code, write your program here
import pandas as pd

df = pd.read_csv("automobile_data.csv")
df = df[df["price"].isnull() != True]
df1 = pd.DataFrame(df["company"].unique(), columns=["company"])
# first file
for comp in df["company"].unique():
    df2 = df[df["company"] == comp]

    df1.loc[df1["company"] == comp, "avg_price"] = df2.price.mean()
    df1.loc[df1["company"] == comp, "max_price"] = df2.price.max()
    df1.loc[df1["company"] == comp, "min_price"] = df2.price.min()
    df1.loc[df1["company"] == comp, "stddev_price"] = df2.price.std()
    df1.loc[df1["company"] == comp, "total_count"] = df2.shape[0]

df1.total_count = df1.total_count.astype(int)
df1.stddev_price.fillna("", inplace=True)
df1 = df1.round(2)
df1.sort_values("avg_price", ascending=False, inplace=True)
df1.to_csv("output/price_by_company.csv", index=False)
# second file
df4 = pd.DataFrame(columns=["horsepower_range", "avg_price", "count"])

for i in range(0, 280, 20):
    df3 = df[df["horsepower"] > i]
    df3 = df3[df["horsepower"] <= i + 20]
    x = "(" + str(i) + "," + str(i + 20) + "]"
    df4 = df4.append({'horsepower_range': x, "count": df3.shape[0], 'avg_price': df3.price.mean()},
                     ignore_index=True)

df4 = df4.round(2)
df4.avg_price.fillna("", inplace=True)

df4.to_csv("output/price_by_horsepower.csv", index=False)
# third file

df5 = df[df["price"] <= 15000]
df5 = df5[df["length"] <= 180]
df5.loc[ :,"score"] = df5.loc[:,"horsepower"] / (df5.loc[:,'average-mileage'] * df5.loc[:,"price"])
df5.score=df5.score.round(7)

#df5.total_count = df5.price.astype(int)
df5.sort_values("score", ascending=False, inplace=True)
df5.to_csv("output/for_john.csv",index=False)