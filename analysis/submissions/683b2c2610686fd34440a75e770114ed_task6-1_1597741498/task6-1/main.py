# Example code, write your program here
import statistics

cp2price = {}
with open('automobile_data.csv') as fin:
    for idx, line in enumerate(fin):
        if idx == 0:
            continue
        data = line.strip().split(',')
        if '' in data:
            continue
        cp = data[1]
        price = int(data[-1])
        if cp not in cp2price:
            cp2price[cp] = []
        cp2price[cp].append(price)

cp2avg = {}
cp2stats = {}
for cp in cp2price:
    data = cp2price[cp]
    avg = '{:0.2f}'.format(statistics.mean(data))
    mx = '{:0.2f}'.format(max(data))
    mn = '{:0.2f}'.format(min(data))
    try:
        stdev = '{:0.2f}'.format(statistics.stdev(data))
    except:
        stdev = ''
    cnt = len(data)
    cp2avg[cp] = statistics.mean(data)
    cp2stats[cp] = [avg, mx, mn, stdev, str(cnt)]

cp_sorted = [k for k, v in sorted(cp2avg.items(), key=lambda item: item[1], reverse=True)]
with open('output/price_by_company.csv', 'w') as fout:
    fout.write('company,avg_price,max_price,min_price,stddev_price,total_count\n')
    for cp in cp_sorted:
        fout.write(cp + ',' + ','.join(cp2stats[cp])+'\n')

car2score = {}
car2out = {}
with open('automobile_data.csv') as fin:
    for idx, line in enumerate(fin):
        if idx == 0:
            continue
        data = line.strip().split(',')
        if '' in data:
            continue
        price = int(data[-1])
        length = float(data[4])
        horsepower = float(data[-3])
        average_mileage = float(data[-2])
        car = data[0]
        if price <= 15000 and length < 180:
            score = horsepower / (average_mileage * price)
            car2score[car] = score
            car2out[car] = line.strip()+','+'{:0.7f}'.format(score)

car_sorted = [k for k, v in sorted(car2score.items(), key=lambda item: item[1], reverse=True)]
with open('output/for_john.csv', 'w') as fout:
    fout.write('index,company,body-style,wheel-base,length,engine-type,num-of-cylinders,horsepower,average-mileage,price,score\n')
    for car in car_sorted:
        fout.write(car2out[car]+'\n')
