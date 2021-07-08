from sklearn.base import TransformerMixin
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegressionCV
from sklearn.pipeline import make_pipeline, Pipeline, FeatureUnion
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.preprocessing import FunctionTransformer

df = pd.read_csv('data/plugin_queries.csv')

# Creating train-test Split
X = df[['query']]
y = df[['is_generation']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)


class LengthTransformer(TransformerMixin):
    def transform(self, x, **transform_params):
        return np.array([len(t.split()) for t in x]).reshape(-1, 1)

    def get_feature_names(self):
        return 'length'

    def fit(self, X, y=None, **fit_params):
        return self


class ComplianceTransformer(TransformerMixin):
    def transform(self, x, **transform_params):
        return np.array([1 if '`' in t or '"' in t else 0 for t in x]).reshape(-1, 1)

    def get_feature_names(self):
        return 'compliance'

    def fit(self, X, y=None, **fit_params):
        return self


# fitting the classifier
vec = CountVectorizer(stop_words='english', ngram_range=(1, 2))
clf = LogisticRegressionCV(max_iter=1000)
# pipe = make_pipeline(vec, clf)

pipe = Pipeline([
    ('features', FeatureUnion([
        ('vectorizer', vec),
        # ('length', LengthTransformer()),
        # ('compliance', ComplianceTransformer()),
    ])),
    ('clf', clf)])
pipe.fit(X_train['query'], y_train['is_generation'])


print(len(vec.vocabulary_))

# feature_names = pipe.named_steps["features"].transformer_list[1][1].get_feature_names()
# print(feature_names)

def print_report(pipe):
    y_actuals = y_test['is_generation']
    y_preds = pipe.predict(X_test['query'])
    report = metrics.classification_report(y_actuals, y_preds)
    print(report)
    print("accuracy: {:0.3f}".format(metrics.accuracy_score(y_actuals, y_preds)))


print_report(pipe)

import eli5

explaination = eli5.show_weights(clf, vec=vec, top=200)

with open('query_classifier_weights.html', 'w') as f:
    f.write(explaination.data)
