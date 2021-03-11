

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import apriori
# from efficient_apriori import apriori
from mlxtend.frequent_patterns import association_rules

pd.set_option('max_columns',None)

#数据加载
data = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
print(data)
print(data.shape)


# 将数据存放到transactions中
transactions = []
#按照行进行遍历
for i in range(0, data.shape[0]):
    #记录一行Ttransaction
    temp = []
    #按照列进行遍历
    for j in range(0, data.shape[1]):
        if str(data.values[i, j]) != 'nan':
           temp.append(data.values[i, j])
    # print(temp)
    transactions.append(temp)

print(transactions)

from mlxtend.preprocessing import TransactionEncoder
#one hot 编码
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
print(te_ary)

transactions_hot_encoded = pd.DataFrame(te_ary, columns=te.columns_)
print(transactions_hot_encoded)

""""
# 挖掘频繁项集和频繁规则
itemsets, rules = apriori(transactions, min_support=0.02,  min_confidence=0.08)
print("频繁项集：", itemsets)
print("关联规则：", rules)
"""


#挖掘频繁项集 最小支持度为0.02
itemsets = apriori(transactions_hot_encoded,use_colnames=True,min_support=0.03)
#按支持度从大到小排序
itemsets = itemsets.sort_values(by='support',ascending=False)
print('#'*20,'频繁项集','#'*20)
print(itemsets)

rules = association_rules(itemsets,metric='lift',min_threshold=1)
rules = rules.sort_values(by='lift',ascending=False)
print('#'*20,'频繁规则','#'*20)
print(rules)


