# TGI ---Target Group Index（目标群体指数），
# 可反映目标群体在特定 研究范围(如地理区域、人口统计领域、媒体受众、产品消费者)内的强势或弱势。

# TGI指数计算：
# [目标群体中具有某一特征的群体所占比例/总体中具有相同特征的群体所占 比例]*标准数 100

# TGI 指数表征不同特征用户关注问题的差异情况

# TGI 指数等于 100 表示平均水平，
# 高于 100，代表该类用户对某类问题的关注程度高于整体水平。


import pandas as pd
import numpy as np

# 加载数据
data = pd.read_excel('./data/TGI指数案例数据.xls', sheet_name=0)
# print('data:\n', data)
# print('data:\n', data.columns)
# print('*' * 100)

# 要进行分析订单数据，必须保证所有的订单都是交易成功状态
res_counts = pd.value_counts(data.loc[:, '订单状态'])
# print('res_counts:\n', res_counts)

#  交易成功                 27792
# 付款以后用户退款成功，交易自动关闭     1040
# Name: 订单状态, dtype: int64

# 剔除 订单状态中为： 付款以后用户退款成功，交易自动关闭 的1040条数据
# (1)删除法
# 确定bool数组
mask = data.loc[:, '订单状态'] == '付款以后用户退款成功，交易自动关闭'
# 确定要删除的行索引
drop_index = data.loc[mask, :].index
# 删除
data.drop(labels=drop_index, axis=0, inplace=True)
print('data:\n', data)
print('data:\n', data.columns)
print('*' * 100)
# (2)保留法
# pass 自己完成

# 1、单个用户平均支付金额
# 思路1：--->各个用户的支付金额
# 思路2：--->计算实付金额的sum / 对用户名称去重 的数量 --->人均消费
# 按照买家分组，求各个买家的 实付金额 的sum  --认为用户昵称是严格区分不同用户
res_sum = data.groupby(by='买家昵称')['实付金额'].sum()
# print('res_sum:\n', res_sum)

# 将res_sum 转化为 dataframe
df = pd.DataFrame(data=res_sum.values,
                  index=res_sum.index,
                  columns=['支付总金额（个人）']
                  )


# print('df:\n', df)


# 2、基于用户支付金额，判断用户是属于低客单还是高客单
# 什么是高客单？ 什么是低客单？
# 用来区分高客单、低客单的中间的阈值：中位数、均值、自定义一个数
def func_gaokedan(val):
    """
    判定是否为高客单客户
    :param val: 数据
    :return: 高客单/低客单
    """
    if val >= 50:
        return '高客单'
    else:
        return '低客单'


df.loc[:, '客单类型'] = df.loc[:, '支付总金额（个人）'].transform(func_gaokedan)
# print('df:\n', df)
# print('*' * 100)

# 对df进行重设索引 ---将原来的行索引变为一列数据---即此时将买家昵称变为数据
df = df.reset_index()
# print('df:\n', df)

# 思路：每个单独的买家 ---所对应一个省份、城市
# 去重
# subset : 指定按照某列、某几列进行去重
# inplace：是否对原数据产生影响
data.drop_duplicates(subset='买家昵称', inplace=True)
# print('data:\n',data)

# 按照 买家昵称 将data中的 省份、城市 添加到 df中去
# # 数据合并
df = pd.merge(left=df, right=data.loc[:, ['买家昵称', '省份', '城市']], on='买家昵称', how='inner')
print('df:\n', df)

# df.to_excel('./data/aaa.xls')
#
# # 3、用透视表的方法来统计每个省市低客单、高客单人数
res_pivot = pd.pivot_table(data=df,
                           index=['省份', '城市'],
                           columns='客单类型',
                           values='买家昵称',
                           aggfunc='count'
                           )
# # 重设索引
res_pivot = res_pivot.reset_index()
print('res_pivot:\n', res_pivot)
print('*' * 100)
#
# # 4、计算总人数，以及每个城市对应的高客单占比
res_pivot.loc[:, '总人数'] = res_pivot.loc[:, '低客单'] + res_pivot.loc[:, '高客单']
# 占比
res_pivot.loc[:, '高客单占比'] = res_pivot.loc[:, '高客单'] / res_pivot.loc[:, '总人数']
print('res_pivot:\n', res_pivot)
#
# # 5、计算全国总体高客单人数占比
all_china = res_pivot.loc[:, '总人数'].sum()
gaokedan_city = res_pivot.loc[:, '高客单'].sum()
# 全国高客单占比
percent_china = gaokedan_city / all_china
print('全国高客单占比为：\n', percent_china)
print('*' * 100)

# # 6、计算每个城市高客单 TGI 指数
# # # [目标群体中具有某一特征的群体所占比例/总体中具有相同特征的群体所占 比例]*标准数 100

res_pivot.loc[:, 'TGI_city'] = res_pivot.loc[:, '高客单占比'] / percent_china * 100

print('res_pivot:\n', res_pivot)

# # TGI指数 > 100 说明该城市的用户对于 该品牌比较热爱的。
# # 如果想要开店，还需要考虑用户群体数量
# # 考虑 各个城市用户数量 > 2000的，再去判断TGI指数

# 筛选出 用户数量 大于500的城市
# 确定bool数组
mask = res_pivot.loc[:, '总人数'] > 500
# 筛选
all_df = res_pivot.loc[mask, :]
# 重设索引
all_df = all_df.reset_index().drop(labels='index', axis=1, inplace=False)

print('all_df:\n', all_df)

# 再去筛选出 TGI指数 > 100的城市
# 确定bool数组
bool_mask = all_df.loc[:, 'TGI_city'] > 100
# 筛选
res = all_df.loc[bool_mask, '城市'].values

print('res:\n', res)
