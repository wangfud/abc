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

#
# # 统计整个的最高分
# print('最高分为：', df.loc[:, 'score'].max())
# print('最低分为：', df.loc[:, 'score'].min())
# print('平均分为：', df.loc[:, 'score'].mean())

# 按照单列进行分组，统计单列的指标
# 统计各个班级的成绩的最大值、最小值、平均值
# 按照cls_id进行分组，统计各个组内的score的最大值、最小值、平均值
# 可以使用groupby进行分组
# res = df.groupby(by='cls_id')
# print('res:\n', res) # groupby会返回一个分组之后的对象
# res = df.groupby(by='cls_id')['score'].max()
# print('res:\n', res)


# 按照多列分组，统计单列指标
# 统计不同班级、不同小组的 成绩的最大值
# 先按照cls_id进行分组，再按照group_id进行分组，然后再去统计score的最大值
# res = df.groupby(by=['cls_id','group_id'])['score'].max()
# print('res:\n',res)

# 按照单列分组，统计多列指标
# # 统计不同班级成绩、身高、年龄的最大值、最小值、均值
# # 按照cls_id进行分组，再去统计 score hight age 的最大值、最小值、均值
# # res = df.groupby(by='cls_id')[['score','hight','age']].max()
# res = df.groupby(by='cls_id')[['score', 'hight', 'age']].min()
# # res = df.groupby(by='cls_id')[['score','hight','age']].mean()
# print('res:\n', res)

# 按照多列进行分组，统计多列指标
# 统计不同班级、不同小组内的 成绩、身高、年龄的最大值、最小值、均值
# res = df.groupby(by=['cls_id','group_id'])[['score','hight','age']].max()
# print('res:\n',res)

# 思路
# res = df[['score','hight','age']].groupby(by=df['cls_id']).max()
# print('res:\n',res)


# 对不同的列，求取不同指标
# 对身高统计最大值、对成绩统计平均值
# 可以借助agg ， agg = aggregate 一样的
# res = df.agg({'hight': [np.max], 'score': [np.mean]})
# print('res:\n',res)
# 也可以先分组，再对组内的不同列求取不同的指标
# res = df.groupby(by='cls_id').agg({'hight': [np.max], 'score': [np.mean]})
# print('res:\n', res)

# 对不同的列，求取不同个数的指标
# 对身高统计最大值、均值，对成绩统计最小值
# res = df.agg({'hight': [np.max, np.mean], 'score': [np.min]})
# print('res:\n', res)

# 对多列求取多个指标
# 对年龄、身高、成绩同时统计最大值、最小值、和
# res = df.loc[:, ['age', 'hight', 'score']].agg([np.max, np.min, np.sum])
# print('res:\n', res)

# 可以使用自定义函数
# 可以使用匿名的自定义函数
# res = df['age'].agg(lambda x: x + 1)
# print('res:\n',res)

# 可以使用有名称的函数
# def func(x):
#
#     return x + 1
#
# res = df['age'].agg(func)
# print('res:\n', res)

# 加载 users
users = pd.read_excel('./data/users.xls', sheet_name=0)

print('users:\n', users)


def func(x):
    """
    自定义判断是否保存广东
    :param x: 数据
    :return: True
    """
    print('----x:\n', x)  # 元素
    if str(x).__contains__('广东'):
        res = True
    else:
        res = False

    return res

    # x --->整列数据
    # res_list = []
    # for tmp in x:
    #     if str(tmp).__contains__('广东'):
    #         res = True
    #     else:
    #         res = False
    #     # 添加
    #     res_list.append(res)
    #
    # return res_list

res = users.loc[:, 'poo'].agg(func)
print('res:\n', res)

# def func(x):
#     '''
#     自定义求和
#     :param x: 数据
#     :return:
#     '''
#     # x ---> 传进来的每一个序列的里面的各个元素
#     print('x:', x)
#     return x + 1


# 也可以使用transform进行自定义函数
# res = df.loc[:, 'age'].transform(func)
# print('res:\n', res)

# 也可以使用apply进行自定义函数
# res = df.loc[:, 'age'].apply(func)
# print('res:\n', res)

def func(x):
    """
    :param x:
    :return:
    """
    print('----',x)
    return np.sum(x)

# transform 和 apply区别
res = df.groupby(by='cls_id')['hight'].transform(func)  # 推荐
# res = df.groupby(by='cls_id')['hight'].apply(func)
print('res:\n', res)

# 传递元素---整列传递进行---针对于所有元素同时操作