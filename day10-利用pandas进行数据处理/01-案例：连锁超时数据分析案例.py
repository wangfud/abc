import pandas as pd

# 设置pandas的显示
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# 加载数据
order = pd.read_csv('./data/order.csv', encoding='ansi')
print('order:\n', order.shape)

# 剔除销量中 <=0 的数据
# （1）删除法
# （2）保留法
# 确定bool数组
mask = order.loc[:, '销量'] > 0
# 保留筛选
order = order.loc[mask, :]

print('order:\n', order)
print('order:\n', order.columns)
print('order:\n', order.dtypes)
print('*' * 100)

# 1、哪些类别的商品比较畅销？
# 研究的是 商品类别 ---销量 之间的关系
# sort_values 默认为升序排序，ascending=False --->降序排序，如果为df，必须通过by指定按照某列的数据进行排序，
# 如果为series不需要指定by参数
# res = order.groupby(by='类别ID')['销量'].sum().sort_values(ascending=False).head(10)
# print('res:\n', res)

# 透视表
# res = pd.pivot_table(
#     data=order,
#     index='类别ID',
#     values='销量',
#     aggfunc='sum'
# ).sort_values(by='销量', ascending=False).head(10)
# print('res:\n', res)

# 2、哪些商品比较畅销？
# 研究的是商品id 和销量之间的关系
# res = order.groupby(by='商品ID')['销量'].sum().sort_values(ascending=False).head(10)
# print('res:\n', res)

# 透视表
# res = pd.pivot_table(
#     data=order,
#     index='商品ID',
#     values='销量',
#     aggfunc='sum'
# ).sort_values(by='销量', ascending=False).head(10)
# print('res:\n', res)


# # 3、求不同门店的销售额占比
#
# # 每个商品的销售额 = 单价 * 销量
#
# # （1）先确定单个商品的销售额
# order.loc[:, '销售额'] = order.loc[:, '销量'] * order.loc[:, '单价']
# print('order:\n', order)
#
# # (2) 研究的 不同门店 同 销售额之间的关系
# # 按照门店编号分组 统计 销售额的sum
# res = pd.pivot_table(
#     data=order,
#     index='门店编号',
#     values='销售额',
#     aggfunc='sum'
# )
# print('res:\n', res)
#
# print('不同门店的销售额占比为：\n', (res['销售额'] / res['销售额'].sum()).apply(lambda x: format(x, '.2%')))

# 4、哪段时间段是超市的客流高峰期？
# 不同时间段内 订单量的高峰期
# 查看哪个时间段内 ---不同的订单数目最多
# 每个小时算一个时间段
# 订单id --需要去重 ---多个商品对应一个订单
# （1）按照订单id对数据进行去重
# subset:可以指定按照某列进行去重
# inplace:如果为True,直接对原df产生影响，如果为False，那么会返回一个修改之后的df
# keep='first' :如果遇到重复的，保留第一个值，删除后续的
order.drop_duplicates(subset='订单ID', inplace=True)
# print('按照订单id去重之后的结果为：\n', order)

# (2) 获取时间属性
# 先转化为pandas支持的时间序列
order.loc[:, '成交时间'] = pd.to_datetime(order.loc[:, '成交时间'])
# 获取 hour属性
order.loc[:, 'hour'] = order.loc[:, '成交时间'].dt.hour
print('order:\n', order)

# (3)按照 hour进行分组，统计 订单ID 的count
res = pd.pivot_table(
    data=order,
    index='hour',
    values='订单ID',
    aggfunc='count'
).sort_values(by='订单ID', ascending=False)
print('res:\n', res)

# 8 9 10 点是 客流高峰期

