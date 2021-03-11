import pandas as pd

# # 加载数据
# fp = pd.read_excel('./data/concat直接拼接数据.xls', sheet_name=None, index_col=0)
# # print('fp:\n', fp)
# # 通过key来获取 df
# df1 = fp['Sheet1']
# df2 = fp['Sheet2']
# print('df1:\n', df1)
# print('df2:\n', df2)
# print('*' * 100)

# 合并
# 横向堆叠 --->列的方向
# 在列的方向直接拼接，在行的方向，获取所有的行，在结果中没有对应的内容，用NaN来补齐
# res = pd.concat(objs=(df1, df2),  # 合并的数据对象
#                 axis=1,  # dataframe中axis=1表示列的方向
#                 join="outer",  # 外连接 --类似于并集
#                 )
# print('res:\n', res)

# # 在列的方向直接拼接，在行的方向，获取共同拥有的行
# res = pd.concat(objs=(df1, df2),  # 合并的数据对象
#                 axis=1,  # dataframe中axis=1表示列的方向
#                 join="inner",  # 内连接 ---类似于交集
#                 )
# print('res:\n', res)

# 纵向堆叠 ---行的方向
# 在行的方向直接拼接，在列的方向，获取所有的列，在结果中没有对应的内容，用NaN来补齐
# res = pd.concat(objs=(df1, df2),  # 合并的数据对象
#                 axis=0,  # dataframe中axis=1表示列的方向，axis=0,代表行的方向
#                 join="outer",  # 外连接 --类似于并集
#                 )
# print('res:\n', res)
# 在行的方向直接拼接，在列的方向，获取共同拥有的列
# res = pd.concat(objs=(df1, df2),  # 合并的数据对象
#                 axis=0,  # dataframe中axis=1表示列的方向，axis=0,代表行的方向
#                 join="inner",  # 内连接 ---类似于交集
#                 )
# print('res:\n', res)


# # append来进行纵向堆叠
# fp = pd.read_excel('./data/append直接拼接数据.xls', sheet_name=None, index_col=0)
# # print('fp:\n', fp)
#
# # 通过key来获取 df
# df1 = fp['Sheet1']
# df2 = fp['Sheet2']
# print('df1:\n', df1)
# print('df2:\n', df2)
# print('*' * 100)

# # 进行纵向堆叠
# # ignore_index=True ，无视原来的行索引，重新生成新的行索引
# all_df = df1.append(df2, ignore_index=True)
# print('all_df:\n', all_df)
