import pandas as pd

# 加载数据
fp = pd.read_excel('./data/merge主键拼接数据.xls', sheet_name=None, index_col=0)
# print('fp:\n', fp)

# 先获取 Sheet1 Sheet2里面的dataframe
# df1 = fp['Sheet1']
# df2 = fp['Sheet2']
# print('df1:\n', df1)
# print('df2:\n', df2)
# print('*' * 100)

# 当左右两边df中函数有相同列名，且该列的值，大部分相同时的连接
# 按照key列的值对df1和df2进行合并
# how=outer,外连接， ---key列所有的值都拿过来进行合并
# res = pd.merge(left=df1,  # 左边的dataframe
#                right=df2,  # 右边的dataframe
#                on='key',  # 用来连接的列
#                how='outer',  # outer(外连接)、inner(内连接)、left(左外连接)、right(右外连接)
#                )
# print('res:\n', res)

# how=inner 内连接，拿取df1和df2中key列共同拥有的值进行合并
# res = pd.merge(left=df1,  # 左边的dataframe
#                right=df2,  # 右边的dataframe
#                on='key',  # 用来连接的列
#                how='inner',  # outer(外连接)、inner(内连接)、left(左外连接)、right(右外连接)
#                )
# print('res:\n', res)

# how=left 左连接，以左边的df为主，使用右边df来配合左边的df
# res = pd.merge(left=df1,  # 左边的dataframe
#                right=df2,  # 右边的dataframe
#                on='key',  # 用来连接的列
#                how='left',  # outer(外连接)、inner(内连接)、left(左外连接)、right(右外连接)
#                )
# print('res:\n', res)

# how=right 右连接,以右边的df为主，使用左边的df来配合右边的df
# res = pd.merge(left=df1,  # 左边的dataframe
#                right=df2,  # 右边的dataframe
#                on='key',  # 用来连接的列
#                how='right',  # outer(外连接)、inner(内连接)、left(左外连接)、right(右外连接)
#                )
# print('res:\n', res)

# 获取 Sheet3 Sheet4中的 dataframe
# df1 = fp['Sheet3']
# df2 = fp['Sheet4']
# print('df1:\n', df1)
# print('df2:\n', df2)
# print('*' * 100)

# 当左右两边df中的列名不相同，但存在某列的值大部分相同时的连接
# 拿取所有的Kx 和 Ky的值进行连接,如果左右df中没有对应的值，用NaN补齐
# res = pd.merge(left=df1,
#                right=df2,
#                how='outer',  #
#                left_on='Kx',  # 指定左边dataframe用来连接的列
#                right_on='Ky'  # 指定右边dataframe用来连接的列
#                )
# print('res:\n',res)
# 拿取Kx 和 Ky的共同拥有的值进行连接
# res = pd.merge(left=df1,
#                right=df2,
#                how='inner',  #
#                left_on='Kx',  # 指定左边dataframe用来连接的列
#                right_on='Ky'  # 指定右边dataframe用来连接的列
#                )
# print('res:\n', res)

# 拿取所有Kx的值进行连接，右边df来配合左df
# res = pd.merge(left=df1,
#                right=df2,
#                how='left',  #
#                left_on='Kx',  # 指定左边dataframe用来连接的列
#                right_on='Ky'  # 指定右边dataframe用来连接的列
#                )
# print('res:\n', res)
# 拿取所有Ky的值进行连接，左边df来配合右边df
# res = pd.merge(left=df1,
#                right=df2,
#                how='right',  #
#                left_on='Kx',  # 指定左边dataframe用来连接的列
#                right_on='Ky'  # 指定右边dataframe用来连接的列
#                )
# print('res:\n', res)

# df1 = fp['Sheet3']
# df2 = fp['Sheet5']
# print('df1:\n', df1)
# print('df2:\n', df2)
# print('*' * 100)
# #  当左右两个df中存在相同的列名，但是该列毫无关系，并且存在另外的列，列名不同，但是列里面的值大部分相同
# res = pd.merge(left=df1,
#                right=df2,
#                how='outer',  #
#                left_on='Kx',  # 指定左边dataframe用来连接的列
#                right_on='Ky',  # 指定右边dataframe用来连接的列
#                suffixes=("_x", "_yy"), # 如果两边dataframe中存在相同的列名时，合并之后，给结果中分别加上_x 和_y来区分列
#                )
# print('res:\n', res)

# 加载 Sheet6  Sheet7 中的dataframe
df1 = fp['Sheet6']
df2 = fp['Sheet7']
print('df1:\n', df1)
print('df2:\n', df2)
print('*' * 100)

# 当左右两个df中含有多列相同的列名，且里面值大部分相同，
# 此时连接时，可以使用多列相同进行连接
# res = pd.merge(left=df1,
#                right=df2,
#                how='outer',  #
#                on=['kk', 'kg'],
#                suffixes=("_x", "_yy"),  # 如果两边dataframe中存在相同的列名时，合并之后，给结果中分别加上_x 和_y来区分列
#                )
# print('res:\n', res)

# 主键连接 join
# df1.join()  #
