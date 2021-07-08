# Example code, write your program here
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

data = pd.read_csv('StudentsPerformance.csv')
gk = data.groupby('race/ethnicity')

#Group A
groupA = gk.get_group('group A')
Math_A = groupA['math score'].sum()
Reading_A = groupA['reading score'].sum()
Writing_A = groupA['writing score'].sum()
genderA = groupA.groupby('gender')
groupA_M = genderA.get_group('male')
groupA_F = genderA.get_group('female')

#Math
Math_AM = (groupA_M['math score'].sum())/53
Math_AF = (groupA_F['math score'].sum())/36
#Reading
Reading_AM = (groupA_M['reading score'].sum())/53
Reading_AF = (groupA_F['reading score'].sum())/36
#Writing
Writing_AM = (groupA_M['writing score'].sum())/53
Writing_AF = (groupA_F['writing score'].sum())/36
#Group B
groupB = gk.get_group('group B')
Math_B = groupB['math score'].sum()
Reading_B = groupB['reading score'].sum()
Writing_B = groupB['writing score'].sum()
genderB = groupB.groupby('gender')
groupB_M = genderB.get_group('male')
groupB_F = genderB.get_group('female')

#Math
Math_BM = (groupB_M['math score'].sum())/86
Math_BF = (groupB_F['math score'].sum())/104
#Reading
Reading_BM = (groupB_M['reading score'].sum())/86
Reading_BF = (groupB_F['reading score'].sum())/104
#Writing
Writing_BM = (groupB_M['writing score'].sum())/86
Writing_BF = (groupB_F['writing score'].sum())/104
#Group C
groupC = gk.get_group('group C')
Math_C = groupC['math score'].sum()
Reading_C = groupC['reading score'].sum()
Writing_C = groupC['writing score'].sum()
genderC = groupC.groupby('gender')
groupC_M = genderC.get_group('male')
groupC_F = genderC.get_group('female')
#Math
Math_CM = (groupC_M['math score'].sum())/139
Math_CF = (groupC_F['math score'].sum())/180
#Reading
Reading_CM = (groupC_M['reading score'].sum())/139
Reading_CF = (groupC_F['reading score'].sum())/180
#Writing
Writing_CM = (groupC_M['writing score'].sum())/139
Writing_CF = (groupC_F['writing score'].sum())/180
#Group D
groupD = gk.get_group('group D')
Math_D = groupD['math score'].sum()
Reading_D = groupD['reading score'].sum()
Writing_D = groupD['writing score'].sum()
genderD = groupD.groupby('gender')
groupD_M = genderD.get_group('male')
groupD_F = genderD.get_group('female')
#Math
Math_DM = (groupD_M['math score'].sum())/133
Math_DF = (groupD_F['math score'].sum())/129
#Reading
Reading_DM = (groupD_M['reading score'].sum())/133
Reading_DF = (groupD_F['reading score'].sum())/129
#Writing
Writing_DM = (groupD_M['writing score'].sum())/133
Writing_DF = (groupD_F['writing score'].sum())/129
#Group E
groupE = gk.get_group('group E')
Math_E = groupE['math score'].sum()
Reading_E = groupE['reading score'].sum()
Writing_E = groupE['writing score'].sum()
genderE = groupE.groupby('gender')
groupE_M = genderE.get_group('male')
groupE_F = genderE.get_group('female')
#Math
Math_EM = (groupE_M['math score'].sum())/71
Math_EF = (groupE_F['math score'].sum())/69
#Reading
Reading_EM = (groupE_M['reading score'].sum())/71
Reading_EF = (groupE_F['reading score'].sum())/69
#Writing
Writing_EM = (groupE_M['writing score'].sum())/71
Writing_EF = (groupE_F['writing score'].sum())/69

fig, (df, df1, df2) = plt.subplots(1, 3, figsize=(20, 6))

plt.subplot(1, 3, 1)
df = pd.DataFrame([['Male', 'A', Math_AM], ['Male', 'B', Math_BM], ['Male', 'C', Math_CM], ['Male', 'D', Math_DM], ['Male', 'E', Math_EM], ['Female', 'A', Math_AF], ['Female', 'B', Math_BF], ['Female', 'C', Math_CF], ['Female', 'D', Math_DF], ['Female', 'E', Math_EF]], columns=['', 'race/ethnicity', 'value'])
df.pivot('race/ethnicity', '', 'value').plot(kind='bar', width=.75, ax=plt.gca())
plt.ylabel('Average Scores')
plt.xlabel('Race/Ethnicity')
plt.title('Math')

plt.subplot(1, 3, 2)
df1 = pd.DataFrame([['Male', 'A', Reading_AM], ['Male', 'B', Reading_BM], ['Male', 'C', Reading_CM], ['Male', 'D', Reading_DM], ['Male', 'E', Reading_EM], ['Female', 'A', Reading_AF], ['Female', 'B', Reading_BF], ['Female', 'C', Reading_CF], ['Female', 'D', Reading_DF], ['Female', 'E', Reading_EF]], columns=['', 'race/ethnicity', 'value'])
df1.pivot('race/ethnicity', '', 'value').plot(kind='bar', width=.75, ax=plt.gca())
plt.ylabel('Average Scores')
plt.xlabel('Race/Ethnicity')
plt.title('Reading')

plt.subplot(1, 3, 3)
df2 = pd.DataFrame([['Male', 'A', Writing_AM], ['Male', 'B', Writing_BM], ['Male', 'C', Writing_CM], ['Male', 'D', Writing_DM], ['Male', 'E', Writing_EM], ['Female', 'A', Writing_AF], ['Female', 'B', Writing_BF], ['Female', 'C', Writing_CF], ['Female', 'D', Writing_DF], ['Female', 'E', Writing_EF]], columns=['', 'race/ethnicity', 'value'])
df2.pivot('race/ethnicity', '', 'value').plot(kind='bar', width=.75, ax=plt.gca())
plt.ylabel('Average Scores')
plt.xlabel('Race/Ethnicity')
plt.title('Writing')

fig.suptitle("Scores by race/ethnicity and gender")

plt.savefig('grouped_scores.png')
plt.savefig('output/grouped_scores.png')