import pandas as pd
import numpy as np

# 加载detail,并合并数据
fp = pd.read_excel('./data/meal_order_detail.xls', sheet_name=None)
print('fp:\n', fp.keys())

# 获取dataframe
detail1 = fp['meal_order_detail1']
detail2 = fp['meal_order_detail2']
detail3 = fp['meal_order_detail3']
# print('detail1:\n', detail1)
# print('*' * 100)
# print('detail2:\n', detail2)
# print('*' * 100)
# print('detail3:\n', detail3)

# 合并
detail = pd.concat(objs=(detail1, detail2, detail3), axis=0, join='outer', ignore_index=True)

# print('detail:\n', detail)
# print('*' * 100)

# 加载info
info = pd.read_csv('./data/meal_order_info.csv', encoding='ansi')
# print('info:\n', info)

# 主键连接
all_df = pd.merge(left=detail, right=info, left_on='order_id', right_on='info_id', how='inner')
# print('all_df:\n', all_df)
# print('all_df:\n', all_df.columns)
# print('*' * 100)

# 判定 emp_id_x  emp_id_y？？？是否一样  ---一样
# flag = np.all(all_df.loc[:, 'emp_id_x'] == all_df.loc[:, 'emp_id_y'])
# print('flag:\n', flag)

# 加载users 与 all_df 进行合并
users = pd.read_excel('./data/users.xls', sheet_name=0)

# 合并
all_df = pd.merge(left=all_df, right=users, left_on='name', right_on='ACCOUNT', how='inner')
# print('all_df:\n', all_df)
# print('all_df:\n', all_df.columns)

# 判断 phone TEL是否一样 ---不一样
# flag = np.all(all_df.loc[:, 'phone'] == all_df.loc[:, 'TEL'])
# print('flag:\n', flag)

# emp_id_x  emp_id_y一样的，order_id info_id一样的， ACCOUNT name一样
all_df.drop(labels=['emp_id_y', 'order_id', 'ACCOUNT'], axis=1, inplace=True)
print('all_df:\n', all_df.shape)
# print('all_df:\n', all_df)
# print('all_df:\n', all_df.columns)

# drop_list = []
# # 还有整列为空的---剔除
# for column in all_df.columns:
#     if all_df.loc[:, column].count() == 0:
#         drop_list.append(column)
#
# print('整列为空的数据有：\n', drop_list)
# # 剔除
# all_df.drop(labels=drop_list, axis=1, inplace=True)
# print('all_df:\n', all_df.shape)
# print('all_df:\n', all_df.columns)

# 整列值都一样的---剔除
# （1）可以使用value_counts --->返回值，判断长度如果为1，则全部一样
# （2）获取每一列的第一个值，与整列数据进行对比，返回bool数组，然后再利用逻辑运算np.all判断返回值，如果为True，则全部一样
# （3）求众数，众数的出现的次数 等于 行数，--全部一样
# （4）df.drop_duplicates()
drop_list = []

for column in all_df.columns:
    # 按照每一列进行去重
    res = all_df.drop_duplicates(subset=column, inplace=False)
    # 如果去重之后返回的res只有一行，那意味着该列数据全部一样
    if res.shape[0] == 1:
        drop_list.append(column)

print('drop_list:\n', drop_list)
# 剔除
all_df.drop(labels=drop_list, axis=1, inplace=True)
print('all_df:\n', all_df.shape)
print('all_df:\n', all_df.columns)
