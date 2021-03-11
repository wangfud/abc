import pandas as pd
import numpy as np

# 设置pandas的显示
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# 加载数据
data = pd.read_excel('./data/某医院2018年数据.xls', sheet_name=0)
# print('data:\n', data)
# print('data:\n', data.columns)

# 数据处理
# （1）修改列索引
data.rename(columns={'购药时间': '成交时间'}, inplace=True)
# print('列索引：\n', data.columns)
# print('*' * 100)
# （2）删除所有空值的数据
# a、检测缺失值
res_null = pd.isnull(data).sum()
# print('检测缺失值结果为：\n', res_null)
# b、删除缺失值
data.dropna(axis=0, how='any', inplace=True)
# print('剔除缺失值之后的结果为：\n', data.shape)
# print('*' * 100)

# （3） 将'销售数量', '应收金额', '实收金额'数据类型转换为 int
data.loc[:, ['销售数量', '应收金额', '实收金额']] = data.loc[:, ['销售数量', '应收金额', '实收金额']].astype(np.int32)


# print('数据类型：\n', data.dtypes)


# （4）删除'销售数量', '应收金额', '实收金额'中小于等于 0 的数据
# # 思路1：bool数组
# mask1 = data.loc[:, '销售数量'] > 0
# mask2 = data.loc[:, '应收金额'] > 0
# mask3 = data.loc[:, '实收金额'] > 0
#
# # 需要同时满足 '销售数量', '应收金额', '实收金额' >0
# mask = mask1 & mask2 & mask3
#
# # 筛选
# data = data.loc[mask, :]
# print('剔除小于0的数据的结果为：\n',data)

# 思路2：设定阈值，使用具体业务法来剔除 < 0的数据
def juti_yewu(data):
    """
    根据具体业务法剔除异常值 ---'销售数量', '应收金额', '实收金额'
    :param data: Series
    :return: mask--bool数组
    """
    # 下限
    low = 0
    # 比较
    mask = data > low

    return mask


# 调用
mask1 = juti_yewu(data.loc[:, '销售数量'])
mask2 = juti_yewu(data.loc[:, '应收金额'])
mask3 = juti_yewu(data.loc[:, '实收金额'])
# 同时满足 '销售数量', '应收金额', '实收金额' >0
mask = mask1 & mask2 & mask3
# 筛选
data = data.loc[mask, :]


# print('剔除小于0的数据的结果为：\n', data)


# （5）'成交时间'特征转标准时间格式
def get_date(val):
    """
    获取时间数据
    :param val: 数据
    :return: 数据
    """
    # 先拆分
    val = val.split(' ')[0]
    # 有 异常数据 --->替换为正常数据
    if val == '2018-02-29':
        val = '2018-02-28'
    # 转化
    val = pd.to_datetime(val)

    return val


# 使用transform调用自定义函数
data.loc[:, '成交时间'] = data.loc[:, '成交时间'].transform(get_date)
print('data:\n', data)
# print('data:\n', data.dtypes)
print('data:\n', data.columns)
print('*' * 100)

# 分析需求：
# （1）每个月的人流量？
# 计算每个月的人数
# 先获取时间数据
data.loc[:, 'month'] = data.loc[:, '成交时间'].dt.month
print('data:\n', data)
# 按照 月 进行分组，统计 社保卡号的 数量
df = pd.pivot_table(
    data=data,
    index='month',
    values='社保卡号',
    aggfunc='count'
).rename(columns={'社保卡号': '人数'}, inplace=False).reset_index()
print('df:\n', df)

# (2) 人均平均消费？
# 消费总额 / 总的人数 = 人均消费
# 先计算 消费总额
all_income = data.loc[:, '实收金额'].sum()
# 计算人数
# 先按照 社保卡号 去重
all_p_num = data.drop_duplicates(subset='社保卡号', inplace=False).shape[0]
print('总人数为：%d 个' % all_p_num)
# 计算人均消费
avg_income = all_income / all_p_num

print('人均消费为：%.2f' % avg_income)
print('*' * 100)

# （3）使用最频繁的前十种药品？
# 按照药品名称进行分组，统计 各个药品的销量 之和
all_df = pd.pivot_table(
    data=data,
    index='商品名称',
    values='销售数量',
    aggfunc='sum'
).sort_values(by='销售数量', ascending=False).reset_index().head(10)
print('all_df:\n', all_df)

# (4) 多少人办社保卡？
#  如果没有社保卡，会给一个临时的卡号
#  如果有社保卡，那么使用自己的社保卡
# 提出要求：有社保卡的话有优惠
# 确定bool数组
bool_mask = data.loc[:, '应收金额'] > data.loc[:, '实收金额']
# 筛选数据
data = data.loc[bool_mask, :]
# 此时对社保数据 data 按照社保卡号进行去重
shebao_p_num = data.drop_duplicates(subset='社保卡号', inplace=False).shape[0]

print('具有社保卡号的人有：%d 个' % shebao_p_num)
