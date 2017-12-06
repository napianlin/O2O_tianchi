#!/user/bin/python
# -*- coding:UTF-8 -*-
import numpy as np
import pandas as pd
from datetime import datetime


# 处理 优惠券折扣率
def get_discount_rate(dis_count):
    if (dis_count != None):
        list = dis_count.split(':')
        if (len(list) >= 2):
            man = list[0]
            jian = list[1]
            discount_rate = float(jian) / float(man)
            return discount_rate
    return None


online_data_path = '../data/ccf_online_napialin.csv'
offline_data_path = '../data/ccf_offline_napianlin.csv'
# User_id,Merchant_id,Action,Coupon_id,Discount_rate,Date_received,Date
ondata = pd.read_csv(online_data_path, nrows=300)
offdata = pd.read_csv(offline_data_path, nrows=300)
# - **用户线上相关的特征**
# 	- 用户线上操作次数
# 	- 用户线上点击率
# 	- 用户线上购买率
# 	- 用户线上领取率
# 	- 用户线上不消费次数
# 	- 用户线上优惠券核销次数
# 	- 用户线上优惠券核销率
# 	- 用户线下不消费次数占线上线下总的不消费次数的比重
# 	- 用户线下的优惠券核销次数占线上线下总的优惠券核销次数的比重
# 	- 用户线下领取的记录数量占总的记录数量的比重

# 用户操作 特征
user_on_action = ondata[['User_id', 'Action']]
user_on_action['user_action'] = 1
user_on_action = user_on_action.groupby(by=['User_id', 'Action']).agg('sum').unstack()  # 11936031     7  14438631     7
user_on_action.columns = ['user_action_click_times', 'user_action_purchase', 'user_action_getCoup']
# user_on_action = user_on_action.reset_index()

user_on_action.replace(np.nan, 0, inplace=True)
user_on_action['user_action_total'] = user_on_action['user_action_click_times'] + user_on_action['user_action_purchase'] + \
                                      user_on_action['user_action_getCoup']

# 用户线上不消费次数
t5 = ondata[ondata['Date'] == 'null'][['User_id']]
t5['user_on_nopurchase_times'] = 1
user_on_nopurchase_times = t5.groupby(by=['User_id']).agg('sum')

#  用户线上优惠券核销次数
t6 = ondata[(ondata['Date'] != 'null') & (ondata['Date_received'] != 'null')][['User_id']]
t6['user_on_purchase_coup_times'] = 1
user_on_purchase_coup_times = t6.groupby(by=['User_id']).agg('sum')

# 用户线下不消费次数占线上线下总的不消费次数的比重  统计user线下没有消费的次数
t7 = offdata[offdata['Date'] == 'null'][['User_id']]
t7['user_off_nopurchase_times'] = 1
user_off_nopurchase_times = t7.groupby(by=['User_id']).agg('sum')

# 用户线下的优惠券核销次数占线上线下总的优惠券核销次数的比重 统计user线下使用消费券的次数
t8 = offdata[(offdata['Date'] != 'null') & (offdata['Date_received'] != 'null')][['User_id']]
t8['user_off_purchase_times'] = 1
user_off_purchase_times = t8.groupby(by=['User_id']).agg('sum')

# 用户线下领取的记录数量占总的记录数量的比重
t9 = offdata[(offdata['Coupon_id'] != 'null') & (offdata['Date'] == 'null')][['User_id']]
t9['user_off_getCoup'] = 1
user_off_getCoup = t9.groupby(by=['User_id']).agg('sum')


data= pd.concat([user_on_action,user_on_nopurchase_times,user_on_purchase_coup_times,user_off_nopurchase_times,user_off_purchase_times,user_off_getCoup],axis=1)
data.replace(np.nan,0,inplace=True)
print data
