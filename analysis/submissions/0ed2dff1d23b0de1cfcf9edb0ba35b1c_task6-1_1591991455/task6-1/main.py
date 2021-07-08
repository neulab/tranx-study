# Example code, write your program here
from collections import OrderedDict

import pandas as pd
import numpy as np


def main():
    df = pd.read_csv("automobile_data.csv")

    # Task 1
    df_by_company = df.groupby("company")
    columns = OrderedDict([
        ("avg_price", df_by_company["price"].mean()),
        ("max_price", df_by_company["price"].max()),
        ("min_price", df_by_company["price"].min()),
        ("stddev_price", df_by_company["price"].std()),
        ("total_count", df_by_company["price"].count()),
    ])
    merged = pd.concat(columns.values(), axis=1)
    merged = merged.set_axis(columns.keys(), axis=1)
    merged = merged.sort_values("avg_price", ascending=False)
    merged.to_csv("output/price_by_company.csv", float_format="%.2f")

    bins = np.arange(df['horsepower'].min() // 20 * 20,
                     df['horsepower'].max() + 19, 20)
    df_binned = pd.cut(df['horsepower'], bins)
    df_2 = df.copy(deep=True)
    df_2['horsepower_range'] = df_binned
    df_by_hp = df_2.groupby('horsepower_range')
    columns = OrderedDict([
        ("avg_price", df_by_hp['price'].mean()),
        ("count", df_by_hp['price'].count()),
    ])
    merged = pd.concat(columns.values(), axis=1)
    merged = merged.set_axis(columns.keys(), axis=1)
    merged = merged.sort_values("horsepower_range", ascending=True)
    merged.to_csv("output/price_by_horsepower.csv", float_format="%.2f")

    df_john = df.loc[(df['price'] <= 15000) & (df['length'] < 180)].copy(deep=True)
    df_john['score'] = df_john.apply(lambda r: r['horsepower'] / (r['average-mileage'] * r['price']), axis=1)
    df_john['score'] = df_john['score'].round(7)
    df_john = df_john.sort_values("score", ascending=False)
    df_john.to_csv("output/for_john.csv", index=False)


if __name__ == '__main__':
    main()
