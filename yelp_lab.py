# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 20:52:03 2015

@author: vanessaohta
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import statsmodels.formula.api as smf

# visualization
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

yelp = pd.read_csv('https://raw.githubusercontent.com/sinanuozdemir/SF_DAT_17/master/data/yelp.csv')
type(yelp)
yelp.head()
yelp.shape

sns.pairplot(yelp, x_vars=['cool','useful','funny'], y_vars='stars', size=6, aspect=0.7)

lm = smf.ols(formula='stars ~ cool useful funny', data=yelp).fit()

# create X and y
feature_cols = ['cool','useful','funny']
X = yelp[feature_cols]
y = yelp.stars

# instantiate and fit
linreg = LinearRegression()
linreg.fit(X, y)

# print the coefficients
print linreg.intercept_
print linreg.coef_

#split into test and train datasets 
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)

X.shape
y.shape

X_train.shape
X_test.shape
y_train.shape
y_test.shape

linreg.fit(X_train, y_train)

# print the coefficients
print linreg.intercept_
print linreg.coef_

linreg.score(X_test, y_test)








