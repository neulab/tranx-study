# Example code, write your program here
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('StudentsPerformance.csv')
agg = df.groupby(['gender', 'race/ethnicity']).mean().round(2)
fig = plt.figure(figsize=(20, 6))
fig.suptitle('Scores by race/ethnicity and gender')
ax = fig.add_subplot(131), fig.add_subplot(132), fig.add_subplot(133)
width = 0.35
labels = ['A', 'B', 'C', 'D', 'E']
keys = agg.keys()
titles = ['Math', 'Reading', 'Writing']
for i in range(3):
    x = np.arange(len(labels))
    data = agg[keys[i]]
    female_data = []
    male_data = []
    for j in range(5):
        female_data.append(data[data.keys()[j]])
        male_data.append(data[data.keys()[j + 5]])

    rects1 = ax[i].bar(x - width / 2, male_data, width, label = 'Male')
    rects2 = ax[i].bar(x + width / 2, female_data, width, label='Female')
    ax[i].set_ylabel('Average Scores')
    ax[i].set_title(titles[i])
    ax[i].set_xticks(x)
    ax[i].set_xticklabels(labels)
    ax[i].set_xlabel('Race/Ethnicity')
    ax[i].legend()

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height().round(2)
            ax[i].annotate('{0:.2f}'.format(height),
                           xy=(rect.get_x() + rect.get_width() / 2, height),
                           xytext=(0, 3),  # 3 points vertical offset
                           textcoords="offset points",
                           ha='center', va='bottom')
    autolabel(rects1)
    autolabel(rects2)
fig.savefig('output/output.png')
