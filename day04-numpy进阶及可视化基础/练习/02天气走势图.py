import matplotlib.pyplot as plt
import numpy as np

#1、创建画布
plt.figure()
#显示中文
plt.rcParams['font.sans-serif'] = 'SimHei'
#显示负号
plt.rcParams['axes.unicode_minus'] = False
#2、准备数据
x = np.arange(1,8)
# print(x)
y1 = [15 ,20, 22, 23, 20, 18, 16]
y2 = [3 ,10, 11, 12, 2, 0, -1]
#3、绘制图形
plt.plot(x,y1,
         color='r',
         # linestyle = "'v'",
         linestyle = "-",
         linewidth=1.2,#线宽
         # marker='o',#原点
         # marker='^',#正三角
         # marker='v',#倒三角
         # marker='|',#竖线
         # marker='H',#六边形
         # marker='D',#菱形
         marker='p',#五角星
         markersize = 7,
         markerfacecolor='b',#点填充颜色
         markeredgecolor = 'g'

         )
plt.plot(x,y2,color='b',linestyle = '-.',marker='D',markerfacecolor = 'b',markeredgecolor='b')
#图形修饰
#（1）增加标题
plt.title('北京下一周天气走势图')
#（2）增加x，y轴的名称
plt.xlabel('日期')
plt.ylabel('温度（℃）')
#（3）修改横轴刻度
xticks = ['周一', '周二', '周三', '周四', '周五', '周六', '周日', ]
#rotation：刻度旋转
plt.xticks(x,xticks,rotation=45)
#（4）修改纵轴刻度
#一般我们需要将刻度显示的数据范围以内：15-30
yticks = np.linspace(-1,30,num=7)
yticks = np.arange(-5,30,step=5)
# print(yticks)
plt.yticks(yticks)#只需要指定新的y即可
#（5）增加图例
#loc=1->4:分别表示从右上角->右下角
plt.legend(['北京','哈尔滨'],loc=8)

#(6)
# plt.plot(x,y1)
#4、显示图形
plt.show()