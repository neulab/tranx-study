import pandas as pd
import matplotlib
matplotlib.rcParams.update({'font.size': 14})
matplotlib.rcParams.update({'figure.figsize': [8, 5.8]})

import matplotlib.pyplot as plt


users = pd.read_csv('data/users.csv')

actual_users = pd.read_csv('data/completed_time_merged.csv')


completed_users = set(actual_users['user'])

users = users[users['user'].isin(completed_users)]

print(users.groupby('occupation').count())

print(len(completed_users))

# python experience
fig, ax = plt.subplots()

data = users.groupby(['python_experience']).count()

print(data)
x = [1, 2, 3, 4, 5]
y = [0, 0, 6, 23, 2]
total = sum(y)

def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()

        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{} ({:.2f}%)'.format(height, height/total * 100), ha=ha[xpos], va='bottom')

rects = ax.bar(x, y, color='lightblue')
autolabel(rects)

ax.set_ylabel('Count')
plt.savefig('figures/python_exp.pdf', bbox_inches='tight')

for i in range(1, 8):
    fig, ax = plt.subplots()

    data = users.groupby(['task'+str(i)]).count().to_dict()['user']

    y = []
    for item in x:
        if item in data:
            y.append(data[item])
        else:
            y.append(0)


    def autolabel(rects, xpos='center'):
        """
        Attach a text label above each bar in *rects*, displaying its height.

        *xpos* indicates which side to place the text w.r.t. the center of
        the bar. It can be one of the following {'center', 'right', 'left'}.
        """

        xpos = xpos.lower()  # normalize the case of the parameter
        ha = {'center': 'center', 'right': 'left', 'left': 'right'}
        offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

        for rect in rects:
            height = rect.get_height()

            ax.text(rect.get_x() + rect.get_width() * offset[xpos], 1.01 * height,
                    '{} ({:.2f}%)'.format(height, height / total * 100), ha=ha[xpos], va='bottom')
    rects = ax.bar(x, y, color='lightblue')
    autolabel(rects)

    ax.set_ylabel('Count')
    plt.savefig('figures/exp_{}.pdf'.format('task'+str(i)), bbox_inches='tight')


# plugin experience figure
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size': 14})
matplotlib.rcParams.update({'figure.figsize': [14.4, 5.3]})


survey_responses = pd.read_csv('data/survey_responses.csv')
survey_responses['user'] = survey_responses.email.str.split('@').str[0]

survey_responses = survey_responses[survey_responses['user'].isin(completed_users)]

survey_responses = survey_responses.drop(columns=['Timestamp', 'email', 'contact'])
survey_responses = survey_responses.reset_index()
survey_responses = survey_responses.drop(columns=['index'])

survey_responses.to_csv('data/filtered_survey.csv')

print(survey_responses)

x = [1, 2, 3, 4, 5]
print(survey_responses.groupby('exp').count())
y = [0, 1, 15, 11, 4]

total = sum(y)
fig, ax = plt.subplots()

rects = ax.bar(x, y, color='lightblue')

def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()

        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{} ({:.2f}%)'.format(height, height/total * 100), ha=ha[xpos], va='bottom')


autolabel(rects)

ax.set_xlabel('Experience (1 - very bad, 5 - very good)')
ax.set_ylabel('Count')
plt.savefig('figures/survey_scores.pdf', bbox_inches='tight')
