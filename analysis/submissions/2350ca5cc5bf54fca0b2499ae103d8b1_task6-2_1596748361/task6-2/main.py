# Example code, write your program here
from sklearn.linear_model import LogisticRegressionCV
import numpy as np

file = open('dataset/wine.data')
x = list()
y = list()
for line in file.readlines():
    x.append([float(value) for value in line.split(',')[1:]])
    y.append(int(line.split(',')[0]))
x = np.asarray(x)
y = np.asarray(y)
c_values = [0.01, 0.1, 1, 10]
# uncomment line 15 to print for c value 100: an abrupt stop occurs with TOTAL NO. of ITERATIONS REACHED LIMIT and output: 'C=100 Mean aCCURACY: 100.00'
# c_values.append(100)
for c in c_values:
    accuracy = LogisticRegressionCV(Cs=[c], scoring='accuracy', max_iter=7500, cv=5, random_state=0, solver='lbfgs').fit(x, y).score(x, y)
    print('C=' + str(c) + '  Mean Accuracy: ' + '%.2f' % (accuracy*100))
