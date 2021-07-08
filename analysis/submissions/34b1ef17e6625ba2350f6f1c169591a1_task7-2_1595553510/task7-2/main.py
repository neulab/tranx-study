# Example code, write your program here
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


def autolabel(rects, i):
    for rect in rects:
        h = rect.get_height()
        axs[i].text(rect.get_x()+rect.get_width()/2., h+1, '%.2f' % h, ha='center', va='bottom')


df = pd.read_csv("StudentsPerformance.csv")
fig, axs = plt.subplots(1, 3, figsize=(20, 6))
ind = np.arange(5)
width = 0.35
male = df.loc[df['gender'] == 'male'].groupby("race/ethnicity")
female = df.loc[df['gender'] == 'female'].groupby("race/ethnicity")

rects1 = axs[0].bar(ind - width/2, male['math score'].mean(), width, label='Male')
rects2 = axs[0].bar(ind + width/2, female['math score'].mean(), width, label='Female')
axs[0].set_xlabel('Race/Ethnicity')
axs[0].set_ylabel('Average Scores')
axs[0].set_title('Math')
axs[0].set_xticks(ind)
axs[0].set_xticklabels(('A', 'B', 'C', 'D', 'E'))
axs[0].legend()
autolabel(rects1, 0)
autolabel(rects2, 0)

rects1 = axs[1].bar(ind - width/2, male['reading score'].mean(), width, label='Male')
rects2 = axs[1].bar(ind + width/2, female['reading score'].mean(), width, label='Female')
axs[1].set_xlabel('Race/Ethnicity')
axs[1].set_ylabel('Average Scores')
axs[1].set_title('Reading')
axs[1].set_xticks(ind)
axs[1].set_xticklabels(('A', 'B', 'C', 'D', 'E'))
axs[1].legend()
autolabel(rects1, 1)
autolabel(rects2, 1)

rects1 = axs[2].bar(ind - width/2, male['writing score'].mean(), width, label='Male')
rects2 = axs[2].bar(ind + width/2, female['writing score'].mean(), width, label='Female')
axs[2].set_xlabel('Race/Ethnicity')
axs[2].set_ylabel('Average Scores')
axs[2].set_title('Writing')
axs[2].set_xticks(ind)
axs[2].set_xticklabels(('A', 'B', 'C', 'D', 'E'))
axs[2].legend()
autolabel(rects1, 2)
autolabel(rects2, 2)

fig.suptitle("Scores by race/ethnicity and gender")
plt.savefig("output/grouped_scores.png")
