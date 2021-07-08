import pandas
import numpy

data = pandas.read_csv("automobile_data.csv")

# drop empty rows
data.dropna()

# price by company
pbc_df = pandas.DataFrame(columns=['company', 'avg_price', 'max_price', 'min_price', 'stddev_price', 'total_count'])
pbc = data.groupby('company')

df = {}
for com in pbc:
    df = {'company': com[0],
          'avg_price': numpy.mean(com[1]['price']).round(decimals=2),
          'max_price': numpy.max(com[1]['price']).round(decimals=2),
          'min_price': numpy.min(com[1]['price']).round(decimals=2),
          'stddev_price': numpy.std(com[1]['price']).round(decimals=2),
          'total_count': numpy.count_nonzero(com[1]['price'])}

    pbc_df = pbc_df.append(df, ignore_index=True)
pbc_df = pbc_df.sort_values(by='avg_price', ascending=False)
pbc_df.to_csv('./output/price_by_company.csv', index=False)

# price by horsepower
pbh_df = pandas.DataFrame(columns=['horsepower_range', 'avg_price', 'count'])
pbh = data.filter(['horsepower', 'price'])
pbh = pbh.groupby(pandas.cut(pbh['horsepower'], numpy.arange(40, 300, 20)))

for ran in pbh:
    if ran[1]['horsepower'].count() != 0:
        df = {'horsepower_range': ran[0],
              'avg_price': numpy.mean(ran[1]['price']).round(decimals=2),
              'count': ran[1]['horsepower'].count()}
    else:
        df = {'horsepower_range': ran[0],
              'avg_price': numpy.mean(ran[1]['price']),
              'count': ran[1]['horsepower'].count()}

    pbh_df = pbh_df.append(df, ignore_index=True)

pbh_df.to_csv('./output/price_by_horsepower.csv', index=False)

#for john

john_df = pandas.DataFrame(columns=['index', 'company', 'body-style', 'wheel-base',
                                    'length', 'engine-type', 'num-of-cylinders',
                                    'horsepower', 'average-mileage', 'price', 'score'])

for car in data.groupby('index'):
    if float(car[1]['length']) <= 180 and float(car[1]['price']) <= 15000:
        score = float(car[1]['horsepower']) / (float(car[1]['average-mileage']) * float(car[1]['price']))
        score = numpy.round(score, decimals=7)

        df = pandas.DataFrame({'index': car[0], 'company': car[1]['company'],
              'body-style': car[1]['body-style'], 'wheel-base': car[1]['wheel-base'],
              'length': car[1]['length'], 'engine-type': car[1]['engine-type'],
              'num-of-cylinders': car[1]['num-of-cylinders'], 'horsepower': car[1]['horsepower'],
              'average-mileage': car[1]['average-mileage'], 'price': car[1]['price'],
              'score': score})

        john_df = john_df.append(df, ignore_index=True)

john_df = john_df.sort_values('score', ascending=False)
john_df.to_csv('./output/for_john.csv',index=False)
