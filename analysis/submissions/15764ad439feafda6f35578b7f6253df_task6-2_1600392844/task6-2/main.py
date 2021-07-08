# Example code, write your program here
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

dataset = pd.read_csv("dataset/wine.data", delimiter=",")
y = dataset.iloc[:, 0]
x = dataset.iloc[:, 1:]
train_, test_, train_lbl, test_lbl = train_test_split(
    x, y, test_size=1/5, random_state=0)
model = LogisticRegression(solver = 'lbfgs', max_iter= 5000, random_state=0, C=0.01)
model.fit(train_, train_lbl)
y_pred = model.predict(test_)
count_misclassified = (test_lbl != y_pred).sum()
accuracy = metrics.accuracy_score(test_lbl, y_pred)
print('C=0.01 Mean Accuracy: {:.2f}'.format(accuracy * 100))
model1 = LogisticRegression(solver = 'lbfgs', max_iter= 5000, random_state=0, C=0.1)
model1.fit(train_, train_lbl)
y_pred = model1.predict(test_)
count_misclassified = (test_lbl != y_pred).sum()
accuracy = metrics.accuracy_score(test_lbl, y_pred)
print('C=0.1 Mean Accuracy: {:.2f}'.format(accuracy * 100))
model2 = LogisticRegression(solver = 'lbfgs', max_iter= 5000, random_state=0, C=1)
model2.fit(train_, train_lbl)
y_pred = model2.predict(test_)
count_misclassified = (test_lbl != y_pred).sum()
accuracy = metrics.accuracy_score(test_lbl, y_pred)
print('C=1 Mean Accuracy: {:.2f}'.format(accuracy * 100))
model3 = LogisticRegression(solver = 'lbfgs', max_iter= 5000, random_state=0, C=10)
model3.fit(train_, train_lbl)
y_pred = model3.predict(test_)
count_misclassified = (test_lbl != y_pred).sum()
accuracy = metrics.accuracy_score(test_lbl, y_pred)
print('C=10 Mean Accuracy: {:.2f}'.format(accuracy * 100))
model4 = LogisticRegression(solver = 'lbfgs', max_iter= 50000, random_state=0, C=100)
model4.fit(train_, train_lbl)
y_pred = model4.predict(test_)
count_misclassified = (test_lbl != y_pred).sum()
accuracy = metrics.accuracy_score(test_lbl, y_pred)
print('C=100 Mean Accuracy: {:.2f}'.format(accuracy * 100))