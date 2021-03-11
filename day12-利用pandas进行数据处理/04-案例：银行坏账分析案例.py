# import pandas as pd
# import numpy as np
#
# # 设置pandas的显示
# pd.set_option('display.float_format', lambda x: '%.2f' % x)
#
# # 加载数据
# data = pd.read_csv('./data/loan.csv', encoding='ansi')
# print('data:\n', data)
# print('data:\n', data.columns)
# print('*' * 100)
#
# # 注意：好坏用户中0代表信用好的用户，1代表信用差的用户
#
# # 检测并处理缺失值
# res_null = pd.isnull(data).sum()
# # print('缺失值检测结果：\n', res_null)
#
# # 处理月收入的缺失值
# # 可以使用 众数 来填充月收入
# # 计算月收入众数
# mode = data.loc[:, '月收入'].mode()[0]
# # 填充
# data.loc[:, '月收入'].fillna(value=mode, inplace=True)
#
# # res_null = pd.isnull(data).sum()
# # print('缺失值检测结果：\n', res_null)
# # 1、月收入和坏账的关系
#
# # 对月收入进行离散化
# # 默认分组效果不好
# # data.loc[:, '月收入'] = pd.cut(
# #     x=data.loc[:, '月收入'],
# #     bins=5
# # )
# # print('分组结果为：\n', data.loc[:, '月收入'])
# # print('*' * 100)
#
#
# # 自定义分组规则的bins,后一个元素必须 > 前一个元素
# # 等宽分组  ---效果不好
# # # a、确定分组组数
# # group_num = 5
# # # b、确定最大值、最小值
# # max_income = data.loc[:, '月收入'].max()
# # min_income = data.loc[:, '月收入'].min()
# # print('max_income:', max_income)
# # print('min_income:', min_income)
# # # c、确定最大值、最小值的间距
# # ptp_income = max_income - min_income
# # # d、确定分组间距
# # width = int(np.ceil(ptp_income / group_num))
# # # e、确定分组节点
# # bins = np.arange(min_income, max_income + width, width)
# # # 注意：如果自定义分组，此时需要传递 include_lowest=True,来包含最小值
# # data.loc[:, '月收入'] = pd.cut(
# #     x=data.loc[:, '月收入'],  # 需要离散化的连续型数据
# #     bins=bins,  # 分组规则
# #     include_lowest=True
# # )
# # print('查看离散化之后的结果为：\n', data.loc[:, '月收入'])
# # print('*' * 100)
#
# # 自定义等频分组
# group_num = 7
# # 确定位置
# q = np.arange(0, 1 + 1 / group_num, 1 / group_num)
# data.loc[:, '月收入'] = pd.qcut(
#     x=data.loc[:, '月收入'],
#     q=q
# )
# print('查看离散化之后的结果为：\n', data.loc[:, '月收入'])
# print('*' * 100)
# # 统计分组之后，每组的元素个数
# res = pd.value_counts(data.loc[:, '月收入'])
# print('分组结果及元素个数：\n', res)
# print('*' * 100)
#
# # 查看月收入 和 信用差的用户数量的关系
# # 月收入 ---类别型数据
# # 按照月收入进行分组，统计 坏用户的数量
# df = pd.pivot_table(
#     data=data,
#     index='月收入',
#     values='好坏客户',
#     aggfunc='sum',  # 注意：坏用户为1，好用户为0
# )
# print('df:\n', df)
#
# #
# percent_bad = df.loc[:, '好坏客户'] / df.loc[:, '好坏客户'].sum()
#
# print('坏用户的占比为：\n', percent_bad)
# # 月收入越高，坏账用户越少。
#
# # 2、年龄和坏账的关系
# # 对年龄进行离散化 ---等频分组
# # 分组聚合

#
# # 3、家属数量和坏账的关系
# # 对家属数量进行分离散化 ---缺失值使用众数填充，然后自定义分组[0,1,2,3,4,21]
# (-0.01,1)
# [1,2)
# [2,3)
# [3,4)
# [4,21)
# # 分组聚合
