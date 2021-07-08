# Example code, write your program here
import os

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.linear_model import LogisticRegression

df = pd.read_csv(os.path.join("dataset","wine.data"),header=None)
df.rename(columns={
     0:'Id'
    ,1: 'Alcohol'
 	,2: 'Malic acid'
 	,3: 'Ash'
	,4: 'Alcalinity of ash'
 	,5: 'Magnesium'
	,6: 'Total_phenols'
 	,7: 'Flavanoids'
 	,8:'Nonflavanoid_phenols'
 	,9: 'Proanthocyanins'
	,10:'Color_intensity'
 	,11:'Hue'
 	,12:'OD280_OD315'
	,13: 'Proline'
}, inplace=True)
Y = df['Id']
X = df.drop('Id',axis=1)
#d = pd.read_csv(os.path.join("dataset","wine.data"),header=None)
#X = d.drop(1,axis=1)
#Y = df.iloc[:,:1]

X_train, X_test,Y_train, Y_test = train_test_split(X,Y,test_size=0.3, random_state=0)
lR= LogisticRegression(solver='lbfgs',max_iter=10000,random_state=0)
lR = lR.fit(X_train,Y_train)
scores = lR.score(X_test, Y_test)
print(("Accuracy  {:.2f}".format(scores*100)))
#kf = KFold(n_splits=5,random_state=0,shuffle=True)
	#scores = cross_val_score(lR,X_train,Y_train,cv=kf,scoring="accuracy")
#scores = cross_val_score(LogisticRegression(),X,Y,cv=kf,scoring="accuracy")
#print(scores)

