from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import jieba

content = ['大家是祖国的未来、祖国的花朵',
           '今天的天气像女朋友的脾气说变就变',
           '女朋友生病了提醒她多喝红糖水',
           '问世间情为何物，直教人生死相许']

# 分词之后的文本内容
seg_list = []

# 对中文需要先分词
# jieba
# 安装：pip install jieba
# 对文本内容进行分词 ---精确模式--适合文本分析
for tmp in content:
    seg = jieba.cut(tmp, cut_all=False)
    # print('seg:\n', seg)  # generator
    # print(list(seg))
    # 拼接成字符串
    seg_str = ','.join(seg)
    # print('seg_str:\n', seg_str)
    seg_list.append(seg_str)

print('seg_list:\n', seg_list)

# # 1、实例化对象
# con_vet = CountVectorizer()
#
# # 2、统计词数
# x = con_vet.fit_transform(seg_list)
# # 获取统计到的词语
# words = con_vet.get_feature_names()
# print('获取统计到的词语：\n', words)
# print('x:\n', x.toarray())

# 1、实例化对象
tfidf = TfidfVectorizer()

# 2、统计词的重要性程度
x = tfidf.fit_transform(seg_list)
# 获取统计到的词语
words = tfidf.get_feature_names()
print('获取统计到的词语：\n', words)
print('x:\n', x.toarray())