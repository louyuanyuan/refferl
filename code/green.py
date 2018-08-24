# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import time,datetime
import matplotlib.pyplot as plt

green_taxi1=pd.DataFrame(pd.read_csv('datasets/green_tripdata_2017-01.csv'))
green_taxi2=pd.DataFrame(pd.read_csv('datasets/green_tripdata_2017-02.csv'))
green_taxi3=pd.DataFrame(pd.read_csv('datasets/green_tripdata_2017-03.csv'))

green_taxi=green_taxi1.append(green_taxi2,ignore_index=False)
green_taxi=green_taxi.append(green_taxi3,ignore_index=False)

green_taxi.head()


green_taxi['lpep_pickup_datetime']=pd.to_datetime(green_taxi['lpep_pickup_datetime'])

green_taxi = green_taxi.set_index('lpep_pickup_datetime')

monthly=green_taxi.resample('M')['VendorID']

plt.rc('font', family='STXihei', size=15)
a=np.array([1,2,3,4,5,6])
plt.bar([1,2,3,4,5,6],monthly,color='#99CC01',alpha=0.8,align='center',edgecolor='white')
plt.xlabel('月份')
plt.ylabel('搭乘次数')
plt.title('2016年1-6月Green TAXI搭乘次数')
plt.legend(['搭乘次数'], loc='upper right')
plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='y',alpha=0.6)
plt.xticks(a,('1月','2月','3月','4月','5月','6月'))
plt.ylim(0,1800000)
plt.show()

