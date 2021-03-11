import numpy as np
import matplotlib.pyplot as plt

# 直方图---由高低不等的柱子，一般情况下，各柱子之间是直接相连
# 用于查看数据的分布规律的。
# 横轴---数据范围，纵轴---各个数据范围内的数目
# 适用于大量数据

# 1、创建画布
plt.figure()
# 默认不支持中文，需要修改参数，让其支持中文
plt.rcParams['font.sans-serif'] = 'SimHei'  # 雅黑字体
# 继续修改参数，让其继续支持负号
plt.rcParams['axes.unicode_minus'] = False

# 2、绘制图形
# 以某班级同学身高分布来绘制直方图 --30名
# 准备数据
hight = np.random.uniform(low=140, high=190, size=(30,))
# print('hight:\n', hight)
# 需要对hight保留一位小数
hight = np.array([float('%.1f' % i) for i in hight])
print('hight:\n', hight)

# 绘制直方图
# 参数bins:分组情况
# 参数1：数据
# 参数edgecolor：区间边缘颜色
# 参数rwidth=1： 用来控制柱子的宽度，一般让柱子宽度为默认
# 参数color :表示柱子的颜色
# 返回值：3个
# 返回值1：各个区间内的元素个数
# 返回值2：分组区间的节点
# 返回值3：Patch objects
# res = plt.hist(hight, bins=5, edgecolor='k', rwidth=1, color='r')
# print('res:\n', res)

# 自定义分组
# bins = [140, 150, 160, 170, 180, 190]
# res = plt.hist(hight, bins=bins, edgecolor='k', rwidth=1, color='r')
# print('res:\n', res)

# 自定义等宽分组
# 确定分组的组数
group_num = 5
# 确定数据最大值、最小值
max_hight = np.max(hight)
print('max:', max_hight)

min_hight = np.min(hight)
print('min:', min_hight)
# 确定最大值、最小值之间的间距
ptp_hight = max_hight - min_hight
# 确定分组的间隔
# np.ceil ---向上取整
width = int(np.ceil(ptp_hight / group_num))
# 确定分组节点
# 注意：结束位置为max+步长，主要为了保证分组尾节点一定包含最大值
bins = np.arange(min_hight, max_hight + width, width)
print('bins:\n', bins)

res = plt.hist(hight, bins=bins, edgecolor='k', rwidth=1)
print('res:\n', res)

# 修改横轴刻度范围
plt.xticks(res[1])
# print('*' * 100)

# 保存区间中心值
avg_val = []

# 遍历下标
for i in range(res[1].shape[0] - 1):
    # 添加元素
    # print(res[1][i:i + 2].mean())
    avg_val.append(float('%.1f' % res[1][i:i + 2].mean()))

# print('*' * 100)
# 进行标注
for i, j in zip(avg_val, res[0]):
    # print(i, j)
    plt.text(i, j, '%d' % j, horizontalalignment='center')

# 增加标题
plt.title('班级学员身高分布直方图')
# 横轴名称
plt.xlabel('身高')
# 纵轴名称
plt.ylabel('人数（个）')

# 添加网格线
# alpha 表示透明度，值越大，越凝实，值越小，越透明，[0,1]
plt.grid(b=True,axis='y',alpha=0.2)

# 保存
plt.savefig('./png/班级学员身高分布直方图.png')

# 3、图形展示
plt.show()

