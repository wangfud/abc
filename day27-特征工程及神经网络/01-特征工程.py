# 二值化处理
# 将数据修改为要么为1，要么为0
from sklearn.preprocessing import Binarizer

# # (1)实例化对象
# # threshold:指定阈值，大于阈值修改为1，小于阈值修改为0
# binary = Binarizer(threshold=1)
# # (2)转化数据
# # 参数：需要转化的数据
# x = binary.fit_transform(x)


# 特征降维
# 特征选择

# 低方差过滤 --->如果方差过小，数据比较接近，整列数据基本相差较小
from sklearn.feature_selection import VarianceThreshold

# # (1)实例化对象
# # 参数 threshold --->表示方差阈值，如果小于该方差，就会被剔除
# threshold = VarianceThreshold(threshold=0.1)
# # (2)进行过滤
# x = threshold.fit_transform(x)


# 卡方统计量---
# 剔除的是与目标值无关的。留下的是月目标值相关的。
from sklearn.feature_selection import chi2  # 卡方检验
from sklearn.feature_selection import SelectKBest  # 筛选

# import pandas as pd
#
# from sklearn.feature_extraction import DictVectorizer
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.tree import export_graphviz
#
# # 利用决策树，来查看在哪些特征下，游客存在生存下去的可能
#
#
# # 1、 加载数据
# data = pd.read_csv('./data/titanic.csv')
#
# # 2、筛选数据
# # 前3列为特征 --->目标值
# data = data.loc[:, ['pclass', 'age', 'sex', 'survived']]
# print('data:\n', data)
# print('data:\n', data.columns)
#
# # 3、数据处理
# # 检测缺失值
# res_null = pd.isnull(data).sum()
# print('缺失值检测结果为：\n', res_null)
#
# # 填充  ---平均年龄
# mean_age = int(data.loc[:, 'age'].mean())
# print('mean_age:', mean_age)
#
# data.loc[:, 'age'].fillna(value=mean_age, inplace=True)
#
# print('缺失值检测:\n', pd.isnull(data).sum())
#
# # 数据集拆分
# x = data.loc[:, ['pclass', 'age', 'sex']]
# print('x:\n', x.dtypes)
# y = data.loc[:, 'survived'].values
# print('y:\n', y.dtype)
#
# #  需要将特征值转化为 数值型
# #  哑变量转化
# # 字典特征数据抽取 ---将字典类型的数据转化为数值型特征
# # (1) 先将 x --->字典
# # 将DataFrame转化为 dict
# x = x.to_dict(orient='records')
# print('x:\n', x)
#
# # (2)字典特征抽取
# # a、实例化对象
# dict_vet = DictVectorizer(sparse=False)
# # b、转化特征
# x = dict_vet.fit_transform(x)
# # 获取转化之后的特征名称
# feature_names = dict_vet.get_feature_names()
# print('feature_names:\n', feature_names)
# print('x:\n', x)
# print('x:\n', type(x))

# # 先计算卡方统计量，由高到低排名， 获取排名靠前的前k个特征
# # 实例化对象
# ch = SelectKBest(chi2, k=3)
# # 统计并筛选数据
# x = ch.fit_transform(x, y)
# print('x:\n', x.shape)


# 特征降维
# 引入PCA 和LDA
# from sklearn.decomposition import PCA
# from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# PCA
# (1)实例化对象
# n_components :如果为小数，降维后的数据占原来数据特性的 占比
# 如果为整数，将高维度的数据转化为 含有n_components 个特征来表示原来的数据
# pca = PCA(n_components=0.9)
# pca = PCA(n_components=2)
# # (2)数据降维
# x = pca.fit_transform(x)

# LDA
# # (1)实例化对象
# n_components --->参考理解如PCA中参数
# lda = LinearDiscriminantAnalysis(n_components=)
# # (2) 数据降维
# x,y = lda.fit_transform(x,y)
