# 箱线图： --查看数据分布、查看数据对称性
# 后续：异常值判断、剔除方式---箱线分析法
# 异常值：超过正常的范围的错误的值


import numpy as np
import matplotlib.pyplot as plt

# 加载数据
fp = np.load('./data/国民经济核算季度数据.npz', allow_pickle=True)
print('fp:\n', fp)
# 遍历获取key
for tmp in fp:
    print(tmp)

# 通过key来获取数组
columns = fp['columns']
values = fp['values']
print('columns:\n', columns)
print('values:\n', values)

# 绘制图形
# 1、创建画布
plt.figure()
# 默认不支持中文，需要修改参数，让其支持中文
plt.rcParams['font.sans-serif'] = 'SimHei'  # 雅黑字体
# 继续修改参数，让其继续支持负号
plt.rcParams['axes.unicode_minus'] = False

# 2、绘制图形
# 以2000-2017年第一产业增加总值 来绘制箱线图
# 准备数据
x = (values[:, 3], values[:, 4], values[:, 5])
# 绘图
# notch=True ---开缺口，中位数的置信区间有关
# sym='*' ----异常值的标注的样式
# vert=False ----箱线图水平
# meanline=True, showmeans=True 同时设置，用来展示平均线
# labels : 各个箱子名称
labels = [tmp[:4] for tmp in columns[3:6]]
plt.boxplot(x, notch=True, sym='*', meanline=True, showmeans=True, labels=labels)
# 设置标题
plt.title('2000-2017年各个季度各个产业增加总值箱线图')

# 设置横轴名称
plt.xlabel('产业')

# 设置纵轴名称
plt.ylabel('生产总值（亿元）')

# 保存图片
plt.savefig('./png/2017年各个季度各个产业增加总值箱线图.png')

# 3、图形展示
plt.show()
