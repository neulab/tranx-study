# Example code, write your program here
from statistics import mean, stdev, StatisticsError
from operator import itemgetter
import numpy as np

with open('automobile_data.csv') as infile:
    company_price_dict = dict()
    in_data = infile.readlines()
    for row in in_data[1:]:
        row_data = row.split(',')
        company_name = row_data[1]
        price = int(row_data[-1]) if row_data[-1] != '\n' else -1
        if price == -1:
            continue
        if company_name not in company_price_dict.keys():
            company_price_dict[company_name] = [price]
        else:
            company_price_dict[company_name].append(price)
    with open('output/price_by_company.csv', 'w+') as outfile:
        outfile.write('company,avg_price,max_price,min_price,stddev_price,total_count'+'\n')
        price_by_company_list = list()
        for company_name in company_price_dict:
            price_list = company_price_dict[company_name]
            avg_price = mean(price_list)
            max_price = str("%.2f" % max(price_list))
            min_price = str("%.2f" % min(price_list))
            try:
                stddev_price = str("%.2f" % stdev(price_list))
            except StatisticsError:
                stddev_price = ''
            total_count = str(len(price_list))
            price_by_company_list.append([company_name, avg_price, max_price, min_price, stddev_price, total_count])
        write_data_list = (sorted(price_by_company_list, key=itemgetter(1), reverse=True))
        for row in write_data_list:
            outfile.write(row[0] + ',' + str("%.2f" % row[1]) + ',' + ','.join(row[2:]) + '\n')
    max_horsepower = max(int(row.split(',')[-3]) for row in in_data[1:] if row_data[-1] != '\n')
    horse_power_range_dict = {i: [] for i in range(40, max_horsepower-20, 20)}
    for horse_power_range in horse_power_range_dict.keys():
        for row in in_data[1:]:
            row_data = row.split(',')
            price = row_data[-1]
            if price == '\n':
                continue
            horse_power = int(row_data[-3])
            if horse_power in range(horse_power_range+1, horse_power_range+21):
                horse_power_range_dict[horse_power_range].append(price)
    with open('output/price_by_horsepower.csv', 'w+') as outfile:
        outfile.write('horsepower_range,avg_price,count' + '\n')
        for horse_power_range, price_list in horse_power_range_dict.items():
            count = len(price_list)
            avg_price = str("%.2f" % mean(int(price[:-1]) for price in price_list)) if count > 0 else ''
            outfile.write('"(' + str(horse_power_range) + ', ' + str(horse_power_range + 20) + ']",' + avg_price + ',' + str(count) + '\n')
    custom_filter_list = []
    for row in in_data[1:]:
        row_data = row.split(',')
        company_name = row_data[1]
        price = int(row_data[-1]) if row_data[-1] != '\n' else -1
        length = float(row_data[4])
        if price == -1 or price > 15000 or length > 180:
            continue
        horse_power = int(row_data[-3])
        average_mileage = int(row_data[-2])
        score = "%.7f" % (horse_power/(average_mileage*price))
        custom_filter_list.append([','.join(row_data[:4]) + ',' + str(length) + ',' + ','.join(row_data[5:-1]) + ',' + row_data[-1][:-1], score])
    custom_filter_list = sorted(custom_filter_list, key=itemgetter(1), reverse=True)
    with open('output/for_john.csv', 'w+') as outfile:
        outfile.write('index,company,body-style,wheel-base,length,engine-type,num-of-cylinders,horsepower,average-mileage,price,score' + '\n')
        for row in custom_filter_list:
            outfile.write(row[0] + ',' + str(row[1]) + '\n')
