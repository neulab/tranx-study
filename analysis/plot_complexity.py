import pandas as pd
### cc

import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

matplotlib.rcParams.update({'font.size': 14})
matplotlib.rcParams.update({'figure.figsize': [20.4, 5.8]})

df = pd.read_csv('data/complexity_scores_merged.csv')
print(df.columns)
df_all = df.copy()
nall = str(df_all['user'].count())
df_all['category'] = 'All (' + nall + ')'
df = pd.concat([df_all, df])
df = df.rename(columns={'cc': 'Cyclomatic Complexity'})
df = df.replace({'uses_plugin': {True: ' w/ plugin', False: ' w/o plugin'}})
ntask1 = str(df.loc[(df.category == 'task1'), 'category'].count())
ntask2 = str(df.loc[(df.category == 'task2'), 'category'].count())
ntask3 = str(df.loc[(df.category == 'task3'), 'category'].count())
ntask4 = str(df.loc[(df.category == 'task4'), 'category'].count())
ntask5 = str(df.loc[(df.category == 'task5'), 'category'].count())
ntask6 = str(df.loc[(df.category == 'task6'), 'category'].count())
ntask7 = str(df.loc[(df.category == 'task7'), 'category'].count())

df.loc[(df.category == 'task1'), 'category'] = 'Basic Python (' + ntask1 + ')'
df.loc[(df.category == 'task2'), 'category'] = 'File (' + ntask2 + ')'
df.loc[(df.category == 'task3'), 'category'] = 'OS (' + ntask3 + ')'
df.loc[(df.category == 'task4'), 'category'] = 'Web Scraping (' + ntask4 + ')'
df.loc[(df.category == 'task5'), 'category'] = 'Web Server &\nClient (' + ntask5 + ')'
df.loc[(df.category == 'task6'), 'category'] = 'Data Analysis &\nMachine Learning (' + ntask6 + ')'
df.loc[(df.category == 'task7'), 'category'] = 'Data\nVisualization (' + ntask7 + ')'

ax = sns.violinplot(x="category", y="Cyclomatic Complexity", hue="uses_plugin",
                    data=df, palette="muted", cut=0, split=True, inner='quartile',
                    order=['All (' + nall + ')', 'Basic Python (' + ntask1 + ')',
                           'File (' + ntask2 + ')', 'OS (' + ntask3 + ')',
                           'Web Scraping (' + ntask4 + ')',
                           'Web Server &\nClient (' + ntask5 + ')',
                           'Data Analysis &\nMachine Learning (' + ntask6 + ')',
                           'Data\nVisualization (' + ntask7 + ')'])
sns.despine()

ax.set(ylim=(None, 20))

ax.legend(loc='upper right', frameon=False)
plt.xlabel("")

plt.savefig('figures/complexity_violin.pdf', bbox_inches='tight')
