import numpy as np
import pandas as pd
from xgboost.sklearn import XGBClassifier
from sklearn import preprocessing
from sklearn.model_selection import KFold
from sklearn.grid_search import GridSearchCV

data_t_ads=pd.read_csv('../JDD_sale/dataset/t_ads.csv')
data_t_comment=pd.read_csv('../JDD_sale/dataset/t_comment.csv')
data_t_order=pd.read_csv('../JDD_sale/dataset/t_order.csv')
data_t_product=pd.read_csv('../JDD_sale/dataset/t_product.csv')
data_t_sales_sum=pd.read_csv('../JDD_sale/dataset/t_sales_sum.csv')
print("t_ads.shape",data_t_ads.shape)
print("t_comment.shape",data_t_comment.shape)
print("t_order.shape",data_t_order.shape)
print("t_product.shape",data_t_product.shape)
print("t_sales_sum.shape",data_t_sales_sum.shape)

# sort by shop_id
sort_t_ads=data_t_ads.sort_values(by=['shop_id','create_dt'])
sort_t_comment=data_t_comment.sort_values(by=['shop_id','create_dt'])
sort_t_order=data_t_order.sort_values(by=['shop_id','ord_dt'])
sort_t_product=data_t_product.sort_values(by=['shop_id','on_dt'])
sort_t_sales_sum=data_t_sales_sum.sort_values(by=['shop_id','dt'])

sort_t_ads.to_csv('../JDD_sale/dataset/sort_t_ads.csv',index=False)
sort_t_comment.to_csv('../JDD_sale/dataset/sort_t_comment.csv',index=False)
sort_t_order.to_csv('../JDD_sale/dataset/sort_t_order.csv',index=False)
sort_t_product.to_csv('../JDD_sale/dataset/sort_t_product.csv',index=False)
sort_t_sales_sum.to_csv('../JDD_sale/dataset/sort_t_sales_sum.csv',index=False)


