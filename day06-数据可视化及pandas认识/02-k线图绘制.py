# 安装tushare
# pip install tushare

# 安装mpl_finance
# pip install mpl_finance

import tushare as ts
import mpl_finance as mpf
import matplotlib.pyplot as plt
import numpy as np

# 获取股票交易数据
data = ts.get_k_data(code='600728',  # 股票代码
                     ktype='D',  # 每个交易日，
                     start='2018-11-01',  # 开始日期
                     autype='qfq'
                     )
print('data:\n', data)
print('data:\n', type(data))  # <class 'pandas.core.frame.DataFrame'>

# 绘图
# 1、创建画布
fig = plt.figure()
# 默认不支持中文，需要修改参数，让其支持中文
plt.rcParams['font.sans-serif'] = 'SimHei'  # 雅黑字体
# 继续修改参数，让其继续支持负号
plt.rcParams['axes.unicode_minus'] = False

# 添加坐标系
# 参数： [left, bottom, width, height]
# 返回坐标系对象
ax = fig.add_axes([0.1, 0.2, 0.8, 0.6])

# 构建 quotes
# (time, open, high, low, close)
# time ---使用序号来代替
t = np.arange(data.shape[0]).reshape((-1, 1))
# print('t:\n', t)

# 获取 ohlc数据 --并转化为ndarray
d = data[['open', 'high', 'low', 'close']].values
# print('d:\n', d)
# print('d:\n', type(d))

# 合并序号 和 数据
quotes = np.concatenate((t, d), axis=1)
print('quotes:\n', quotes)
# 2、绘图
# ax :坐标系
# quotes：数据
# width=0.2： k线图中每一个具体的小蜡烛的宽度
# colorup='r',  # 涨的颜色
# colordown='g' # 下跌的颜色
mpf.candlestick_ohlc(ax, quotes=quotes, width=0.5, colorup='r', colordown='g')

# 设置标题
plt.title('k线图')

# 3、展示
plt.show()
