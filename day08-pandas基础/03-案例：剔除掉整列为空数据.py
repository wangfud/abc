import pandas as pd
import numpy as np

# 加载数据
detail = pd.read_excel('./data/meal_order_detail.xls', sheet_name=0)
print('detail:\n', detail)
print('detail:\n', detail.columns)
print('*' * 100)
print(detail.dtypes)

# # 构建一个list
# drop_list = []
#
# # 对每一列进行统计count指标
# for column in detail.columns:
#     if detail.loc[:, column].count() == 0:
#
#         drop_list.append(column)
#
# print(drop_list)
# # 删除掉整列为空的数据
# detail.drop(labels=drop_list, axis=1, inplace=True)
# print('剔除掉整列为空的数据的结果为：\n', detail)

# print(detail.loc[:, detail.count() != 0])
