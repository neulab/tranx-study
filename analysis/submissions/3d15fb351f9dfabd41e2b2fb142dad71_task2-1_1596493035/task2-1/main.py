# Example code, write your program here
import pandas as pd
def task2_1():
    inp=pd.read_csv("/vagrant/task2-1/data.csv")
    df=inp[['first_name','last_name','email','gender']]
    df.to_csv("/vagrant/task2-1/output/output.csv",index=False)

task2_1()