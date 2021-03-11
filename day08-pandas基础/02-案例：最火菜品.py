import pandas as pd
import numpy as np

# 加载数据
detail = pd.read_excel('./data/meal_order_detail.xls', sheet_name=0)
print('detail:\n', detail)
print('detail:\n', detail.columns)
print('*' * 100)

# # 可以对 dishes_name 的统计众数、及众数出现的次数
# 哪个菜品出场最多，以及出场次数
# print('最火菜品及出现的次数：\n', detail.loc[:, 'dishes_name'].describe())

# 需要剔除  白饭/大碗  再去进行统计剩下的菜品的众数及出现的次数
# # （1） 确定bool数组
# mask = detail.loc[:, 'dishes_name'] == '白饭/大碗'
# #  (2) 确定 行名称
# drop_index = detail.loc[mask, :].index
# # （2）删除 白饭/大碗
# detail.drop(labels=drop_index, axis=0, inplace=True)
# print('剔除掉白饭/大碗之后的数据：\n',detail)


# 保留 非白饭/大碗 的菜品
# （１）确定bool数组
mask = detail.loc[:, 'dishes_name'] != '白饭/大碗'

# （2） 保留非白饭/大碗的数据
detail = detail.loc[mask, :]

# 可以对 dishes_name 的统计众数、及众数出现的次数
print('最火菜品及出现的次数：\n', detail.loc[:, 'dishes_name'].describe()['top'])
print('最火菜品及出现的次数：\n', detail.loc[:, 'dishes_name'].describe()['freq'])
