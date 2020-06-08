# Task Description

You are expected to train a multi-class logistic regression model for the data in `dataset`. The dataset is Wine from UCI Machine Learning Repository (http://archive.ics.uci.edu/ml/datasets/Wine/).
You could find detailed dataset description in `dataset/wine.names`, and the actual dataset file in `dataset/wine.data`.
The dataset file is comma-separated, with the first column being target class `1, 2 or 3` and followed by 13 real-valued attributes.
Since this is a multi-class classification problem, you are actually using multinomial logistic regression model.

After running `python main.py` the program should train and evaluate the logistic regression model on the dataset through 5-fold cross-validation. The solver used should be `lbfgs`.
Since we are also interested in how different regularization parameter `C` selection affects model performance, the program should print cross-validation mean accuracy (2 decimals) for `C = {0.01, 0.1, 1, 10, 100}`.
Please refer to example output for the print format.
Also, for stable results, please set the random state to 0.


# Example Output

```
$ python main.py
C=0.01  Mean Accuracy: 95.10
...
C=100   Mean Accuracy: 98.43


```

Note that the numbers for `Mean Accuracy` shown above is just an example and does not reflect the real results.