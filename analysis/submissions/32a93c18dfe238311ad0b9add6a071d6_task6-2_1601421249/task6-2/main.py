import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
dataset = pd.read_csv('dataset/wine.data')
X = dataset.iloc[:, range(1, 13)].values
y = dataset.iloc[:, 0].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
C = [0.01, 0.1, 1, 10, 100]
for num in C:
    classifier = LogisticRegression(random_state=0, C=num, max_iter=100000000)
    run = classifier.fit(X_train, y_train)
    y_pred = run.predict(X_test)
    accuracy = cross_val_score(run, X, y, scoring='accuracy', cv=5)
    mean = str(round(accuracy.mean() * 100, 2))
    print(f"C={num}  Mean Accuracy: {mean}")