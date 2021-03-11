# 交叉表
# 交叉表是一种特殊的透视表，主要用于计算分组频率

import pandas as pd
import numpy as np

#
# 创建df
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

# 可以使用 pd.crosstab 创建交叉表
# res = pd.crosstab(
#     index=df['cls_id'],  # 指定某列为行索引
#     columns=df['group_id'],  # 指定某列为列索引
# )
# print('res:\n', res)

# 满足index、columns进行分组之后，结果的频率

# # 注意:index columns必须同时出现
# # 注意：values aggfunc必须同时出现
# # 也能完成分组聚合
# res = pd.crosstab(
#     index=df['cls_id'],  # 指定某列为行索引
#     columns=df['group_id'],  # 指定某列为列索引
#     values=df['score'],  # 针对的主体，即统计指标的列
#     aggfunc=np.max,  # 统计的指标
# )
# print('res:\n', res)
