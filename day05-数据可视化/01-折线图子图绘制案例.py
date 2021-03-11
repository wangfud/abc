import numpy as np
import matplotlib.pyplot as plt

# 加载数据
fp = np.load('./data/国民经济核算季度数据.npz', allow_pickle=True)
print('fp:\n', fp)
# 遍历获取key
for tmp in fp:
    print(tmp)

# 通过key获取数组
columns = fp['columns']
values = fp['values']

print('columns:\n', columns)
print('values:\n', values)

# columns中元素为values中各个列的解释说明
# values[:,0] values[:,3]  values[:,-1]

# 绘制折线图 ---2000到2017年各个季度各个产业、行业增加总值发展趋势
# 1、创建画布
# 返回画布对象
fig = plt.figure()
# 默认不支持中文，需要修改参数，让其支持中文
plt.rcParams['font.sans-serif'] = 'SimHei'  # 雅黑字体
# 继续修改参数，让其继续支持负号
plt.rcParams['axes.unicode_minus'] = False

# 调整子图间距
# wspace=None, # 宽度间距
# hspace=None # 高度间距,小数值
fig.subplots_adjust(hspace=0.6)
# 2、绘图
# 添加子图
fig.add_subplot(2, 1,1)
# 2000-2017年各个季度各个产业的增加总值发展趋势
# 横轴--各个季度这个时间
x = np.arange(values.shape[0])  # --->[0 1 2 ... 68]
# 纵轴---2000-2017年各个季度各个产业的增加总值
y1 = values[:, 3]  # 2000年-2017年各个季度第一产业增加总值
y2 = values[:, 4]
y3 = values[:, 5]
# 绘图
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

# for循环绘制 --可以设置点线样式、颜色

# 直接绘图
y = values[:, 3:6]
plt.plot(x, y) # 不能设置点线样式、颜色

# 增加标题
plt.title('2000-2017年各个季度各个产业增加总值发展趋势', fontsize=8)
# 增加横轴名称
# plt.xlabel('时间')
# 增加纵轴名称
plt.ylabel('生产总值（亿元）', fontsize=8)
# 修改横轴刻度
# rotation=45 旋转45°
plt.xticks(x[::4], values[:, 1][::4], rotation=45, fontsize=8)

# 设置纵轴刻度
plt.yticks(fontsize=8)
# 增加图例
legend = [tmp[:4] for tmp in columns[3:6]]

plt.legend(legend, loc='upper left', fontsize=8)

fig.add_subplot(2, 1, 2)
# 2000-2017年各个季度各个行业的增加总值发展趋势
x = np.arange(1, 8)
# 准确纵轴数据
y_gz = np.array([15, 20, 22, 23, 20, 18, 16])
y_heb = np.array([-10, -8, -12, -10, -8, -6, 1])

# 绘制图形
# color ---> 线条的颜色
# linestyle -->线的样式
# linewidth -->线的宽度
# marker --->点的样式
# markersize --->点的大小
# markerfacecolor --->点的填充颜色
# markeredgecolor --->点的边缘颜色
plt.plot(x, y_gz, color='r', linestyle=':', linewidth=1.2, marker="*", markersize=7, markerfacecolor='b',
         markeredgecolor='g')
plt.plot(x, y_heb, color='b', linestyle='-.', linewidth=1.2, marker="o", markersize=7, markerfacecolor='k',
         markeredgecolor='k')

# 注意：建议将所有的修饰都放置在绘图之后

# 增加标题
plt.title('下一周广州、哈尔滨天气温度走势')

# 增加横轴名称
plt.xlabel('日期')

# 增加纵轴名称
plt.ylabel('温度（℃）')

# 修改横轴刻度
# 如果设置刻度的时候，需要将刻度替换为中文，此时需要2个参数
# 参数1：需要被替换的序号
# 参数2：中文刻度
xticks = ['周一', '周二', '周三', '周四', '周五', '周六', '周日', ]
plt.xticks(x, xticks)

# 修改纵轴刻度
# 如果修改刻度的时候，重设刻度显示范围，此时只需要一个参数
# 参数：新的刻度范围
yticks = np.arange(-15, 33, 10)
plt.yticks(yticks)

# 增加图例
# 参数1：图例
# 参数loc:图例位置
plt.legend(['广州温度', '哈尔滨温度'], loc='upper right')

# 标注点
# plt.text --->每一次只能标注一个点
for i, j in zip(x, y_gz):
    # print(i, j)
    # 参数1：标注位置的横轴
    # 参数2：标注位置的纵轴
    # 参数3：标注的内容--str
    # horizontalalignment='center' --让其标注居中
    # verticalalignment='bottom'
    plt.text(i, j + 1, '%d℃' % j, horizontalalignment='center')

for i, j in zip(x, y_heb):
    # print(i, j)
    # 参数1：标注位置的横轴
    # 参数2：标注位置的纵轴
    # 参数3：标注的内容--str
    # horizontalalignment='center' --让其标注居中
    # verticalalignment='bottom'
    plt.text(
        i, #标注位置的横轴
        j + 1, #标注位置的纵轴
        '%d℃' % j, #标注的内容--str
        horizontalalignment='center' ,
        # verticalalignment='bottom'
    )

# 保存
plt.savefig('./png/2000-2017年各个产业、行业增加总值发展趋势.png')
# 3、图形展示
plt.show()
