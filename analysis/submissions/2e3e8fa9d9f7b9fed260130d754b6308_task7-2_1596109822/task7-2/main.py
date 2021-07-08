# Example code, write your program here
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("StudentsPerformance.csv")
fig,ax=plt.subplots(1,3,figsize=(20,6))
m=data[data['gender']=='male'].groupby('race/ethnicity')
f=data[data['gender']=='female'].groupby('race/ethnicity')
m.mean().plot(kind='bar',x='math score',ax=ax[0],label='Male')
f.mean().plot(kind='bar',x='math score',ax=ax[0],label='Female')
m.mean().plot(kind='bar',x='reading score',ax=ax[1],label='Male')
f.mean().plot(kind='bar',x='reading score',ax=ax[1],label='Female')
m.mean().plot(kind='bar',x='reading score',ax=ax[2],label='Male')
f.mean().plot(kind='bar',x='writing score',ax=ax[2],label="Female")
ax[0].set_title("Math")
ax[1].set_title("Reading")
ax[2].set_title("Writing")
for i in ax:
    i.legend(['Male','Female'],loc='upper left')
    i.set_xticklabels(["A", "B", "C", "D", "E"])
    i.set_xlabel('race/ethnictiy')
    i.set_ylabel('average score')
fig.savefig('grouped_scores.png')