from sklearn.feature_extraction.text import CountVectorizer  # 统计词数模块

# 可以使用词数来代替文本特征
# 可以使用词的重要性程度来代替文本特征

# 构建文章
content = ['The river flows eastward, and the stars in the sky join the Big Dipper',
           'i  y Sunset, heartbroken man in the end of the world',
           'Sun for morning,Moon for night,and You forever',
           'good good study,day day up']

# 统计词的数量来将文本特征转化为数值特征
# 1、实例化对象
# 注意：统计词数的时候，认为单个长度的词不重要的，所以不统计
# 停止词 stop_words---可以人为指定一些不重要的词语
con_vet = CountVectorizer(stop_words=['big', 'day', 'dipper'])
# 2、统计词数
x = con_vet.fit_transform(content)
# 获取统计到的词语
words = con_vet.get_feature_names()
print('统计到的词语：\n', words)
# print('x:\n', x)  # --->sparse矩阵
print('x:\n', x.toarray())
