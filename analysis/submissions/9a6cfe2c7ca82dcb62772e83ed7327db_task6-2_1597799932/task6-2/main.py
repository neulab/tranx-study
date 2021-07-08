# Example code, write your program here
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import  r2_score
data = pd.read_csv("dataset/wine.data")
y = data.iloc[:, 0]
X = data.iloc[:, 1:]

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2,
                                                    random_state=123,
                                                    stratify=y)

scaler = preprocessing.StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
for i in range(5):
    C= [0.01, 0.1, 1.00, 10.0, 100]
    pipeline = make_pipeline(preprocessing.StandardScaler(),
                             LogisticRegression(random_state=0,C=C[i]))

    hyperparameters = {'logisticregression__C': [0.01, 0.1, 1, 10, 100]}
    clf = GridSearchCV(pipeline, hyperparameters, cv=5)


    clf.fit(X_train, y_train)
    pred = clf.predict(X_test)
    print("C=",C[i],"   Mean accuracy:",("{:.2f}".format(r2_score(y_test, pred)*100)))

