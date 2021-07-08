# Example code, write your program here
import pandas as pd
import numpy as np

from sklearn import linear_model, metrics
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import metrics

wineData = pd.read_csv('dataset/wine.data', names=['Class', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'f13'])
print(wineData)
train_x, test_x, train_y, test_y = train_test_split(wineData[['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'f13']], wineData['Class'], train_size=0.7, random_state=0)
mulLR = linear_model.LogisticRegression(multi_class='multinomial', solver='lbfgs').fit(train_x, train_y)

for c in [0.01, 0.1, 1, 10, 100]:
    acc = cross_val_score(mulLR, train_x, train_y, cv=c, scoring='accuracy').mean()
    print('c='+c+' Mean Accuracy: '+acc)
