
import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt

#数据加载
data = pd.read_csv('train.csv')

#转换为pandas中的日期
data['Datetime'] = pd.to_datetime(data['Datetime'],dayfirst=True)

#设置datatime为index
data.index = data['Datetime']
data.drop(['ID','Datetime'],axis=1,inplace=True)

# print(data)

#按照天采样
daily_data = data.resample('D').sum()
# print(daily_data)

daily_data['ds'] = daily_data.index
daily_data['y'] = daily_data['Count']
daily_data.drop(['Count'],axis=1, inplace=True)
print(daily_data)

#创建模型
m = Prophet(yearly_seasonality=True, seasonality_prior_scale=0.1)
#拟合之前数据
m.fit(daily_data)

# 预测未来7个月，213天
future = m.make_future_dataframe(periods=213)
# print(future)

#设置下限
daily_data['cap'] = 16856
daily_data['floor'] = 60
future['cap'] = 20000
future['floor'] = 60

#创建模型
m = Prophet(growth='logistic')
#拟合之前数据
m.fit(daily_data)

#预测未来数据
forecast = m.predict(future)
print(forecast)
m.plot(forecast)
plt.show()

