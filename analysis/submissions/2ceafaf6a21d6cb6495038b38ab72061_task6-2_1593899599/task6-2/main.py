# Example code, write your program here
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate
from sklearn.model_selection import cross_val_score
import numpy as np
import random
random.seed(0)
np.random.seed(0)


# load data
X, y = [], []

with open("dataset/wine.data", "r") as f:
    for line in f:
        tks = line.strip().split(",")
        X.append(np.array(tks[1:]))
        y.append(np.array(tks[0]))
X = np.array(X, dtype=np.float)
y = np.array(y, dtype=np.float)
print(X.shape, y.shape)

for c in (0.01, 0.1, 1, 10, 100):
    regressor = LogisticRegression(C=c, max_iter=2000)
    scores = cross_val_score(regressor, X, y, cv=5)
    print(f"C={c} Mean Accuracy={np.mean(scores) :.2f}")
