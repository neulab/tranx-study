# Example code, write your program here
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("StudentsPerformance.csv")
df['race/ethnicity']=df['race/ethnicity'].str.replace("group"," ")
df['Average score math']=df[['math score']].apply(lambda x:x.mean())
print(df)

fig,axs=plt.subplots(1,3,figsize=(20,6))

plt.subplot(131)
plt.title("math")
sns.barplot(hue='gender',y='math score', x='race/ethnicity',data=df)

plt.subplot(132)
plt.title('Reading')
sns.barplot(hue='gender',y='reading score', x='race/ethnicity',data=df)

plt.subplot(133)
plt.title('writing')
sns.barplot(hue='gender',y='writing score', x='race/ethnicity',data=df)

plt.savefig('grouped_scores')