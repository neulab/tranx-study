import pandas as pd
from sklearn.linear_model import LogisticRegressionCV
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv('./dataset/wine.data', header=None)
x, y = data.iloc[:, 1:], data[0]
x  = MinMaxScaler().fit_transform(x)
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0, test_size= 0.3)
for c in [0.01, 0.1, 1, 10, 100]:
    lr = LogisticRegressionCV(Cs=[c],solver='lbfgs', multi_class='multinomial', random_state=0)
    lr.fit(x_train, y_train.ravel())
    y_train_pred = lr.predict(x_train)
    y_test_pred = lr.predict(x_test)
    print('c=%.2f \tMean Accuracy: ' % lr.C_[0], "{:.2f}".format(accuracy_score(y_test, y_test_pred)*100.0))