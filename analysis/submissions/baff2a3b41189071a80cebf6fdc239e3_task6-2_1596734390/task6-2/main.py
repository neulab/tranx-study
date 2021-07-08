from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.linear_model import LogisticRegressionCV as lr

from sklearn import preprocessing
import numpy as np


c = [[0.01], [0.10], 1, 10, 100]
ds = load_wine()
x_train, x_test, y_train, y_test = train_test_split(ds['data'],
                                                    ds['target'],random_state=0)
x_train_scaled = preprocessing.scale(x_train)
x_test_scaled = preprocessing.scale(x_test)


for i in c:
    model = lr(Cs=i, solver='lbfgs', random_state=0).fit(X=x_train_scaled, y=y_train)
    cvs = cross_val_score(model, x_test_scaled, y_test,)
    print('C=', np.mean(i), 'Mean Accuracy:', np.round(np.mean(np.array(cvs)*100), decimals=2))
