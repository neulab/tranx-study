# Example code, write your program here
import numpy as np
from sklearn.linear_model import *
import warnings
warnings.filterwarnings('ignore')

data = np.genfromtxt('dataset/wine.data', delimiter=',')
y = data[:, 0]
X = data[:, 1:]
Cs = [0.01, 0.1, 1, 10, 100]

model = LogisticRegressionCV(Cs=Cs, cv=5, random_state=0, max_iter=200, solver='lbfgs')
model.fit(X, y)

# (fold, Cs)
for C, acc in zip(Cs, model.scores_[1].mean(0)):
    print("C={0:4}     Mean Accuracy: {1:.2f}".format(C, acc * 100.0))