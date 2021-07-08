# Example code, write your program here
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('StudentsPerformance.csv')
barWidth = 0.35

male = [df[(df['race/ethnicity'] == 'group A') & (df['gender'] == 'male')]['math score'].mean(),
df[(df['race/ethnicity'] == 'group B') & (df['gender'] == 'male')]['math score'].mean(),
df[(df['race/ethnicity'] == 'group C') & (df['gender'] == 'male')]['math score'].mean()]

female = [df[(df['race/ethnicity'] == 'group A') & (df['gender'] == 'female')]['math score'].mean(),
df[(df['race/ethnicity'] == 'group B') & (df['gender'] == 'female')]['math score'].mean(),
df[(df['race/ethnicity'] == 'group C') & (df['gender'] == 'female')]['math score'].mean()]


plt.figure(figsize=(20,6))
plt.title('Scores by race/ethnicity and gender')

plt.subplot(131)
plt.title('Math')
# Make the plot
r1 = np.arange(len(male))
r2 = [x + barWidth for x in r1]
plt.bar(r1, male, width=barWidth, label='male')
plt.bar(r2, female, width=barWidth, label='female')
plt.xlabel('Race/Ethnicity')
plt.ylabel('Average Scores')
plt.xticks([r + barWidth for r in range(len(male))], ['A', 'B', 'C'])
plt.legend()


plt.subplot(132)
male = [df[(df['race/ethnicity'] == 'group A') & (df['gender'] == 'male')]['reading score'].mean(),
df[(df['race/ethnicity'] == 'group B') & (df['gender'] == 'male')]['reading score'].mean(),
df[(df['race/ethnicity'] == 'group C') & (df['gender'] == 'male')]['reading score'].mean()]

female = [df[(df['race/ethnicity'] == 'group A') & (df['gender'] == 'female')]['reading score'].mean(),
df[(df['race/ethnicity'] == 'group B') & (df['gender'] == 'female')]['reading score'].mean(),
df[(df['race/ethnicity'] == 'group C') & (df['gender'] == 'female')]['reading score'].mean()]
plt.title('Reading')
# Make the plot
r1 = np.arange(len(male))
r2 = [x + barWidth for x in r1]
plt.bar(r1, male, width=barWidth, label='male')
plt.bar(r2, female, width=barWidth, label='female')
plt.xlabel('Race/Ethnicity')
plt.ylabel('Average Scores')
plt.xticks([r + barWidth for r in range(len(male))], ['A', 'B', 'C'])
plt.legend()


plt.subplot(133)
male = [df[(df['race/ethnicity'] == 'group A') & (df['gender'] == 'male')]['writing score'].mean(),
df[(df['race/ethnicity'] == 'group B') & (df['gender'] == 'male')]['writing score'].mean(),
df[(df['race/ethnicity'] == 'group C') & (df['gender'] == 'male')]['writing score'].mean()]

female = [df[(df['race/ethnicity'] == 'group A') & (df['gender'] == 'female')]['writing score'].mean(),
df[(df['race/ethnicity'] == 'group B') & (df['gender'] == 'female')]['writing score'].mean(),
df[(df['race/ethnicity'] == 'group C') & (df['gender'] == 'female')]['writing score'].mean()]
plt.title('Writing')
# Make the plot
r1 = np.arange(len(male))
r2 = [x + barWidth for x in r1]
plt.bar(r1, male, width=barWidth, label='male')
plt.bar(r2, female, width=barWidth, label='female')
plt.xlabel('Race/Ethnicity')
plt.ylabel('Average Scores')
plt.xticks([r + barWidth for r in range(len(male))], ['A', 'B', 'C'])
plt.legend()

plt.savefig('grouped_scores.png')




