import pandas as pd

# 加载数据
users = pd.read_excel('./data/users.xls', sheet_name=0)
print('users:\n', users)

# 新增加一列
# users['next_year_age'] = 18
# print('users:\n', users)
# 如果整列数据相同，对分析结果来说，此列对于结果的区分，无意义

# 增加一列的时候，都是通过在已知数据中进行计算 得到新的列
# users.loc[:, 'next_year_age'] = users['age'] + 1
# print('users:\n', users)

# 增加一列数据的意义：给数据集中各个数据对象增加一个新的属性值
