import pandas as pd
import numpy as np

# 1、非数值型数据转化为数值型数据 ---哑变量转化
# 创建df
# df = pd.DataFrame(
#     data=np.mat([['广州', '深圳', '北京', '上海', '杭州', '广州'],
#                  ['zs', 'ls', 'ww', 'zl', 'kk', 'jj']]).T,
#     index=range(1, 7),
#     columns=['城市', '姓名']
# )
# print('df:\n', df)
#
# # 将非数值型数据转化为数值型
# # 哑变量转化
# res = pd.get_dummies(
#     data=df.loc[:, '城市'],  # 需要转化的数据
#     prefix='city',  # 前缀
#     prefix_sep='_',  # 前缀与数据之间的连接符
# )
# print('res:\n', res)
#
# # 合并
# all_df = pd.concat((df, res), axis=1, join='inner').drop(labels='城市', axis=1, inplace=False)
# print('all_df:\n', all_df)

# 2、连续数据的离散为类别型数据的处理 ---离散化
# 连续型数据--->具体的数值数据---一般用float类型表示
# 类别型数据（离散型数据）--->用来区分不同的类别，一般可以使用整数，也可以不使用整数

# 离散化---将连续型数据进行分组，转化一组一组这样的数据 --->类别型

# 加载detail
detail = pd.read_excel('./data/meal_order_detail.xls', sheet_name=0)
print('detail:\n', detail)
print('detail:\n', detail.columns)
print('*' * 100)

# amounts 代表菜品单价 ---连续型数据
# 可以使用cut进行离散化
# 可以使用默认分组
# detail.loc[:, 'amounts'] = pd.cut(
#     x=detail.loc[:, 'amounts'],  # 需要离散化的连续型数据
#     bins=5,  # 分组规则
# )
# print('查看离散化之后的结果为：\n', detail.loc[:, 'amounts'])
# print('*' * 100)

# 可以自定义分组
# # 构建自定义分组节点
# # 自定义等宽分组
# # a、确定分组组数
# group_num = 5
# # b、确定最大值、最小值
# max_amounts = detail.loc[:, 'amounts'].max()
# min_amounts = detail.loc[:, 'amounts'].min()
# print('min_amounts:', min_amounts)
# print('max_amounts:', max_amounts)
# # c、确定最大值、最小值的间距
# ptp_amounts = max_amounts - min_amounts
# # d、确定分组间距
# width = int(np.ceil(ptp_amounts / group_num))
# # e、确定分组节点
# bins = np.arange(min_amounts, max_amounts + width, width)
# # 注意：如果自定义分组，此时需要传递 include_lowest=True,来包含最小值
# detail.loc[:, 'amounts'] = pd.cut(
#     x=detail.loc[:, 'amounts'],  # 需要离散化的连续型数据
#     bins=bins,  # 分组规则
#     include_lowest=True
# )
# print('查看离散化之后的结果为：\n', detail.loc[:, 'amounts'])
# print('*' * 100)

# 可以使用自定义等频分组
# # 确定分组组数
# group_num = 5
# # 可以计算分位数来进行等频分组
# bins = detail.loc[:, 'amounts'].quantile(q=np.arange(0, 1 + 1 / group_num, 1 / group_num))
# # 注意：如果自定义分组，此时需要传递 include_lowest=True,来包含最小值
# detail.loc[:, 'amounts'] = pd.cut(
#     x=detail.loc[:, 'amounts'],  # 需要离散化的连续型数据
#     bins=bins,  # 分组规则
#     include_lowest=True
# )
# print('查看离散化之后的结果为：\n', detail.loc[:, 'amounts'])
# print('*' * 100)

# # 借助qcut来进行等频分组
# # 确定分组组数
# group_num = 5
# # 确定分组的分位数
# q = np.arange(0, 1 + 1 / group_num, 1 / group_num)
# detail.loc[:, 'amounts'] = pd.qcut(
#     x=detail.loc[:, 'amounts'],  # 需要离散化的连续型数据
#     q=q,  # 位置
#     labels=['I', 'II', 'III', 'IV', 'V'],  # 可以指定各个分组的名称
# )
# print('查看离散化之后的结果为：\n', detail.loc[:, 'amounts'])
# print('*' * 100)

# # 也可以自己定义分组节点
# bins = [1, 30, 60, 100, 120, 180]
# # 注意：如果自定义分组，此时需要传递 include_lowest=True,来包含最小值
# detail.loc[:, 'amounts'] = pd.cut(
#     x=detail.loc[:, 'amounts'],  # 需要离散化的连续型数据
#     bins=bins,  # 分组规则
#     include_lowest=True,
#     labels=['I', 'II', 'III', 'IV', 'V']
# )
# print('查看离散化之后的结果为：\n', detail.loc[:, 'amounts'])
# print('*' * 100)
#
# # 用区间数据代替原来的具体的数值。
# # 查看 amounts 的数据，及数据出现的次数
# res = pd.value_counts(detail.loc[:, 'amounts'])
# print('res:\n', res)


