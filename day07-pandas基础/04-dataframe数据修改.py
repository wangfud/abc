import pandas as pd
import numpy as np

# 加载数据
users = pd.read_excel('./data/users.xls', sheet_name=0)
print('users:\n', users)

# 修改
# users.loc[:, 'age'] = 18
# print('users:\n', users)

# 满足条件的才进行修改
# 将 sex 里面 性别为 男 的这些数据的 age  修改为18岁
# # (1) 确定哪些数据是满足条件的？
# bool_mask = users.loc[:, 'sex'] == '男'
# print('bool_mask:\n', bool_mask)
# # (2)将满足条件的 进行修改
# users.loc[bool_mask, 'age'] = 18
# print('users:\n', users)

# 将 users里面的 age 为 奇数的年龄 修改为18岁
# bool_mask = users.loc[:, 'age'] % 2 == 1
# users.loc[bool_mask, 'age'] = 18
#
# print('users:\n', users)

# bool_mask = []
print(type(users.iloc[1,-3]))
# print(users['poo'].find('广东')==1)
#
# 将poo中广东 的 age 修改为18岁
bool_mask = []
for i in range(users.shape[0]):
    # i :代表行下标
    if type(users.iloc[i, -3]) != float:
        if users.iloc[i, -3].find('广东') != -1:
            bool_mask.append(True)
        else:
            bool_mask.append(False)
    else:
        bool_mask.append(False)
# 转化为一维数组
bool_mask = np.array(bool_mask)
# 修改
users.loc[bool_mask, 'age'] = 18
#
# print('users:\n', users)

print(np.nan)
print(type(np.nan))