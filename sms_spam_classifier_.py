# -*- coding: utf-8 -*-
"""SMS Spam Classifier .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11nZvZPLvm6RHxN16xgI-u9JqJJ15gnNn
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

df=pd.read_csv("mail_data.csv")

print(df)

data=df.where((pd.notnull(df)),'')
data.head()

data.info()

data.loc[data["Category"] == 'spam',"Category",] = 0
data.loc[data["Category"] == 'ham',"Category",] = 1

X=data['Message']
Y=data['Category']

print(Y)

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=3)

print(X.shape)
print(X_train.shape)
print(X_test.shape)

feature_extraction = TfidfVectorizer(min_df = 1, stop_words = 'english', lowercase = True)

X_train_features = feature_extraction.fit_transform(X_train)
X_test_features=feature_extraction.transform(X_test)

Y_train=Y_train.astype('int')
Y_test=Y_test.astype('int')

print(X_train_features)

Model=SVC()

Model.fit(X_train_features,Y_train)

prediction_on_training_data=Model.predict(X_train_features)
accuracy_on_training_data=accuracy_score(Y_train,prediction_on_training_data)

print('accuracy on training data:',accuracy_on_training_data)

prediction_on_testing_data=Model.predict(X_test_features)
accuracy_on_testing_data=accuracy_score(Y_test,prediction_on_testing_data)

print('accuracy on testing data:',accuracy_on_testing_data)

