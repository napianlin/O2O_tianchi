#!/user/bin/python
# -*- coding:UTF-8 -*-
import datetime as time
import numpy as np
import pandas as pd

def  date_Test():
    date1=time.date.today()
    dateStr=date1.strftime('%y %m %d')
# print dateStr

def None_Np_nan_Test():
    data2=pd.DataFrame([[1,'null'],[3.1,None]],columns=['a','b'])
    print '没处理\n',data2.dtypes,'\n'
    print data2,'\n'
    data2.replace(['null',None],-1,inplace=True)
    data2['b']=data2['b'].astype('int')
    print '第一步处理\n',data2.dtypes,'\n'
    print data2,'\n'
    # data2.b=data2.b.astype(int) #这样会舍掉 小数
    data2.replace(-1,np.nan,inplace=True)

    print '第二步处理\n',data2.dtypes,'\n'
    print data2


    # 没处理
    # a    float64
    # b     object
    # dtype: object
    #
    #      a     b
    # 0  1.0  null
    # 1  3.1  None
    #
    # 第一步处理
    # a    float64
    # b      int32
    # dtype: object
    #
    #      a  b
    # 0  1.0 -1
    # 1  3.1 -1
    #
    # 第二步处理
    # a    float64
    # b    float64
    # dtype: object
    #
    #      a   b
    # 0  1.0 NaN
    # 1  3.1 NaN

def dataFrame_Test():
    data2 = pd.DataFrame([[1, 'null'], [3.1, None]], columns=['a', 'b'])

    d1=data2['b']
    d2 = data2[['b']]
    print type(d1),'\n',type(d2)
    # < class 'pandas.core.series.Series'>
    # < class 'pandas.core.frame.DataFrame'>
    #一定要注意这里面的区别data2['b']是Series，data2[['b']]是DataFrame，两个类在很多地方都是不一样的

dataFrame_Test()


#注意 这个时候用了apply方法 注意与 agg的区别
# t10.user_date_datereceived_gap = t10.user_date_datereceived_gap.apply(get_user_date_datereceived_gap)
#注意 这个时候用了apply方法 注意与 agg的区别 可以使用 t10.groupby('user_id').agg([('min_user_date_datereceived_gap','min'),('avg_user_date_datereceived_gap','mean')])