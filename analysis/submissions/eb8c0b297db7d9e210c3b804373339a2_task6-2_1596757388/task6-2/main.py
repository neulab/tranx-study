# Example code, write your program here

# Import library
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Import panda library
import pandas as pd

# Wine names definition
wine_names = ['Class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium',
         'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins',
         'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']

# Pandas dataframe
wine_data = pd.read_csv('dataset/wine.data', names= wine_names)

# Dataframe definition
wine_df = pd.DataFrame(wine_data)

# Index begin in 0
wine_df.Class = wine_df.Class - 1

# Y vector definition
Y = wine_df.loc[:, 'Class'].values

# X vector definition (Considering all columns are expected results)
X = wine_df.loc[:, 'Alcohol':'Proline'].values

# Regularization parameters
c_list = [.01, 0.1, 1, 10, 100]

# Loop over regularization parameters
for c in c_list:

    # Define the train and test
    train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=c, random_state=0)

    # Perform the logistical regression
    sol = LogisticRegression( solver='lbfgs', multi_class='multinomial', max_iter= 100000 )

    # Fitting
    sol.fit(train_X, train_Y)

    # Score
    acc = sol.score(test_X, test_Y)

    # Print results
    print('C = ' + str(c) + ' - ' + 'Mean accuracy:' + '{:.2f}'.format(acc))
