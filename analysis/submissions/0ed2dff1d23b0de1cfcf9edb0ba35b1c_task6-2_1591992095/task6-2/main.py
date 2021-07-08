# Example code, write your program here
import warnings

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score


def main():
    np.random.seed(0)
    X, y = [], []
    with open("dataset/wine.data", "r") as f:
        for line in f:
            if not line.strip(): continue
            label, *feat = line.strip().split(",")
            X.append([float(x) for x in feat])
            y.append(int(label))
    X = np.asarray(X)
    y = np.asarray(y)

    warnings.filterwarnings('ignore')
    for c in [0.01, 0.1, 1, 10, 100]:
        clf = LogisticRegression(
            multi_class='multinomial', solver='lbfgs', C=c, max_iter=100)
        mean_acc = np.mean(cross_val_score(clf, X, y, cv=10))
        print(f"C={c}\tMean Accuracy: {mean_acc * 100:.2f}")


if __name__ == '__main__':
    main()
