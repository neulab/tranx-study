# Example code, write your program here
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn import model_selection

df = pd.read_csv('dataset/wine.data', index_col=False)
print(df)
X = df.iloc[:, 1:]
y = df.iloc[:, 0]

for c in [0.01, 0.1, 1, 10, 100]:
    clf = LogisticRegression(C=c, random_state=0, solver='lbfgs').fit(X, y)
    score = model_selection.cross_val_score(clf, X, y, cv=5)
    print('C=', c, 'Mean Accuracy: ', round(score.mean()*100, 2))



