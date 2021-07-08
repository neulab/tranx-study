# Example code, write your program here
import pandas as pd
from collections import defaultdict
import numpy as np

df = pd.read_csv('./automobile_data.csv')
company_info = defaultdict(list)
for i in range(len(df)):
    cur_d = df.iloc[i]
    company_info[cur_d.company].append(cur_d.price)

_company_info = {}
for k, v in company_info.items():
    cur_v = np.array(v)
    _company_info[k] = {'avg_price': np.mean(cur_v),
                        'max_price': np.max(cur_v),
                        'min_price': np.min(cur_v),
                        'stddev_price': np.std(cur_v),
                        'total_count': len(v)}

company_df = pd.DataFrame(_company_info)
print(company_df)

keys = company_info.keys()
company_df = pd.DataFrame({'company': list(keys),
                            'avg_price': [_company_info[x]['avg_price'] for x in keys],
                            'max_price': [_company_info[x]['max_price'] for x in keys],
                            'min_price': [_company_info[x]['min_price'] for x in keys],
                            'stddev_price': [_company_info[x]['stddev_price'] for x in keys],
                            'total_count': [_company_info[x]['total_count'] for x in keys],
                           })

company_df.to_csv("output/price_by_company.csv", index=False)


# part two
hp_info = defaultdict(list)
for i in range(len(df)):
    cur_d = df.iloc[i]
    hp_info[int(cur_d.horsepower / 20)].append(cur_d.price)
_hp_info = defaultdict(list)
keys = sorted(hp_info.keys())
_hp_info['horsepower_range'] = [f"[{x*20}, {(x+1)*20}]" for x in keys]
for key in keys:
    avg_price = '{:.2f}'.format(np.mean(np.array(hp_info[key])))
    _hp_info['avg_price'].append(avg_price)
    _hp_info['count'].append(len(hp_info[key]))
hp_df = pd.DataFrame(_hp_info)

hp_df.to_csv('output/price_by_horsepower.csv', index=False)

xx = list(df.columns.values)
selected_info = []
scores = []
for i in range(len(df)):
    cur_d = df.iloc[i]
    if cur_d.length <= 180:
        score = f'{cur_d["horsepower"] / (cur_d["average-mileage"] * cur_d["price"]) :.7f}'
        if score != 'nan':
            scores.append(score)
            selected_info.append(cur_d)
jdf = pd.DataFrame(selected_info, columns=xx)
jdf = jdf.assign(scores=pd.Series(scores))
jdf = jdf.sort_values(by='scores', ascending=False)
jdf.to_csv("./output/for_john.csv", index=False)


