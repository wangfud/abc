# 雷达图：可以描述高维度数据
# 【x,y】 --->二维空间
# 【x,y,z】 --->三维空间
# 【x,y,z,h,j,k】 --->六维空间

import matplotlib.pyplot as plt
import numpy as np

# 雷达图：极坐标

# 1、创建画布
plt.figure()
# 默认不支持中文，需要修改参数，让其支持中文
plt.rcParams['font.sans-serif'] = 'SimHei'  # 雅黑字体
# 继续修改参数，让其继续支持负号
plt.rcParams['axes.unicode_minus'] = False

# 2、绘图
# 设置数据长度---将2π弧度划分的份数
datalength = 5
# 构建角度
angle = np.linspace(0, 2 * np.pi, datalength, endpoint=False)
print('angle:\n', angle)

# 闭合角度
angle = np.concatenate((angle, [angle[0]]), axis=0)
print('angle:\n', angle)

# 构建数据
data = np.array([2, 3.5, 4, 4.5, 5])
# 闭合数据
data = np.concatenate((data, [data[0]]), axis=0)
print('data:\n', data)
# 绘制雷达图
# 参数1：角度值
# 参数2：对应角度上的值的大小
plt.polar(angle, data, color='r', marker='*',markersize=12)

# 设置刻度
xticks = ['生存评分', '输出评分', '团战评分', 'KDA', '发育评分']
plt.xticks(angle, xticks)

# 增加标题
plt.title('某玩家王者战报')

# 保存
plt.savefig('./png/某玩家王者战报.png')

# 3、图形展示
plt.show()
