# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 14:34:03 2020

@author: quresa9
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

df = pd.read_csv('salary_data_cleaned.csv')
df.columns

# Choose relevant columns
df_model = df[['average_salary','Rating', 'Size', 'currency', 'Type of ownership',
             'Industry', 'Sector', 'Revenue', 'hourly','age' ,'job_region-state', 
             'python_yn','sql_yn', 'cloud_yn', 'excel_yn', 'bigquery_yn',
             'spark_yn', 'job_simpl', 'seniority', 'desc_len']]
# Get dummy data 
df_dum = pd.get_dummies(df_model)
df_dum
# Train, test split 

X = df_dum.drop('average_salary', axis = 1)
y = df_dum.average_salary.values

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state = 42 ) 
#y_train = y_train.reshape(len(y_train),1)
#y_test = y_test.reshape(len(y_test),1)

print(X_train.shape, X_test.shape)
print(y_train.shape, y_test.shape)
#MODELS
import statsmodels.api as sm
# multiple linear regressions
# use stat models
X_sm = sm.add_constant(X_train)
model = sm.OLS(y_train,X_sm)
print(model.fit().summary())

# Sklearn Linear Regression 
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score

lm = LinearRegression()
lm.fit(X_train, y_train)
print('Score',lm.score(X_train, y_train))
print(np.mean(cross_val_score(lm, X_train, y_train, scoring = 'neg_mean_absolute_error', cv=3)))

# lasso regression
# Alpha value place an important role in tuning Lasso regression model. 
# Let us try to acheive optimizied 'alpha value' where 'error' is minimum. 
lm_l = Lasso(alpha = 0.12)
lm_l.fit(X_train, y_train)
print('Score',lm_l.score(X_train, y_train))
print(np.mean(cross_val_score(lm_l, X_train, y_train, scoring = 'neg_mean_absolute_error', cv=3)))

# Alpha value place an important role in tuning Lasso regression model. 
# Let us try to acheive optimizied 'alpha value' where 'error' is minimum.
alpha = []
error = []

for e in range(1,100):
    alpha.append(e/100)
    lmm = Lasso(alpha = e/100)
    error.append(np.mean(cross_val_score(lmm, X_train, y_train, 
                                         scoring = 'neg_mean_absolute_error', 
                                         cv=3))
    )
    
plt.plot(alpha, error)   

eff = tuple(zip(alpha,error))

df_err = pd.DataFrame(list(eff), columns=['alpha','error'])

df_err[df_err.error == max(df_err.error)]

# random forest 
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()
rf.fit(X_train, y_train)
print('RF before GridSearch score: ',np.mean(cross_val_score(rf, X_train, y_train, 
                              scoring = 'neg_mean_absolute_error', 
                              cv=3)))
# tune model parameters using GridSearch CV
from sklearn.model_selection import GridSearchCV
parameters = {'n_estimators': np.arange(10,100,10), 'criterion':('mse','mae'), 
              'max_features':('auto','sqrt','log2')}

gs = GridSearchCV(rf, parameters, 
                  scoring = 'neg_mean_absolute_error',
                  cv=3)
gs.fit(X_train, y_train)
gs.best_estimator_
print('RF After GridSearch score: ',gs.best_score_)


# test ensembles 
ypred_lm = lm.predict(X_test)
ypred_lml = lm_l.predict(X_test)
ypred_rf = gs.best_estimator_.predict(X_test)

from sklearn.metrics import mean_absolute_error as mae
print('MAE linear regression: ', mae(y_test, ypred_lm))
print('MAE lasso regression: ', mae(y_test, ypred_lml))
print('MAE random forest regression: ', mae(y_test, ypred_rf))


# At times, by combining two models, it improves the result. 
# Let's try it with Lasoo and random forest.
ens_lml_rf = (ypred_lml+ypred_rf)/2
print('MAE Ensemble regression: ', mae(y_test, ens_lml_rf))

