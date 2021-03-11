from sklearn.feature_extraction.text import TfidfVectorizer  # 词的重要性程度统计模块

# 构建文章
content = ['The river flows eastward, and the stars in the sky join the Big Dipper',
           'i  y Sunset, heartbroken man in the end of the world',
           'Sun for morning,Moon for night,and You forever',
           'good good study,day day up']

# 1、实例化对象
tfidf = TfidfVectorizer()
# 2、统计词的重要性程度
x = tfidf.fit_transform(content)
# 获取统计的词语
words = tfidf.get_feature_names()
print('words:\n', words)
# print('x:\n',x)  # sparse矩阵
print('x:\n', x.toarray())

# 统计的是词的tfidf指标
# tfidf = tf*idf
# tf ---词频
# 指的是某一个给定的词语在该文件中出现的频率。即词 w 在文档 d 中出现的次 count(w, d)和文档 d 中总词数 size(d)的比值
# tf_flows = 1/14

# idf ----逆文档词频
# 是一个词语普遍重要性的度量
# 某一特定词语的 IDF，可以由总文件数目除以包含该词 语之文件的数目，再将得到的商取对数得到。即文档总数 n 与词 w 所出现文件数 docs(w, D) 比值的对数

# idf_flows = log(4/1)

# tf_idf_flows = tf_flows *  idf_flows= 1/7

# 如果真正计算 ---词 ---加权重