# Example code, write your program here
import pandas as pd
def task2_1():
    inp=pd.read_csv("data.csv")
    df=inp[['first_name','last_name','email','gender']]
    df.to_csv("output/output.csv",index=False)

task2_1()