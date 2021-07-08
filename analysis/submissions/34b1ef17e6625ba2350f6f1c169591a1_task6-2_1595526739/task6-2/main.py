# Example code, write your program here
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import numpy as np
import pandas as pd

data = np.loadtxt("dataset/wine.data", delimiter=',')
label = data[:, 0]
feature = data[:, 1:]
for C in [0.01, 0.1, 1, 10, 100]:
    clf = LogisticRegression(random_state=0, C=C, max_iter=10000)
    scores = cross_val_score(clf, feature, label, cv=5, scoring='accuracy')
    print("C="+str(C), "Mean Accuracy:", round(scores.mean(), 2))
