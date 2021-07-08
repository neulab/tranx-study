import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('StudentsPerformance.csv')
letters = ['A','B','C','D','E']
fig, ax = plt.subplots(1,3,figsize=(20,6),dpi=100)
fig.suptitle('Scores by race/ethnicity and gender')

ax[0].bar(letters,pd.DataFrame(data.loc[data['gender'] == 'male']).groupby(['race/ethnicity'])['math score'].mean(),-.35,align='edge',label='Male')
ax[0].bar(letters,pd.DataFrame(data.loc[data['gender'] == 'female']).groupby(['race/ethnicity'])['math score'].mean(),.35,align='edge',label='Female')
ax[0].title.set_text("Math")
ax[0].set(xlabel="Race/Ethnicity",ylabel='Average Scores')
ax[0].legend(loc='upper left')

ax[1].bar(letters,pd.DataFrame(data.loc[data['gender'] == 'male']).groupby(['race/ethnicity'])['reading score'].mean(),-.35,align='edge',label='Male')
ax[1].bar(letters,pd.DataFrame(data.loc[data['gender'] == 'female']).groupby(['race/ethnicity'])['reading score'].mean(),.35,align='edge',label='Female')
ax[1].title.set_text("Reading")
ax[1].set(xlabel="Race/Ethnicity",ylabel='Average Scores')
ax[1].legend(loc='upper left')

ax[2].bar(letters,pd.DataFrame(data.loc[data['gender'] == 'male']).groupby(['race/ethnicity'])['writing score'].mean(),-.35,align='edge',label='Male')
ax[2].bar(letters,pd.DataFrame(data.loc[data['gender'] == 'female']).groupby(['race/ethnicity'])['writing score'].mean(),.35,align='edge',label='Female')
ax[2].title.set_text("Writing")
ax[2].set(xlabel="Race/Ethnicity",ylabel='Average Scores')
ax[2].legend(loc='upper left')
for i in range(0,3):
    for rect in ax[i].patches:
        hgt = rect.get_height()
        yp = rect.get_y() + hgt + 3
        ax[i].text(rect.get_x() + rect.get_width()/2,yp,'%.2f' % hgt, ha='center',va='top')
plt.savefig("output/grouped_scores.png")