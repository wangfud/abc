import pandas as pd

# 加载dataframe
users = pd.read_excel('./data/users.xls', sheet_name=0)

# 修改 users的行索引
index = ['index_' + str(i) for i in range(users.shape[0])]
users.index = index

print('users:\n', users)
print('users:\n', users.columns)

# 先列后行 ---直接索引方式
# 注意：数组arr[行,列] ---行、列同时索引
# 获取单列数据 -列名
# print('获取users里面的age列：\n', users['age'])
# 获取多列数据 --列名列表
# print('获取users里面的 NAME age poo 列：\n', users[['NAME', 'age', 'poo']])
# 获取多列数据
print('获取users里面的sex poo address age列：\n', detail[-4:]) # 获取的是行，而不是列

# 获取单列数据的指定行  --先获取单列，再进行行下标切片
# print('获取users里面的NAME 列前3行：\n', users['NAME'][:3])
# 获取单列数据的指定行  --先获取单列，再进行行名称切片，名称切片包含结束位置
# print('获取users里面的NAME 列前3行：\n', users['NAME']['index_0':'index_2'])
# 获取单列数据的指定行  --先获取单列，再进行行下标列表
# print('获取users里面的NAME 列前3行：\n', users['NAME'][[0,1,2]])
# 获取单列数据的指定行  --先获取单列，再进行行名称列表
# print('获取users里面的NAME 列前3行：\n', users['NAME'][['index_0','index_1','index_2']])
# 可以使用head来获取前n行
# print('获取users里面的NAME 列前3行：\n', users['NAME'].head(3))
# 可以使用tail来获取后n行
# print('获取users里面的NAME 列前3行：\n', users['NAME'].tail(3))

# 获取多列指定行
# print('获取users里面的 NAME sex  age列 前3行：\n',users[['NAME','sex','age']].head(3))
# print('获取users里面的 NAME sex  age列 前3行：\n',users[['NAME','sex','age']].tail(3))
# print('获取users里面的 NAME sex  age列 前3行：\n', users[['NAME', 'sex', 'age']][:3])
# print('获取users里面的 NAME sex  age列 前3行：\n', users[['NAME', 'sex', 'age']][:'index_2'])
# print('获取users里面的 NAME sex  age列 前3行：\n', users[['NAME', 'sex', 'age']][[0,1,2]]) # 错误的
# print('获取users里面的 NAME sex  age列 前3行：\n', users[['NAME', 'sex', 'age']][['index_0','index_1','index_2']]) # 错误的


# 同时索引--需要借助loc和iloc方法
# loc只能使用名称,不能使用下标
# 获取单列数据
# print('获取users里面的age列：\n', users.loc[:, 'age'])
# 获取单列的 前3行
# print('获取users里面的age列的前3行：\n', users.loc[:'index_2', 'age'])
# 获取多列的 前3行
# print('获取users里面的age poo NAME列的前3行：\n', users.loc[:'index_2', ['NAME', 'age', 'poo']])

# iloc只能使用下标，不能使用名称
# print('获取users里面的age列：\n', users.iloc[:, -1])
# print('获取users里面的age列：\n', users.iloc[:, 'age']) # 错误的
# 获取多列的指定行
# print('获取users里面 age poo NAME列 前10行：\n', users.iloc[:10, [3, -3, -1]])


# 直接索引---效率最高
# loc,iloc --效率比直接索引慢的， --推荐--
