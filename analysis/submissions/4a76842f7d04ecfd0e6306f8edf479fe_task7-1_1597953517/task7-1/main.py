# Example code, write your program here
import matplotlib.pyplot as plt
import csv
from datetime import datetime
import matplotlib.figure
import numpy
# import pandas as pd
#######,xticks=["2019-12-15","2020-01-01","2020-01-15","2020-02-01","2020-02-15",
#                                                  "2020-03-01","2020-03-15"]
#p = pd.read_csv("shampoo.csv")
# p.plot(x="Date",y="Sales",kind="scatter",title="Shampoo Sales Trend",
#       figsize=(10,6),fontsize=12,color="m")
# plt.rcParams.update({'font.size':22})
x=[]
y=[]
flag=0
with open("shampoo.csv","r") as csvfile:
    plots=csv.reader(csvfile,delimiter=",")
    for rows in plots:
        if flag == 1:
            x.append(datetime.strptime(rows[0],"%Y-%m-%d"))
            y.append(float(rows[1]))
        else:
            flag = 1
# print(x)
# print(y)
plt.figure(figsize=(10,6))
plt.scatter(x,y,color='m')
#
plt.xlabel("Date",fontsize=16)
plt.ylabel("Sales",fontsize=16)
plt.title("Shampoo Sales Trend",fontsize=20)
plt.xticks(fontsize=12)
plt.xlim(xmin=datetime.strptime("2019-12-15","%Y-%m-%d"))
plt.yticks(fontsize=12)
plt.savefig("shampoo.png")

# print(p)
