# -*- coding: utf-8 -*-
"""RandomForestHyperparameter.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TANTa7gVA4e9SsqazehxJtXKWhILqUpw
"""

# -*- coding: utf-8 -*-
"""Combined_ML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dk3qEivWHhT-5RpNQERluGcRqkj6_qCE
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import VotingClassifier
from xgboost import XGBClassifier
from pickle import dump

df = pd.read_csv('Admission_Predict.csv')
y = df['target']
X = df.drop(['target'], axis = 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

cv = KFold(n_splits=10)

model = LogisticRegression(solver='lbfgs', max_iter=10000)
#models.append(('abc', AdaBoostClassifier(base_estimator=DecisionTreeClassifier(criterion= "gini",max_depth= 2, min_samples_leaf= 5, splitter= "random"), learning_rate= 0.01, n_estimators= 10)))
#models.append(('log', LogisticRegression(solver='lbfgs', max_iter=10000)))
#models.append(('gbc', GradientBoostingClassifier()))
##models.append(('svc', SVC()))
#models.append(('rfc', RandomForestClassifier()))
#models.append(('extra', ExtraTreesClassifier(n_estimators=100, max_features=3)))

#model = VotingClassifier(models)
model.fit(X, y)
score = cross_val_score(model, X_train, y_train, cv=cv)
print(score.mean())

dump(model, open('university_admission.pkl', 'wb'))