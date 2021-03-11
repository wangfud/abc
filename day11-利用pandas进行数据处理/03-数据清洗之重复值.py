# 1、剔除整列全部一样的值
# （1）Python基础语言自定义函数来判定是否整列重复
# （2）set集合--具有去重功
# （3）drop_duplicates() 用来去重


# 2、如果多列数据的值相同这样的情况
# 如何判定两列数据相同？？？ ---bool数组
# 两列之间数据大部分相同？
# 两列之间存在强的关联性？
# corr() --用来计算相关性系数
# 相关性系数[-1,1]之间，[-1,0) ---负相关  (0,1]---正相关 0---不相关

import pandas as pd

# 加载数据
detail = pd.read_excel('./data/meal_order_detail.xls', sheet_name=0)
print('detail:\n', detail)

# 计算相关性系数
# method="pearson" --->默认计算的是皮尔逊相关系数
# {'pearson', 'kendall', 'spearman'}  ---相关性计算规则
corr = detail.loc[:, ['amounts', 'counts']].corr()
print('corr:\n', corr)

# 如果两列数据 --corr 的绝对值 接近于1，那么近乎完全相关，此时，可以剔除掉其中一列
# 局限性：只能用于数值型数据
