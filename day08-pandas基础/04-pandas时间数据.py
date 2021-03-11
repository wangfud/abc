import pandas as pd

# numpy中的时间数据类型：datetime64[ns]
# pandas默认支持的时间点的类型:Timestamp
# pandas默认支持的时间序列类型：DatetimeIndex

# 加载数据
# detail = pd.read_excel('./data/meal_order_detail.xls', sheet_name=0)
# print('detail:\n', detail)
# print('detail:\n', detail.columns)
# print('detail:\n', detail.dtypes)

# 可以通过 pd.to_datetime 将时间字符串转化为pandas支持的时间点类型
# res = pd.to_datetime('2020-10-11')
# print('res:\n', res)
# print('res:\n', type(res))

# ['2020-10-11','2020-10-10','2020-10-09'] --时间字符串序列
# 可以通过  pd.to_datetime 将时间字符串序列转化为pandas支持的时间序列
# res = pd.to_datetime(['2020-10-11', '2020-10-10', '2020-10-09'])
# print('res:\n', res)
# print('res:\n', type(res))  # <class 'pandas.core.indexes.datetimes.DatetimeIndex'>
# 也可以通过 pd.DatetimeIndex将时间字符串序列转化为pandas支持的时间序列
# res = pd.DatetimeIndex(['2020-10-11', '2020-10-10', '2020-10-09'])
# print('res:\n', res)
# print('res:\n', type(res))

# 可以使用列表推导式从pandas支持的时间序列中获取时间属性
# detail.loc[:, 'place_order_time'] = pd.to_datetime(detail.loc[:, 'place_order_time'])
# print(detail.loc[:, 'place_order_time'])

# # 获取时间属性
# # 获取 place_order_time 年属性
# year = [tmp.year for tmp in detail.loc[:, 'place_order_time']]
# print('year:\n', year)
# # 获取 place_order_time 月属性
# month = [tmp.month for tmp in detail.loc[:, 'place_order_time']]
# print('month:\n', month)
# # 获取 place_order_time 时属性
# hour = [tmp.hour for tmp in detail.loc[:, 'place_order_time']]
# print('hour:\n', hour)
# # 获取 place_order_time  季度属性
# quarter = [tmp.quarter for tmp in detail.loc[:, 'place_order_time']]
# print('quarter:\n', quarter)
# # 获取 place_order_time 日期属性
# date = [tmp.date() for tmp in detail.loc[:, 'place_order_time']]
# print('date:\n', date)
#
# # 获取 place_order_time 时间属性
# time = [tmp.time() for tmp in detail.loc[:, 'place_order_time']]
# print('time:\n', time)

# # 可以通过dt来获取时间属性
# year = detail.loc[:, 'place_order_time'].dt.year
# print('year:\n', year)
#
# month = detail.loc[:, 'place_order_time'].dt.month
# print('month:\n', month)
#
# date = detail.loc[:, 'place_order_time'].dt.date
# print('date:\n', date)
#
# time = detail.loc[:, 'place_order_time'].dt.time
# print('time:\n', time)

# 计算时间差  ----Timedelta
# res = pd.to_datetime('2020-10-11') - pd.to_datetime('1999-11-2')
# res = pd.to_datetime('2020-10-11') - pd.to_datetime('1998-12-19')
# print('res:\n', res.days)
# print('res:\n', type(res))  # <class 'pandas._libs.tslibs.timedeltas.Timedelta'>

# 可以计算时间推移
# [weeks, days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds]
# res = pd.to_datetime('2020-10-11') - pd.Timedelta(days=5)
# res = pd.to_datetime('2020-10-11') - pd.Timedelta(hours=5)
# res = pd.to_datetime('2020-10-11') - pd.Timedelta(years=2) # 错误的
# print('res:\n', res)

# 可以创建时间序列
# start ---开始
# end ---结束
# periods  ----序列长度
# res = pd.date_range(start='2019-10-11',
#                     # end='2020-10-11',
#                     periods=500,
#                     freq='M'
#                     )
# print('res:\n', res)


# print('获取最小时间：',pd.Timestamp.min)
# print('获取最大时间：',pd.Timestamp.max)
