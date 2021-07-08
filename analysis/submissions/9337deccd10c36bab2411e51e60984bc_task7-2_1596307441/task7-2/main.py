# Example code, write your program here
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('StudentsPerformance.csv').drop(['parental level of education', 'lunch', 'test preparation course'], axis = 1)
data = data.groupby(['race/ethnicity', 'gender']).mean()

fig = plt.gcf()
fig.set_size_inches(20, 6)
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)
ax = [ax1, ax2, ax3]
params = ['math score', 'reading score', 'writing score']
labels = ['Math', 'Reading', 'Writing']
fig.suptitle('Scores by race/ethnicity and gender')
for i in range(3):
    plot_data = data[params[i]].unstack()
    plot_data.columns = [c[0].upper() + c[1:] for c in plot_data.columns]
    plot_data.plot(kind = 'bar', ax = ax[i], title = labels[i])
    ax[i].set_ylabel('Average Scores')
    ax[i].set_xlabel('Race/Ethnicity')
    for p in ax[i].patches:
        ax[i].annotate('{:.2f}'.format(float(p.get_height())), (p.get_x(), p.get_height()))
fig.savefig('grouped_scores.png', bbox_inches = 'tight')