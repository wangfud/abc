import matplotlib.pyplot as plt
import numpy as np

# 以下一周天气温度走势为例

# 1、创建画布
# figsize= (,) --->表示画布的大小
# dpi --->像素值
# 返回值--->画布对象
plt.figure()
# 默认不支持中文，需要修改参数，让其支持中文
plt.rcParams['font.sans-serif'] = 'SimHei'  # 雅黑字体
# 继续修改参数，让其继续支持负号
plt.rcParams['axes.unicode_minus'] = False

# 2、绘制图形
# 准备横轴数据
# 周一、周二、...、周日
# 注意：如果横轴为中文，绘制图形的时候，建议先用序号来代替，后续再替换序号
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
yticks = np.arange(-15, 33, 3)
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
    plt.text(i, j + 1, '%d℃' % j, horizontalalignment='center' )

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

# 保存图片
plt.savefig('./png/下一周广州、哈尔滨天气温度走势.png')

# 3、展示
plt.show()

# 折线图：用于查看数据的发展变化趋势

