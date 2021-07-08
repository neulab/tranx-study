# Example code, write your program here
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

C = [0.01, 0.1, 1, 10, 100]
data = pd.read_csv('dataset/wine.data', header = None)
data = data.apply(LabelEncoder().fit_transform)
X = data.drop(0, axis = 1)
Y = data[0]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, shuffle=True)

model = [None, None, None, None, None]
for i in range(len(C)):
    model[i] = LogisticRegression(solver = 'lbfgs', multi_class='multinomial', C = C[i], random_state=0, max_iter=1000)
    model[i].fit(X_train, Y_train)
    score = model[i].score(X_test, Y_test)
    print('C=' + str(C[i]) + '    Mean Accuracy: ' + '{:.2f}'.format(score))
