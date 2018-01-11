# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 20:35:25 2017

@author: WangHaitao
"""
import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.metrics import r2_score
data_x_1 = pd.read_csv('../JDD_sale/dataset/data_1.csv')
data_y_1 = np.array(pd.read_csv('../JDD_sale/dataset/sale1.csv'))
data_x_2 = pd.read_csv('../JDD_sale/dataset/data_2.csv')
data_y_2 = np.array(pd.read_csv('../JDD_sale/dataset/sale2.csv'))
#缺失值处理，填上0
data_X_1 = np.array(data_x_1.fillna(0))
data_X_2 = np.array(data_x_2.fillna(0))
#划分训练集和测试集
X_train = [line[1:] for line in data_X_1]
y_train = [line[-1] for line in data_y_1]
X_test = [line[1:] for line in data_X_2]
y_test = [line[-1] for line in data_y_2]

alpha = 0.1
lasso = Lasso(alpha=alpha)

y_pred=lasso.fit(X_train,y_train).predict(X_test)
r2_score_lasso = r2_score(y_test, y_pred)
print(lasso.score(X_test,y_test))
print("r^2 on test data : %f" % r2_score_lasso)
