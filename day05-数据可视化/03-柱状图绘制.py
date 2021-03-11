import numpy as np
import matplotlib.pyplot as plt

# 柱状图---高低不等柱子组成的。
# 横轴一般表示不同的类别，纵轴一般表示为各个类别的数目
# 主要用于对比不同的类别，查看类别之间的差距
# 对比类别类别不宜过多，一般对比的类别数目少于9类的。
# 用于少量数据的对比

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

# 以2000、2017年第一季度各个产业、行业的对比
# 1、创建画布
fig = plt.figure()
# 默认不支持中文，需要修改参数，让其支持中文
plt.rcParams['font.sans-serif'] = 'SimHei'  # 雅黑字体
# 继续修改参数，让其继续支持负号
plt.rcParams['axes.unicode_minus'] = False

# 调整子图间距
plt.subplots_adjust(wspace=0.4, hspace=0.3)

# 2、绘制图形
fig.add_subplot(2, 2, 1)
# 2000年第一季度各个产业对比柱状图
# 准备数据
# 横轴
x = np.arange(3)
# 纵轴
y = values[0, 3:6]
# 绘制柱状图
# 参数1：横轴
# 参数2：纵轴
# 参数width：柱子宽度
# 参数color:指的是数字的颜色，可以给一个具体颜色值，也可以给一个arry_like
# 参数align='center'，柱子的位置，在刻度中心位置。
plt.bar(x, y, width=0.6, color=['r', 'g', 'b'])

# 增加标题
plt.title('2000年第一季度各个产业对比柱状图')
# 横轴名称
# plt.xlabel('产业')
# 纵轴名称
plt.ylabel('生产总值（亿元）')
# 修改横轴刻度
xticks = [tmp[:4] for tmp in columns[3:6]]
plt.xticks(x, xticks)

# 标注
# for i, j in zip(x, y):
#     plt.text(i, j, str(j), horizontalalignment='center')

fig.add_subplot(2, 2, 2)
# 2017年第一季度各个产业对比柱状图

fig.add_subplot(2, 2, 3)
# 2000年第一季度各个行业对比柱状图

fig.add_subplot(2, 2, 4)
# 2017年第一季度各个行业对比柱状图

# 保存图片
plt.savefig('./png/2000、2017年第一季度各个产业、行业对比柱状图.png')

# 3、图形展示
plt.show()
