import pandas as pd
import os.path

#Load data from csv file
data = pd.read_csv('automobile_data.csv').dropna()

#Generate a list of all the company names
companies = []
for company in data.company:
    if company not in companies:
        companies.append(company)

#Prepare lists for variables to be stored in
avg_price = []
max_price = []
min_price = []
stddev_price = []
cars = []

#Gather required data for each company
for comp in companies:
    comp_data = data[data.company == comp]
    count = 0
    maxvalue = 0
    minvalue = 1000000000
    totalvalue = 0
    for price in comp_data.price:
        if price > maxvalue:
            maxvalue = price
        if price < minvalue:
            minvalue = price
        totalvalue = totalvalue + price
        count += 1

    avg = ("%.2f" % round(totalvalue/count, 2))
    avg_price.append(avg)
    max_price.append("%.2f" % round(maxvalue, 2))
    min_price.append("%.2f" % round(minvalue, 2))
    cars.append(count)
    #Calulate standard deviation
    totalvalue = 0
    for price in comp_data.price:
        mean_diff = price - float(avg)
        totalvalue = totalvalue + (mean_diff)**2
    mean = totalvalue/count
    stddev = ("%.2f" % round(mean**0.5, 2))
    stddev_price.append(stddev)

#Arrange data into correct order and store in csv file:
data_folder = os.path.join("output")
file_to_open = os.path.join(data_folder, "price_by_company.csv")
with open(file_to_open, 'w') as fw:
    fw.write('company,avg_price,max_price,min_price,stddev_price,total_count\n')
    sorting = True
    while sorting:
        i = 0
        largest = 0
        for price in avg_price:
            if float(price) > largest:
                n = i
                largest = float(price)
            i += 1
        fw.write(companies[n]+','+avg_price[n]+','+str(max_price[n])+','+str(min_price[n])+','+str(stddev_price[n])+','+str(cars[n])+'\n')
        #Delete values which have been stored
        del companies[n]
        del avg_price[n]
        del max_price[n]
        del min_price[n]
        del stddev_price[n]
        del cars[n]
        if len(companies) == 0:
            sorting = False

#Get data for horsepower csv
hpr = []
rangel = 40
rangeu = 60
tracking = True
while tracking:
    count = 0
    totalprice = 0
    i = 0
    for hp in data.horsepower:
        if hp >= rangel and hp <= rangeu:
            count += 1
            totalprice = totalprice + data.price.iloc[i]
        i += 1
    hpr.append('"(' + str(rangel) + ', ' + str(rangeu) + ']"')
    if count == 0:
        avg = ''
    else:
        avg = ("%.2f" % round(totalprice/count, 2))
    avg_price.append(avg)
    cars.append(count)
    rangel += 20
    rangeu += 20
    if rangeu == 300:
        tracking = False

file_to_open = os.path.join(data_folder, "price_by_horsepower.csv")
with open(file_to_open, 'w') as fw:
    i = 0
    fw.write('horsepower_range,avg_price,count\n')
    for price in avg_price:
        fw.write(hpr[i] + ',' + str(price) + ',' + str(cars[i]) + '\n')
        i += 1

#Filter out cars that don't meet johns criteria and calculate scores
i = 0
ind = []
scores = []
for price in data.price:
    if price <= 15000 and data.length.iloc[i] < 180:
        ind.append(i)
        score = (data.horsepower.iloc[i])/((data.averagemileage.iloc[i])*price)
        scores.append("%.7f" % round(score, 7))
    i += 1

#Sort the scores for john csv
file_to_open = os.path.join(data_folder, "for_john.csv")
new_index = []
new_scores = []
sorting = True
while sorting:
    high_score = 0
    i = 0
    n = 0
    for score in scores:
        if float(score) > high_score:
            high_score = float(score)
            n = i
        i += 1
    new_index.append(ind[n])
    new_scores.append(high_score)
    del scores[n]
    del ind[n]
    if len(scores) == 0:
        sorting = False

#Create the john csv
with open(file_to_open, 'w') as fw:
    fw.write('index,company,body-style,wheel-base,length,engine-type,num-of-cylinders,horsepower,averagemileage,price,score\n')
    i = 0
    for value in new_index:
        with open('automobile_data.csv', 'r') as fr:
            lines = fr.readlines()
        newstring = ''
        for char in lines[value+1]:
            if char == '\n':
                break
            else:
                newstring = newstring + char
        fw.write(newstring + ',' + str(new_scores[i]) + '\n')
        i += 1
