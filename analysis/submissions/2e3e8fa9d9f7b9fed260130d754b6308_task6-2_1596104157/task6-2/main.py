# Example code, write your program here
import numpy as np
import pandas as pd
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn import metrics
name= ['class','Alcohol', 'Malic acid','Ash','Alcalinity of ash' ,'Magnesium',
       'Total phenols','Flavanoids''Nonflavanoid phenols','Proanthocyanins',
       'Color','intensity','Hue','OD280/OD315 of diluted wines','Proline']
data=pd.read_csv('dataset/wine.data',names=name)
X=data[name[1:]]
y=data[['class']]
clf = LogisticRegression(random_state=0, multi_class='multinomial', solver='lbfgs')
scores = cross_val_score(clf, X, y, cv=5)
C = [0.01, 0.1, 1, 10, 100]
for i in range(5):
       print('c={} {:.2f}%'.format(C[i],scores[i]*100))
