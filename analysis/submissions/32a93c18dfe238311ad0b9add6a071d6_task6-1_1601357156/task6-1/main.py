import pandas as pd
import numpy as np
all_data = pd.read_csv('automobile_data.csv')
all_data = all_data.dropna()
by_comp = all_data.groupby('company').agg({'price': ['mean', 'min', 'max', 'std', 'count']})
by_comp.columns = ['avg_price', 'min_price', 'max_price', 'stddev_price', 'total_count']
by_comp = by_comp.reset_index()
by_comp = by_comp.round(decimals=2)
by_comp.sort_values('avg_price', ascending=False, inplace=True)
by_comp.to_csv(r'output/price_by_company.csv',index=False)

by_hp = pd.DataFrame(all_data.groupby(pd.cut(all_data['horsepower'], np.arange(40, 300, 20)))['horsepower'].agg(['count', 'mean']))
by_hp.rename({'mean': 'avg_price'}, axis=1,inplace=True)
by_hp = by_hp.round(decimals=2)
by_hp.to_csv(r'output/price_by_horsepower.csv',index=True)

john = pd.DataFrame(all_data.loc[all_data['length'] <= 180.0])
john['score'] = (john['horsepower'] / (john['average-mileage'] * john['price']))
john['score'] = john['score'].map(lambda x: '%.7f' % x)
john.sort_values('score', ascending=False, inplace=True)
john.to_csv(r'output/for_john.csv',index=False)