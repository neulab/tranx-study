import pandas as pd
from sklearn.model_selection import train_test_split, KFold
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt
import os

#Load in data file
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'dataset/wine.data')

#Store data as df
df = pd.read_csv(file_path)

#Specify X and y
y = df.c1
df.drop('c1', axis='columns',inplace=True)
X = df

#Create test-train split
X_test, X_train, y_test, y_train = train_test_split(X,y,train_size=0.2)

#Create model, with loop used to check different C values and print scores
for c in [0.01, 0.1, 1, 10, 100]:
    model = LogisticRegression(C=c, random_state=0, solver='lbfgs',max_iter=20000)
    model.fit(X_train, y_train)
    score = round(model.score(X_test, y_test), 2)
    print('C=' + str(c) + ' Mean Accuracy: ' + str(score))
