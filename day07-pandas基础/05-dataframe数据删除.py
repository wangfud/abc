import pandas as pd
import numpy as np

# 加载数据
users = pd.read_excel('./data/users.xls', sheet_name=0)
print('users:\n', users)
print('*' * 100)

# 可以借助drop方法进行删除数据
# labels: 要删除的行名称列表、列名称列表
# axis: 如果要删除指定的行，此时axis=0,如果要删除指定的列，此时axis=1
# inplace:如果为True,直接对原df进行修改,如果为False，不会对原df产生修改，会返回一个新的修改之后的df
# users.drop(labels=['age', 'poo'], axis=1, inplace=True)
# res= users.drop(labels=['age', 'poo'], axis=1, inplace=False)
# users.drop(labels=[0, 1, 2, 3, 4], axis=0, inplace=True)
# print('users:\n', users)
# print('res:\n',res)

# # 删除法
# # 将users中 sex中 男性 全部删除掉
# (1) 确定bool数组
bool_mask = users.loc[:, 'sex'] == '男'
# (2) 确定 行名称
drop_index = users.loc[bool_mask, :].index
# (3)删除
users.drop(labels=drop_index, axis=0, inplace=True)
# print('删除之后的结果：\n', users)

# # 保留法
# 保留非男性的数据
# (1) 确定bool数组
bool_mask = users.loc[:, 'sex'] != '男'
# (2) 筛选
users = users.loc[bool_mask, :]
# print('保留法的结果为：\n',users)
