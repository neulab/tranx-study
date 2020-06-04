# Task Description

You are expected to perform data analysis on automobile data listed in `automobile_data.csv`. Note that there might be some missing data in some columns, and in this case, please ignore the missing data rows.

After running `python main.py` the program should output several `.csv` files to `output` directory as described below:

1. `output/price_by_company.csv`: contains 5 columns `company`, `avg_price`, `max_price`, `min_price`, `stddev_price`, `total_count`, representing company name, the average, maximum, minimum and standard deviation of the price, as well as the count of all the cars manufactured by this company. The rows should be sorted from the highest average price to the lowest.
2. `output/price_by_horsepower.csv`: contains 3 columns `horsepower_range`, `avg_price` and `count`, representing the horsepower ranges bucketed by 20 interval (e.g. `80-100`), and the average price and count for the cars falling into this range. The rows should be sorted from the lowest horsepower range to the highest.
3. `output/for_john.csv`: John is trying to buy a car from this list, but he has a limited budget of 15000. His garage is also relatively small that could only fit cars under 180 in length. He also wants to take price, horsepower and average mileage into account, so he created a scoring function `score = horsepower / (average-mileage * price)` so he could find the car with high horsepower and low price and average mileage. In the output CSV file, list all the cars that matches his criteria, with all information represented under the original column names in the data file and an additional column at last `score` representing his own scoring function. The rows should be sorted from the highest score to the lowest to help John select his dream car!

# Example Output

```
$ python main.py

$ ls output/
price_by_company.csv  price_by_horsepower.csv  for_john.csv

```