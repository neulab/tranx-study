import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")
final_df = pd.DataFrame(sorted(df["race/ethnicity"].unique()), columns=["race/ethnicity"])
groups =sorted(df["race/ethnicity"].unique())

for group in groups :
    df1 = df[df["gender"] == "male"]
    df2 =df1[df1["race/ethnicity"]==group]
    final_df.loc[final_df["race/ethnicity"]==group, 'male math score'] = np.round(df2['math score'].mean(),2)
    final_df.loc[final_df["race/ethnicity"]==group, 'male reading score'] = np.round(df2['reading score'].mean(),2)
    final_df.loc[final_df["race/ethnicity"]==group, 'male writing score'] = np.round(df2['writing score'].mean(),2)
    df1 = df[df["gender"] == "female"]
    df2 = df1[df1["race/ethnicity"] == group]
    final_df.loc[final_df["race/ethnicity"] == group, 'female math score'] = np.round(df2['math score'].mean(), 2)
    final_df.loc[final_df["race/ethnicity"] == group, 'female reading score'] = np.round(df2['reading score'].mean(), 2)
    final_df.loc[final_df["race/ethnicity"] == group, 'female writing score'] = np.round(df2['writing score'].mean(), 2)

xt = ["A","B","C","D","E"]
xlabel="Race/Ethnicity"
ylabel="Average Scores"

fig = plt.figure(figsize=(20,6))
plt.axis('off')
plt.title("Scores by race/ethnicity and gender" ,loc='center',fontsize = 15,x=0.5, y=1.05)

ax1=fig.add_subplot(131)
x=final_df.plot.bar(x='race/ethnicity',y=['male math score','female math score'],rot=0,ax =ax1,width = 0.5 )

plt.title('Math')

plt.xlabel(xlabel)
plt.ylabel(ylabel)
ax1.set_xticklabels(xt, minor=False)
y1_1 = final_df['male math score']
y1_2 = final_df['female math score']
xlocs, xlabs = plt.xticks()
for i, v in enumerate(y1_1):
    plt.text(xlocs[i] - 0.35, v + 1, str(v))
for i, v in enumerate(y1_2):
    plt.text(xlocs[i] - 0.1, v + 1, str(v))
ax2=fig.add_subplot(132)
final_df.plot.bar(x='race/ethnicity',y=['male reading score','female reading score'],rot=0,ax =ax2,width = 0.5 )
plt.title('Reading')
plt.xlabel(xlabel)
plt.ylabel(ylabel)
ax2.set_xticklabels(xt, minor=False)
y2_1 = final_df['male reading score']
y2_2 = final_df['female reading score']
xlocs, xlabs = plt.xticks()
for i, v in enumerate(y2_1):
    plt.text(xlocs[i] - 0.35, v + 1, str(v))
for i, v in enumerate(y2_2):
    plt.text(xlocs[i] - 0.1, v + 1, str(v))
ax3=fig.add_subplot(133)
final_df.plot.bar(x='race/ethnicity',y=['male writing score','female writing score'],rot=0,ax =ax3,width = 0.5  )
plt.title('Writing')
plt.xlabel(xlabel)
plt.ylabel(ylabel)
ax3.set_xticklabels(xt, minor=False)
y3_1 = final_df['male writing score']
y3_2 = final_df['female writing score']
xlocs, xlabs = plt.xticks()
for i, v in enumerate(y3_1):
    plt.text(xlocs[i] - 0.35, v + 1, str(v))
for i, v in enumerate(y3_2):
    plt.text(xlocs[i] - 0.1, v + 1, str(v))

plt.savefig('/vagrant/task7-2/output/grouped_scores', dpi=110)
