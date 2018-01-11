import pandas as pd
import numpy as np

#ads_1_sum,ads_2_sum是每个店铺90天的广告费用和
ads_all=pd.read_csv('../JDD_sale/dataset/sort_t_ads.csv')
ads_all['create_dt']=pd.to_datetime(ads_all['create_dt'])
ads_all=ads_all.set_index('create_dt')
#ads_1是01-31以后90天的广告数据，ads_2是2016-12-31以后90天的数据
ads_1_tmp=ads_all['2017-01-31':]
ads_2_tmp=ads_all['2016-12-31':'2017-03-30']
#print(ads_1_tmp.shape,ads_2_tmp.shape)
ads_1=ads_1_tmp[['shop_id','consume']]
ads_2=ads_2_tmp[['shop_id','consume']]
#print(ads_1.shape,ads_2.shape)
#print(ads_1.head(10),ads_2.head(10))
#ads_1_sum,ads_2_sum是每个店铺的消费和
ads_1_sum=ads_1.groupby(['shop_id']).sum()
ads_2_sum=ads_2.groupby(['shop_id']).sum()
#print(ads_1_sum.shape,ads_2_sum.shape)



#######################################################################
#comment_1_sum,comment_2_sum是每个店铺90天的广告费用和
comment_all=pd.read_csv('../JDD_sale/dataset/sort_t_comment.csv')
comment_all['create_dt']=pd.to_datetime(comment_all['create_dt'])
comment_all=comment_all.set_index('create_dt')
#comment_1是01-31以后90天的广告数据，comment_2是2016-12-31以后90天的数据
comment_1_tmp=comment_all['2017-01-31':]
comment_2_tmp=comment_all['2016-12-31':'2017-03-30']
#print(comment_1_tmp.shape,comment_2_tmp.shape)
comment_1=comment_1_tmp[['shop_id','good_num','cmmt_num']]
comment_2=comment_2_tmp[['shop_id','good_num','cmmt_num']]
#print(comment_1.head(10),comment_2.head(10))
comment_1_sum=comment_1.groupby(['shop_id']).sum()
comment_2_sum=comment_2.groupby(['shop_id']).sum()
print(comment_1_sum.index)
#print(comment_1_sum.head(5),comment_2_sum.head(5))



#######################################################################
#order_1_sum,order_2_sum是每个店铺90天的广告费用和
order_all=pd.read_csv('../JDD_sale/dataset/sort_t_order.csv')
order_all['ord_dt']=pd.to_datetime(order_all['ord_dt'])
order_all=order_all.set_index('ord_dt')
#order_1是01-31以后90天的广告数据，order_2是2016-12-31以后90天的数据
order_1_tmp=order_all['2017-01-31':]
order_2_tmp=order_all['2016-12-31':'2017-03-30']
#print(order_1_tmp.shape,order_2_tmp.shape)
order_1=order_1_tmp[['shop_id','offer_cnt','ord_cnt']]
order_2=order_2_tmp[['shop_id','offer_cnt','ord_cnt']]
#print(order_1.head(10),order_2.head(10))
order_1_sum=order_1.groupby(['shop_id']).sum()
order_2_sum=order_2.groupby(['shop_id']).sum()
#print(order_1_sum.head(5),order_2_sum.head(5))



#######################################################################
result_1=pd.concat([comment_1_sum,ads_1_sum,order_1_sum],axis=1)
result_2=pd.concat([comment_2_sum,ads_2_sum,order_2_sum],axis=1)
result_1.to_csv('../JDD_sale/dataset/data_1.csv')
result_2.to_csv('../JDD_sale/dataset/data_2.csv')

