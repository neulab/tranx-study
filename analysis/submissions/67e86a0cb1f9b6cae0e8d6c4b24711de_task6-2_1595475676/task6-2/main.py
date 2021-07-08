# Example code, write your program here
import numpy
data = numpy.loadtxt('dataset/wine.data',delimiter=',')
X = data[:,1:]
y = data[:,0]
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split,cross_validate,KFold
from sklearn.metrics import accuracy_score
for C in [0.01,0.1,1,10,   100]:
    model = LogisticRegression(C=C,max_iter=10000,multi_class='multinomial')
    cv=KFold(random_state=0)
    accs=0.
    for train_index, test_index in cv.split(X,y):
        X_train, y_train = X[train_index], y[train_index]
        X_test, y_test  =X[test_index],y[test_index]
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        acc = accuracy_score(y_test,pred)
        accs+=acc
    print('C={:.2f} Mean Accuracy: {:.2f}'.format(C, accs/5.*100))