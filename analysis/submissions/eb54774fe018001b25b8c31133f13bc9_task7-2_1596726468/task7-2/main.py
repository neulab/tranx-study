# Example code, write your program here
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def autolabel(Ax,rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        Ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')



df = pd.read_csv('StudentsPerformance.csv')

grp = df.groupby('gender')

males = pd.DataFrame(grp.get_group("male"))
females = pd.DataFrame(grp.get_group("female"))

malesGrp=males.groupby("race/ethnicity")
femalesGrp=females.groupby("race/ethnicity")

races = ["group A", "group B", "group C", "group D", "group E"]
subjects = ["math score", "reading score", "writing score"]

maleScore={"math score":[],"reading score":[],"writing score":[]}
femaleScore={"math score":[],"reading score":[],"writing score":[]}

for s in subjects:
    for r in races:
        # print("Male "+r+" "+s+": "+str(pd.DataFrame(malesGrp.get_group(r))[s].to_numpy().mean()))
        # print("Female " + r + " " + s + ": " + str(pd.DataFrame(femalesGrp.get_group(r))[s].to_numpy().mean()))
        maleScore[s].append(float(format(pd.DataFrame(malesGrp.get_group(r))[s].to_numpy().mean(), ".2f")))
        femaleScore[s].append(float(format(pd.DataFrame(femalesGrp.get_group(r))[s].to_numpy().mean(), ".2f")))

# print(maleScore)
# print(femaleScore)
# makes the data

xAxis=[0,1,2,3,4]
labels=["A","B","C","D","E"]
wi = np.arange(len(xAxis))
width=0.35



# plt.savefig("output/test.png")



#labels = ['G1', 'G2', 'G3', 'G4', 'G5']

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ((ax,ax1,ax2)) = plt.subplots(nrows=1,ncols=3,figsize=(20,6))
fig.suptitle("Scores by race/ethnicity and gender")

rects1 = ax.bar(x - width/2, maleScore["math score"], width, label='Male')
rects2 = ax.bar(x + width/2, femaleScore["math score"], width, label='Female')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Average Score')
ax.set_xlabel('Race/Ethnicity')
ax.set_title('Math')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

autolabel(ax,rects1)
autolabel(ax,rects2)

rects1 = ax1.bar(x - width/2, maleScore["reading score"], width, label='Male')
rects2 = ax1.bar(x + width/2, femaleScore["reading score"], width, label='Female')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax1.set_ylabel('Average Score')
ax1.set_xlabel('Race/Ethnicity')
ax1.set_title('Reading')

ax1.set_xticks(x)
ax1.set_xticklabels(labels)
ax1.legend()

autolabel(ax1,rects1)
autolabel(ax1,rects2)

rects1 = ax2.bar(x - width/2, maleScore["writing score"], width, label='Male')
rects2 = ax2.bar(x + width/2, femaleScore["writing score"], width, label='Female')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax2.set_ylabel('Average Score')
ax2.set_xlabel('Race/Ethnicity')
ax2.set_title('Writing')

ax2.set_xticks(x)
ax2.set_xticklabels(labels)
ax2.legend()


autolabel(ax2,rects1)
autolabel(ax2,rects2)

# fig.tight_layout()

#plt.show()

plt.savefig("output/grouped_scores.png")
