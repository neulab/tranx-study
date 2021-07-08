# Example code, write your program here

# Import pandas library
import pandas

# Import math library
import math

# Filename definition
fileName = 'automobile_data.csv'

# Pandas data
data = pandas.read_csv(fileName, error_bad_lines=False)

# Columns name - Output 1
columnsName1 = ['company', 'avg_price', 'max_price', 'min_price', 'stddev_price']

# Columns name - Output 2
columnsName2 = ['horsepower_range', 'avg_price', 'count']

# Columns name - Output 3
columnsName3 = list(data.columns) + ['score']

# Reduced data for output1
reduced_data1 = data[['company', 'price']]

# Define new columns
reduced_data1.insert(1, 'avg_price', reduced_data1['price'], True)
reduced_data1.insert(2, 'max_price', reduced_data1['price'], True)
reduced_data1.insert(3, 'min_price', reduced_data1['price'], True)
reduced_data1.insert(4, 'stddev_price', reduced_data1['price'], True)
reduced_data1.insert(5, 'total_count', reduced_data1['price'], True)

# Output data 1
output_data1 = reduced_data1.groupby(['company']).agg({'avg_price': 'mean',
                                                      'max_price': 'max',
                                                      'min_price': 'min',
                                                      'stddev_price': 'std',
                                                      'total_count':  'count'})

# Remove rows with NaN
output_data1 = output_data1.apply(pandas.to_numeric, errors='coerce')
output_data1 = output_data1.dropna()

# Sort rows in descending order (average price)
output_data1 = output_data1.sort_values(by='avg_price', ascending=False)

# Save panda to output file
output_data1.to_csv('output/price_by_company.csv', float_format='%.2f')

# Minimum value of horse power
minValue = math.floor(data['horsepower'].min() / 10) * 10

# Maximum value of horse power
maxValue = math.ceil(data['horsepower'].max() / 10) * 10

# Spacing definition
spacing = 20

# Number of divisions
nDiv = math.ceil((maxValue - minValue) / spacing)

# Pandas dataframe initialization
output_data2 = pandas.DataFrame(columns=['horsepower_range', 'avg_price' ,'count'])

# Loop over the number of divisions
for i in range(0, nDiv):

    # First point of range
    lower_range = minValue + (spacing*i)

    # Second point of range
    higher_range = minValue + (spacing*(i+1))

    # Data portion for output2
    data2 = data.loc[(data['horsepower'] >= lower_range) & (data['horsepower'] <= higher_range)]

    # Pandas data frame in each iteration
    output_data_iter = pandas.DataFrame({'horsepower_range': ["(" + str(lower_range) + ', ' + str(higher_range) + "]"],
                                         'avg_price': data2['price'].mean(),
                                         'count': data2['price'].count()})

    # Append to output data
    output_data2 = output_data2.append(output_data_iter)

# Remove rows with NaN
output_data2 = output_data2.dropna(subset=['avg_price'])

# Save panda to output file
output_data2.to_csv('output/price_by_horsepower.csv', float_format='%.2f', index=False)

# Data portion for output3
output_data3 = data.loc[(data['length'] < 180) & (data['price'] < 15000)]

# Score function
output_data3.insert(10, 'score', (output_data3['horsepower'] / (output_data3['average-mileage'] * output_data3['price'])), True)

# Sort rows in descending order (average price)
output_data3 = output_data3.sort_values(by='score', ascending=False)

# Round the number of digits for score
output_data3['price'] = output_data3['price'].astype(int)
output_data3['score'] = output_data3['score'].round(decimals=7)

# Save panda to output file
output_data3.to_csv('output/for_john.csv', index=False)