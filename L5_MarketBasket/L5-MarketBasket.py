
import pandas as pd
from nltk.tokenize import word_tokenize

#数据加载


data = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
print(data)
print(data.shape)

#将数据存储到Ttransaction中

transaction = []
#存储字典
item_count = {}

for i in range(data.shape[0]):
    temp = []
    for j in range(data.shape[1]):
        item = str(data.values[i,j])
        if item != 'nan':
            temp.append(item)
            if item not in item_count:
                item_count[item] = 1
            else:
                item_count[item] += 1
    transaction.append(temp)

print(transaction)
print(item_count)

# 创建词云函数
from wordcloud import WordCloud

#去掉停用词
def remove_stop_words(f):
    stop_words = ['water','tea']
    for stop_word in stop_words:
        f = f.replace(stop_word,' ')
    return f

def create_word_cloud(f):
	f = remove_stop_words(f)
	cut_text = word_tokenize(f)
	cut_text = " ".join(cut_text)
	wc = WordCloud(
		max_words=100,
		width=2000,
		height=1200,
    )
	wordcloud = wc.generate(cut_text)
	wordcloud.to_file("wordcloud.jpg")

#生成词云
all_words = ' '.join('%s' %item for item in transaction)
print(all_words)

create_word_cloud(all_words)

#打印前10项商品
print(sorted(item_count.items(),key=lambda x:x[1],reverse=True)[:10])


