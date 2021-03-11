# 缺失值？
# 数据缺失的位置 ---缺失值（NaN、* ,' ',?,... ）
import pandas as pd
import numpy as np

# 设置pandas的显示
pd.set_option('display.float_format', lambda x: '%.1f' % x)

# 加载数据
data = pd.read_excel('./data/qs.xls', sheet_name=0)
print('data:\n', data)
print('*' * 100)

# 检测缺失值
# pd.isnull, pd.notnull 来检测是否含有缺失值
# 检测不出 特殊字符的缺失值
# 只能检测出NaN类型的缺失值
# pd.isnull --->如果缺失，则为True,如果有值，则为False,和sum连用，可以检测出各列的缺失值个数
# res_null = pd.isnull(data).sum()
# print('res:\n', res_null)

# pd.notnull --->如果缺失，则为False,如果有值，则为True,和sum连用，返回非空数据的数目，和count类似。 ---需要与shape[0]对比
# res_null = pd.notnull(data).sum()
# print('res:\n', res_null)

# 针对于特殊字符的缺失值，无法检测，但是，如果含有特殊字符的缺失值，再后续的计算中可能会报错，再反过来推倒可能含有特殊字符的缺失值


# 处理缺失值
# （1）删除法
# 可以使用dropna来删除缺失值。
# axis: 0--代表行， 1---代表列
# how='any', 只要含有缺失值，就进行删除
# how='all'，整列或者整行都为缺失值，才进行删除
# inplace :True，对原df进行修改，False,返回一个新的df
# data.dropna(axis=1, how='any', inplace=True)
# data.dropna(axis=0, how='any', inplace=True)
# # data.dropna(axis=1, how='all', inplace=True)
# print('data:\n',data)
# 可能会造成数据的大量丢失，
# 整列、或者整行大部分为缺失的情况下进行删除
# 在大量数据中仅删除极少量的数据

# # （2）填充法
# # 可以使用fillna来指定均值、中位数、众数、上一个、下一个非空的邻居来进行填充
# # 使用众数来填充 商品ID
# # a、计算众数
# mode = data.loc[:, '商品ID'].mode()[0]
# # b、填充
# data.loc[:, '商品ID'].fillna(value=mode, inplace=True)
# # 可以上下邻居来填充 门店编号
# # method --backfill,bfill代表下一个非空邻居， pad,ffill代表上一个非空邻居
# data.loc[:, '门店编号'].fillna(method='pad', inplace=True)
#
# data.loc[:, '类别ID'].fillna(method='bfill', inplace=True)
#
# print('data:\n', data)
# 填充之后可能会导致数据的分布规律发生变化

# （3）插值法
# 线性插值 ---拟合线性关系
# 多项式插值 ---（拉格朗日多项式插值、牛顿多项式插值） ---拟合多项式
# 样条插值 ---拟合曲线关系

# 借用插值模块
from scipy.interpolate import interp1d  # 线性插值模块, 样条插值模块
from scipy.interpolate import lagrange  # 拉格朗日多项式插值模块

# 构建插值数组
# x = np.array([1, 2, 3, 4, 5, 8, 9])
# y = np.array([3, 5, 7, 9, 11, 17, 19])  # y = 2*x + 1
# z = np.array([2, 8, 18, 32, 50, 128, 162])  # z = 2*x^2

# 利用插值模块 ---进行插值
# 用x来拟合y，用x来拟合z

# 线性插值
# line1 = interp1d(x, y, kind='linear')
# line2 = interp1d(x, z, kind='linear')
# print('使用x来拟合y得到结果为：', line1([6, 7]))  # [13. 15.]
# print('使用x来拟合z得到结果为：', line2([6, 7]))  # [ 76. 102.]

# 拉格朗日插值
# la1 = lagrange(x, y)
# la2 = lagrange(x, z)
# print('使用x来拟合y得到结果为：', la1([6, 7]))  # [13. 15.]
# print('使用x来拟合z得到结果为：', la2([6, 7]))  # [72. 98.]

# 样条插值
# line1 = interp1d(x, y, kind='cubic')
# line2 = interp1d(x, z, kind='cubic')
# print('使用x来拟合y得到结果为：', line1([6, 7]))  # [13. 15.]
# print('使用x来拟合z得到结果为：', line2([6, 7]))  # [72. 98.]

# 发现：
# 如果真实关系为线性关系，使用线性插值、拉格朗日插值、样条插值 ---效果一样
# 如果真实关系为非线性关系，那么线性插值表现差，拉格朗日插值、样条插值效果较好

# 真实工作环境中，非线性关系数据普遍存在 ----->推荐使用：拉格朗日插值、样条插值。

# 如果使用插值法真实的完成插值？？？  ---以拉个朗日插值法为例
# 使用插值法 来插值  类别ID

# # 指定n ---获取的是缺失值位置的前n个和后n个元素
# n = 5
#
# # 先判定缺失值的位置
# for i in range(data.shape[0]):
#     # i 表示行下标
#     # 判定 第i 行是否是缺失值
#     if pd.isnull(data.iloc[i, 1]):
#         # print(i)
#         if i - n < 0:
#             start = 0
#         else:
#             start = i - n
#         # 获取缺失值位置的前n个及后n个元素
#         mask = data.iloc[start:i + n, 1]
#         # 获取mask中非空的元素
#         y = mask[mask.notnull()].values
#         # 获取mask中的非空元素所对应的x
#         x = mask[mask.notnull()].index
#
#         # print('x:\n', x)
#         # print('y:\n', y)
#         # 构建拉格朗日对象
#         la = lagrange(x, y)
#         # 拟合
#         data.iloc[i, 1] = la([i])

# print('data:\n', data)

# 特殊字符的缺失值
# * : ? ' ' ...特殊字符的缺失值
# 先将特殊字符缺失值进行替换
data.replace('*', np.nan, inplace=True)
print('data:\n',data)
# 删除、填充、插值随意选择
