# Example code, write your program here

# Import pandas library
import pandas as pd

# Import matlib plot
import matplotlib.pyplot as plt

# Import numpy
import numpy as np

# File name
fileName = 'StudentsPerformance.csv'

# Open file on pandas
fileContent = pd.read_csv(fileName)

# Groups
groupA = fileContent[fileContent['race/ethnicity'] == 'group A']
groupB = fileContent[fileContent['race/ethnicity'] == 'group B']
groupC = fileContent[fileContent['race/ethnicity'] == 'group C']
groupD = fileContent[fileContent['race/ethnicity'] == 'group D']
groupE = fileContent[fileContent['race/ethnicity'] == 'group E']

# Separate groups into male and female
groupAMale   = groupA[groupA['gender'] == 'male']
groupAFemale = groupA[groupA['gender'] == 'female']
groupBMale   = groupB[groupB['gender'] == 'male']
groupBFemale = groupB[groupB['gender'] == 'female']
groupCMale   = groupC[groupC['gender'] == 'male']
groupCFemale = groupC[groupC['gender'] == 'female']
groupDMale   = groupD[groupD['gender'] == 'male']
groupDFemale = groupD[groupD['gender'] == 'female']
groupEMale   = groupE[groupE['gender'] == 'male']
groupEFemale = groupE[groupE['gender'] == 'female']

# Labels for the graphics
labels = ['A', 'B', 'C', 'D', 'E']

# First graph (left) - Male
math_male_A = groupAMale['math score'].mean()
math_male_B = groupBMale['math score'].mean()
math_male_C = groupCMale['math score'].mean()
math_male_D = groupDMale['math score'].mean()
math_male_E = groupEMale['math score'].mean()
math_male = [math_male_A, math_male_B, math_male_C, math_male_D, math_male_E]

# First graph (left) - Female
math_female_A = groupAFemale['math score'].mean()
math_female_B = groupBFemale['math score'].mean()
math_female_C = groupCFemale['math score'].mean()
math_female_D = groupDFemale['math score'].mean()
math_female_E = groupEFemale['math score'].mean()
math_female = [math_female_A, math_female_B, math_female_C, math_female_D, math_female_E]

# Second graph (left) - Male
reading_male_A = groupAMale['reading score'].mean()
reading_male_B = groupBMale['reading score'].mean()
reading_male_C = groupCMale['reading score'].mean()
reading_male_D = groupDMale['reading score'].mean()
reading_male_E = groupEMale['reading score'].mean()
reading_male = [reading_male_A, reading_male_B, reading_male_C, reading_male_D, reading_male_E]

# Second graph (left) - Female
reading_female_A = groupAFemale['reading score'].mean()
reading_female_B = groupBFemale['reading score'].mean()
reading_female_C = groupCFemale['reading score'].mean()
reading_female_D = groupDFemale['reading score'].mean()
reading_female_E = groupEFemale['reading score'].mean()
reading_female = [reading_female_A, reading_female_B, reading_female_C, reading_female_D, reading_female_E]

# Third graph (left) - Male
writing_male_A = groupAMale['writing score'].mean()
writing_male_B = groupBMale['writing score'].mean()
writing_male_C = groupCMale['writing score'].mean()
writing_male_D = groupDMale['writing score'].mean()
writing_male_E = groupEMale['writing score'].mean()
writing_male = [writing_male_A, writing_male_B, writing_male_C, writing_male_D, writing_male_E]

# Third graph (left) - Female
writing_female_A = groupAFemale['writing score'].mean()
writing_female_B = groupBFemale['writing score'].mean()
writing_female_C = groupCFemale['writing score'].mean()
writing_female_D = groupDFemale['writing score'].mean()
writing_female_E = groupEFemale['writing score'].mean()
writing_female = [writing_female_A, writing_female_B, writing_female_C, writing_female_D, writing_female_E]

# Bar width
barWidth = 0.35

# Bar positions
r1 = np.arange(len(math_male))
r2 = [x + barWidth for x in r1]

# Subplots definition
fig, axs = plt.subplots(1, 3, figsize=(20, 6))

# Title definition
fig.suptitle("Scores by race/ethnicity and gender")

# Plot - Math
rect1M = axs[0].bar(r1, math_male, width=barWidth, label='Male')
rect2M = axs[0].bar(r2, math_female, width=barWidth, label='Female')
axs[0].set_title('Math')
axs[0].set_xlabel('Race/Ethnicity')
axs[0].set_ylabel('Average score')
axs[0].legend(loc='upper left')

# Plot - Reading
rect1R = axs[1].bar(r1, reading_male, width=barWidth, label='Male')
rect2R = axs[1].bar(r2, reading_female, width=barWidth, label='Female')
axs[1].set_title('Reading')
axs[1].set_xlabel('Race/Ethnicity')
axs[1].set_ylabel('Average score')
axs[1].legend(loc='upper left')

# Plot - Writing
rect1W = axs[2].bar(r1, writing_male, width=barWidth, label='Male')
rect2W = axs[2].bar(r2, writing_female, width=barWidth, label='Female')
axs[2].set_title('Writing')
axs[2].set_xlabel('Race/Ethnicity')
axs[2].set_ylabel('Average score')
axs[2].legend(loc='upper left')

# Set X label
plt.setp(axs, xticks=[r + barWidth/2 for r in range(len(r1))], xticklabels=labels)


# Function definition for autolabel
def auto_label(rects, index):

    # Loop over bars
    for rect in rects:

        # Height definition
        height = rect.get_height()

        axs[index].annotate('{:.2f}'.format(height),
                            xy=(rect.get_x()+rect.get_width()/2, height),
                            xytext=(0, 3),
                            textcoords="offset points",
                            ha='center', va='bottom')


# Auto legend
auto_label(rect1M, 0)
auto_label(rect2M, 0)
auto_label(rect1R, 1)
auto_label(rect2R, 1)
auto_label(rect1W, 2)
auto_label(rect2W, 2)

# Legend
plt.legend()

# Save plot
plt.savefig('grouped_scores.png')