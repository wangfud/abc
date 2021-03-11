import numpy as np
import matplotlib.pyplot as plt

# 加载数据
fp = np.load('./data/国民经济核算季度数据.npz', allow_pickle=True)
print('fp:\n', fp)
# 遍历 获取key
for tmp in fp:
    print(tmp)

# 通过key获取数组
columns = fp['columns']
values = fp['values']

print('columns:\n', columns)
print('values:\n', values)

# 以2000-2017年各个产业增加总值散点图
# 1、创建画布
plt.figure()
# 默认不支持中文，需要修改参数，让其支持中文
plt.rcParams['font.sans-serif'] = 'SimHei'  # 雅黑字体
# 继续修改参数，让其继续支持负号
plt.rcParams['axes.unicode_minus'] = False

# 修改其他颜色RC
# 横轴字体颜色
# plt.rcParams['xtick.color'] = '#00F5FF'
# # 纵轴字体颜色
# plt.rcParams['ytick.color'] = '#00F5FF'
# # 背景颜色
# plt.rcParams['axes.facecolor'] = '#8B7355'
# # 边框颜色
# plt.rcParams['axes.edgecolor'] = '#00CD00'
# # 保存的画布颜色
# plt.rcParams['savefig.facecolor'] = '#8B1A1A'
# 2、绘制图形
# 准备横轴
# 横轴---时间 ---序号
x = np.arange(values.shape[0])

# 准备纵轴
y1 = values[:, 3]  # 第一产业
y2 = values[:, 4]  # 第二产业
y3 = values[:, 5]  # 第三产业
# 绘制散点图
# s ---表示的是点的大小，可以传递一个值，也可以传递一个序列，表示各个点的大小
# s = [5, 60]
# c ---表示点的颜色，可以传递一个值，也可以传递一个序列，表示各个点的颜色
# c = ['r', 'g', 'b', 'k']  # 注意：如果传递序列，序列长度必须点的个数相同
# marker ---点的样式
plt.scatter(x, y1, s=30, c='r', marker='*')
plt.scatter(x, y2, s=30, c='k', marker='o')
plt.scatter(x, y3, s=30, c='b', marker='d')

# 增加标题
plt.title('2000-2017年各个季度各个产业增加总值散点图', fontsize=8)
# 增加横轴名称
# plt.xlabel('时间')
# 增加纵轴名称
plt.ylabel('生产总值（亿元）', fontsize=8)
# 修改横轴刻度
# rotation=45 旋转45°
print(values[:, 1][::4])
plt.xticks(x[::4], values[:, 1][::4], rotation=45, fontsize=8)

# 设置纵轴刻度
plt.yticks(fontsize=8)
# 增加图例
legend = [tmp[:4] for tmp in columns[3:6]]

plt.legend(legend, loc='upper left', fontsize=8)

# 保存图片
plt.savefig('./png/2000-2017年各个季度各个产业增加总值散点图.jpg')

# 3、图形展示
plt.show()

# 散点图应用：
# 可以查看数据发展趋势
# 可以用来查看数据的分布
