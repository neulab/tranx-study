# Example code, write your program here
import matplotlib.pyplot as plt
import numpy as np

def autolabel(rects, idx):
    for rect in rects:
        height = rect.get_height()
        ax[idx].annotate('{:0.2f}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

data = []
with open('StudentsPerformance.csv') as fin:
    for idx, line in enumerate(fin):
        if idx == 0:
            continue
        tmp = line.strip().split(',')
        gender = tmp[0].strip('\"')
        group = tmp[1].split()[1].strip('\"')
        score = [float(tmp[-3].strip('\"')), float(tmp[-2].strip('\"')), float(tmp[-1].strip('\"'))]
        data.append([gender, group, score])

labels = ['A', 'B', 'C', 'D', 'E']
x = np.arange(len(labels))
width = 0.35
fig, ax = plt.subplots(1, 3, figsize=(20, 6))
fig.suptitle('Scores by race/ethnicity and gender')
for idx, subj in enumerate(['Math', 'Reading', 'Writing']):
    male = []
    female = []
    for label in labels:
        m_tot = m_cnt = f_tot = f_cnt = 0
        for rec in data:
            if rec[0] == 'male' and rec[1] == label:
                m_tot += rec[2][idx]
                m_cnt += 1
            if rec[0] == 'female' and rec[1] == label:
                f_tot += rec[2][idx]
                f_cnt += 1
        male.append(m_tot/m_cnt)
        female.append(f_tot/f_cnt)

    rects1 = ax[idx].bar(x - width / 2, male, width, label='Male')
    rects2 = ax[idx].bar(x + width / 2, female, width, label='Female')
    ax[idx].set_ylabel('Average Scores')
    ax[idx].set_xlabel('Race/Ethnicity')
    ax[idx].set_title(subj)
    ax[idx].set_xticks(x)
    ax[idx].set_xticklabels(labels)
    ax[idx].legend()

    autolabel(rects1, idx)
    autolabel(rects2, idx)

plt.savefig('grouped_scores.png')
