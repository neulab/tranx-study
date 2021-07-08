# Example code, write your program here
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_wine
import numpy
X, y = load_wine(return_X_y=True)
arr = {0.01,0.1,1,10,100}
for i in sorted(arr):
    # print(i)
    clf = LogisticRegression(C=i, random_state=0, solver='lbfgs', max_iter=1000000, multi_class='multinomial').fit(X,y)
    # print(clf.score(X,y))
    print ("C="+str(i)+"\tMean Accuracy: "+str(format(numpy.array(cross_val_score(clf, X, y, cv=5)).mean()*100,".2f")))
