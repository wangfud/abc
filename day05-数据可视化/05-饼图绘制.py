import numpy as np
import matplotlib.pyplot as plt

# 饼图：将各部分数据绘制一张饼中，用来表示整体与部分、部分与部分之间的占比关系
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

# 以2017年第一季度各个产业占比
# 1、创建画布
plt.figure()
# 默认不支持中文，需要修改参数，让其支持中文
plt.rcParams['font.sans-serif'] = 'SimHei'  # 雅黑字体
# 继续修改参数，让其继续支持负号
plt.rcParams['axes.unicode_minus'] = False

# 2、绘制图形
# 准备数据
x = values[-1, 3:6]
# explode :表示的各部分扇形距离中心的距离
explode = (0.01, 0.01, 0.02)
# labels: 各部分扇形的名称
labels = [tmp[:4] for tmp in columns[3:6]]
# colors:表示颜色
colors = ['r', 'g', 'b']
# autopct :表示占比的显示
autopct = '%.2f%%'
# pctdistance: 占比显示距离中心的半径，默认为0.6个半径
# shadow ：阴影
shadow = True
# labeldistance: 标签距离中心的半径，默认为1.1个半径
# radius：半径的大小，默认为1
# wedgeprops：设置一些线条样式、宽度、颜色
# 绘制饼图
plt.pie(x,
        explode=explode,#表示的各部分扇形距离中心的距离
        labels=labels,#labels: 各部分扇形的名称
        colors=colors,#colors:表示颜色
        autopct=autopct,#autopct :表示占比的显示
        shadow=shadow,#shadow ：是否显示阴影
        # wedgeprops={'edgecolor': 'r', 'linewidth': 3, 'linestyle': '--'}
        )

# 如果此时绘制出来为椭圆
# plt.axis('equal')

# 增加标题
plt.title('2017年第一季度各个产业占比饼图')
# 增加图例
plt.legend(labels, loc='upper left', fontsize=8)

# 保存图片
plt.savefig('./png/2017年第一季度各个产业占比饼图.png')
# 3、图形展示
plt.show()
