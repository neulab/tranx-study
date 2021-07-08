# Example code, write your program here
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate
import statistics

X = []
y = []
with open('dataset/wine.data') as fin:
    for line in fin:
        data = line.strip().split(',')
        X.append([float(x) for x in data[1:]])
        y.append(int(data[0]))

for c in [0.01, 0.1, 1, 10, 100]:
    clf = LogisticRegression(C=c)
    results = cross_validate(clf, X, y, cv=5)
    acc = '{:0.2f}'.format(statistics.mean(results['test_score'])*100)
    print('C='+str(c)+'\tMean Accuracy: '+acc+'\n')