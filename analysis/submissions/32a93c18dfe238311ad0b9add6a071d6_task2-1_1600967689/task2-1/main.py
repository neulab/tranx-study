# Example code, write your program here
import pandas
df = pandas.read_csv('data.csv')
df = df.drop(['id','ip_address'], axis=1)
df.to_csv(r'output/output.csv')