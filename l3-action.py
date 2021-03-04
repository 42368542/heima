
import pandas as pd


#数据加载
from sklearn import preprocessing
from sklearn.cluster import KMeans

data = pd.read_csv('car_data.csv')
train_x = data[["人均GDP","城镇人口比重","交通工具消费价格指数","百户拥有汽车量"]]

#规范化到【0，1】空间
min_max_scaler = preprocessing.MinMaxScaler()
train_x = min_max_scaler.fit_transform(train_x)
pd.DataFrame(train_x).to_csv('temp.csv',index=False)
print(train_x)

#使用KMeans进行聚类
kmeans = KMeans(n_clusters=5)
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)

#合并聚类结果，插入到原数据中
result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类结果'},axis=1,inplace=True)
print(result)

"""
# K-Means 手肘法：统计不同K取值的误差平方和
import matplotlib.pyplot as plt
sse = []
for k in range(1, 11):
	# kmeans算法
	kmeans = KMeans(n_clusters=k)
	kmeans.fit(train_x)
	# 计算inertia簇内误差平方和
	sse.append(kmeans.inertia_)
x = range(1, 11)
plt.xlabel('K')
plt.ylabel('SSE')
plt.plot(x, sse, 'o-')
plt.show()

"""

#使用层次聚类
from scipy.cluster.hierarchy import dendrogram, ward
from sklearn.cluster import KMeans, AgglomerativeClustering
import matplotlib.pyplot as plt
model = AgglomerativeClustering(linkage='ward', n_clusters=5)

#fit+predict
y = model.fit_predict(train_x)
print(y)
linkage_matrix = ward(train_x)
dendrogram(linkage_matrix)
plt.show()