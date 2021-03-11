import pandas as pd
import numpy as np

# 透视表
# 是plus版本的分组聚合。

# 创建dataframe
df = pd.DataFrame(
    data={
        'name': ['zs', 'ls', 'ww', 'zl', 'kk', 'jj', 'oo', 'yy', 'ee', 'ab', 'cb', 'mn'],
        'age': [18, 19, 18, 17, 16, 20, 19, 18, 17, 21, 22, 19],
        'hight': [170.5, 173.5, 173, 182.5, 183, 164, 168, 192, 177, 176.5, 175.5, 176],
        'cls_id': ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B'],
        'group_id': [1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2],
        'score': [99, 98, 85, 87, 83, 85.5, 96, 97, 98, 88, 90, 93.5]
    },
    index=['stu0', 'stu1', 'stu2', 'stu3', 'stu4', 'stu5', 'stu6', 'stu7', 'stu8', 'stu9', 'stu10', 'stu11']
)
print('df:\n', df)
print('df:\n', type(df))  # <class 'pandas.core.frame.DataFrame'>
print('*' * 100)

# 统计不同班级的平均成绩
# res = df.groupby(by='cls_id')['score'].mean()
# print('res:\n', res)

# 可以通过透视表实现
# # 可以 通过 pd.pivot_table 来创建透视表
# res = pd.pivot_table(
#     data=df,  # 用来创建透视表的dataframe数据
#     values='score',  # 针对的主体，进行统计指标的列
#     index='cls_id',  # 可以通过index来指定分组规则，可以指定最终结果的行索引
#     aggfunc=np.mean,  # values所对应的统计指标
# )
# print('res:\n', res)
# print('res:\n', type(res))  # <class 'pandas.core.frame.DataFrame'>

# 统计不同班级、不同小组，的成绩、身高、年龄的最大值
# res = df.groupby(by=['cls_id', 'group_id'])[['score', 'hight', 'age']].max()
# print('res:\n', res)
# print('*' * 100)
# 也可以通过透视表来实现
# res = pd.pivot_table(
#     data=df,  # 用来创建透视表的dataframe数据
#     values=['score', 'hight', 'age'],  # 针对的主体，进行统计指标的列
#     index=['cls_id', 'group_id'],  # 可以通过index来指定分组规则，可以指定最终结果的行索引
#     aggfunc=np.max,  # values所对应的统计指标
# )
# print('res:\n', res)
# print('res:\n', type(res))

# 既可以指定行索引，也可以指定列索引
res = pd.pivot_table(
    data=df,  # 用来创建透视表的dataframe数据
    values='score',  # 针对的主体，进行统计指标的列
    index='cls_id',  # 可以通过index来指定分组规则，可以指定最终结果的行索引
    columns='group_id',  # 可以通过columns来指定分组规则，可以指定最终结果的列索引
    aggfunc=np.mean,  # values所对应的统计指标
    # margins_name="All",  # 开关名称
    # margins=True,  # 开启开关
    # dropna=True, # 整列为空的数据，自动被过滤掉。
)
print('res:\n', res)
print('res:\n', type(res))
