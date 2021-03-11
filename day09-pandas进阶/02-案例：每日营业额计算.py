# 以detail表为例，
# 计算表中订单 ----每日营业额
# 存在 place_order_time
# counts(数量) amounts(单价)

import pandas as pd

# 加载数据
detail = pd.read_excel('./data/meal_order_detail.xls', sheet_name=0)
# print('detail:\n', detail)
# place_order_time  counts amounts列
# 单个菜品的收入 = 单价 * 数量
# (1)先计算 单个菜品的收入
detail.loc[:, 'income'] = detail.loc[:, 'amounts'] * detail.loc[:, 'counts']

# (2) 准备时间数据
# 转化为pandas默认支持的时间序列
detail.loc[:, 'place_order_time'] = pd.to_datetime(detail.loc[:, 'place_order_time'])
# 获取日期属性
detail.loc[:, 'day'] = detail.loc[:, 'place_order_time'].dt.date

# print(detail)
# (3) 按照日期 进行分组，统计income的和
res = detail.groupby(by='day')['income'].sum()
print('res:\n',res)
