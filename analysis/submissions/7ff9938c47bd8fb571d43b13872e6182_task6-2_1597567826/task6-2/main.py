# Example code, write your program here
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


names=['names', 'Alcohol',
 	'Malicacid',
 	'Ash',
	'ash ',
 	'Magnesium',
	'Total_phenols',
 	'Flavanoids',
 	'Nonflavanoid',
 	'Proanthocyanins',
	'Colorintensity',
 	'Hue',
 	'OD280/OD315',
 	'Proline']
Dataset=pd.read_csv('dataset/wine.data',names=names)

Y=Dataset.loc[:,'names']
X=Dataset.iloc[:,1:-1]

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=5,random_state=0)

scalar=StandardScaler()
X_train=scalar.fit_transform(X_train)
X_test=scalar.fit_transform(X_test)
C={0.01,0.1,1,10,100}
for c in C:
    regressor=LogisticRegression(solver='lbfgs' ,C=c,multi_class='multinomial',max_iter=1000)
    regressor.fit(X_train,Y_train)
    print("score for c= ",c," ====>  ",regressor.score(X_test,Y_test))
