import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
#data_pd=pd.read_csv('d:/carotid_atherosclerosis/decesionTree/dataSetCon_knni.csv',header='infer',encoding='utf-8')
data_pd=pd.read_csv('../BIBM2017/data_knni_0725.csv',header='infer',encoding='utf-8')
data_np=np.array(data_pd)
list_name=list(data_pd.columns)
list_name=list_name[:-1]
clf=RandomForestClassifier(n_estimators=100,max_depth=None,min_samples_split=2,random_state=256)

dataSet_1=[line for line in data_np if line[-2]<1]
dataSet_2=[line for line in data_np if 1<=line[-2]<1.3]
dataSet_3=[line for line in data_np if 1.3<=line[-2]]


X_1=preprocessing.scale(np.array([line[:-2] for line in dataSet_1]))
y_1=np.array([line[-1] for line in dataSet_1])
X_2=preprocessing.scale(np.array([line[:-2] for line in dataSet_2]))
y_2=np.array([line[-1] for line in dataSet_2])
X_3=preprocessing.scale(np.array([line[:-2] for line in dataSet_3]))
y_3=np.array([line[-1] for line in dataSet_3])


clf.fit(X_1,y_1)
rt_import=np.array(clf.feature_importances_)
# print(rt_import)
#min_max_scaler=preprocessing.MinMaxScaler(feature_range=(0, 1))
#rt_import_scale=min_max_scaler.fit_transform(rt_import)
dict_import=zip(list_name,rt_import)
sort_dict=dict((names,value) for names,value in dict_import)
print(sorted(sort_dict.items(),key=lambda asd:asd[1],reverse=True))

clf.fit(X_2,y_2)
rt_import=np.array(clf.feature_importances_)
# print(rt_import)
#min_max_scaler=preprocessing.MinMaxScaler(feature_range=(0, 1))
#rt_import_scale=min_max_scaler.fit_transform(rt_import)
dict_import=zip(list_name,rt_import)
sort_dict=dict((names,value) for names,value in dict_import)
print(sorted(sort_dict.items(),key=lambda asd:asd[1],reverse=True))

clf.fit(X_3,y_3)
rt_import=np.array(clf.feature_importances_)
# print(rt_import)
#min_max_scaler=preprocessing.MinMaxScaler(feature_range=(0, 1))
#rt_import_scale=min_max_scaler.fit_transform(rt_import)
dict_import=zip(list_name,rt_import)
sort_dict=dict((names,value) for names,value in dict_import)
print(sorted(sort_dict.items(),key=lambda asd:asd[1],reverse=True))