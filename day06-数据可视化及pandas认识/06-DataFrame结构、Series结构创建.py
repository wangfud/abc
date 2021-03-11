import pandas as pd
import numpy as np

# 可以使用 pd.DataFrame来创建DataFrame结构
# 1、将大字典转化为df
# df = pd.DataFrame(
#     data={
#         'name': ['zs', 'ls', 'ww'],
#         'age': [16, 17, 16],
#         'group': [1, 2, 1]
#     },
#     index=['stu0', 'stu1', 'stu2']
# )
# print('df:\n', df)
# print('df:\n', type(df))  # <class 'pandas.core.frame.DataFrame'>

# 2、可以将列表嵌套转化为df
df = pd.DataFrame(
    data=[['zs', 16, 1],
          ['ls', 17, 2],
          ['ww', 16, 1]],
    index=['stu0', 'stu1', 'stu2'],  # 行索引
    columns=['name', 'age', 'group']
)
print('df:\n', df)
print('df:\n', type(df))

# # 加载.npz数据
# fp = np.load('./data/国民经济核算季度数据.npz', allow_pickle=True)
# print('fp:\n', fp)
# # 遍历获取key
# for tmp in fp:
#     print(tmp)
#
# # 通过key来获取数组
# columns = fp['columns']
# values = fp['values']
# print('columns:\n', columns)
# print('values:\n', values)
#
# # 构建index
# index = ['index_' + str(i) for i in range(values.shape[0])]
# print('index:\n', index)
#
# # 3、也可以将二维的ndarray转化为df
# df = pd.DataFrame(data=values,
#                   index=index,
#                   columns=columns,  # 列索引
#                   )
# print('df:\n',df)
# print('df:\n',type(df))

# 可以使用pd.Series来创建一个Series结构
# 1、可以将简单列表转化为Series
# se = pd.Series(data=['zs', 'ls', 'ww'],
#                index=['stu0', 'stu1', 'stu2']  # 行索引
#                )
# print('se:\n', se)
# print('se:\n', type(se))  # <class 'pandas.core.series.Series'>

# 2、可以将一维ndarray转化为Series
# se = pd.Series(data=np.array(['zs', 'ls', 'ww']),
#                index=['stu0', 'stu1', 'stu2']  # 行索引
#                )
# print('se:\n', se)
# print('se:\n', type(se))  # # <class 'pandas.core.series.Series'>

# 3、可以将字典转化为Series
# se = pd.Series(
#     data={'zs': 95, 'ls': 89, 'ww': 91},
#     index=['zs', 'ls', 'ww', 'zl']
# )
# print('se:\n', se)
# print('se:\n', type(se))

# 可以通过获取DataFrame中单列数据，来得到Series结构
# 4、获取dataframe中一列数据
se = df['name']
print('se:\n', se)
print('se:\n', type(se))
