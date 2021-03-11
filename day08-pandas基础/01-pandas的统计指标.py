import pandas as pd
import numpy as np

# 加载数据
detail = pd.read_excel('./data/meal_order_detail.xls', sheet_name=0)
print('detail:\n', detail)
print('detail:\n', detail.columns)
print('*' * 100)

# pandas对于数值型数据的统计指标
# 查看数据类型
print('detail的元素的数据类型：\n', detail.dtypes)
# 对detail中的数值数据进行统计指标
# 对 amounts(单价) counts(数量)进行统计指标
# print('对detail中的amounts、counts统计最大值：\n', detail.loc[:, ['amounts', 'counts']].max())  # 返回series
# print('对detail中的amounts统计最大值：\n', detail.loc[:, 'amounts'].max())  # 返回具体的数值
# print('对detail中的amounts统计和\n', detail.loc[:, 'amounts'].sum())
# print('对detail中的amounts统计最小值\n', detail.loc[:, 'amounts'].min())
# print('对detail中的amounts统计均值\n', detail.loc[:, 'amounts'].mean())
# print('对detail中的amounts统计中位数\n', detail.loc[:, 'amounts'].median())
# print('对detail中的amounts统计最大值的下标\n', detail.loc[:, 'amounts'].idxmax())
# print('对detail中的amounts统计最小值的下标\n', detail.loc[:, 'amounts'].idxmin())
# print('对detail中的amounts统计标准差：\n', detail.loc[:, 'amounts'].std())
# print('对detail中的amounts统计方差：\n', detail['amounts'].var())

# 统计众数 --出现次数最多的数据 ---返回众数series
# print('对detail中的amounts统计众数：\n', detail.loc[:, 'amounts'].mode())
# print('对detail中的amounts统计众数：\n', type(detail.loc[:, 'amounts'].mode()))  # <class 'pandas.core.series.Series'>

# 统计非空数据的数目
# print('对detail中的amounts统计非空数据的数目：\n',detail.loc[:,'amounts'].count())
# print('对detail中的cost统计非空数据的数目：\n',detail.loc[:,'cost'].count())

# 统计四分位数
# print('对detail中的amounts统计四分位数：\n', detail.loc[:, 'amounts'].quantile(q=[0, 0.25, 0.5, 0.75, 1.0]))
# print('对detail中的amounts统计四分位数：\n', detail.loc[:, 'amounts'].quantile(q=np.arange(0, 1 + 1 / 4, 1 / 4)))


# 统计描述---describe
# 返回8个结果
# 非空数据的数目、均值、标准差、分位数（最小值、下四分位数、中位数、上四分位数、最大值）
print('对detail中的amounts统计描述：\n', detail.loc[:, 'amounts'].describe())
'''
count    2779.000000 #非空数据的数目
mean       45.337172 #均值
std        36.808550 #标准差
min         1.000000 #最小值
25%        25.000000 #下四分位数
50%        35.000000 #中位数
75%        56.000000 #上四分位数
max       178.000000 #最大值
'''

# # 可以借助describe对于非数值型数据进行统计指标
# # 返回4种结果
# # 非空数据的数目，去重之后的数据数目，众数，众数出现的次数
# print('对detail中的dishes_name统计描述:\n', detail.loc[:, 'dishes_name'].describe())
#
# # 如果统计 单价的众数，以及单价众数出现的次数
# # (1)先将单价进行转换类型----非数值型
# # category ---类别型
# detail.loc[:, 'amounts'] = detail.loc[:, 'amounts'].astype('category')
# print('detail的数据类型：\n', detail.dtypes)
# # (2)统计describe描述
# print('此时对amounts统计describe：\n', detail.loc[:, 'amounts'].describe())

# 可以借助mode对于非数值型数据统计众数
# print('对detail中的dishes_name统计众数：\n',detail.loc[:,'dishes_name'].mode())

# value_counts 可以统计某列数据各个不同元素的及其出现的次数
# print('对于counts统计不同的数量及其出现的次数:\n',detail.loc[:,'counts'].value_counts())
