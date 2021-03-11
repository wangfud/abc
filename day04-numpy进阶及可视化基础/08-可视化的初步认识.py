# 需要利用可视化直观地查看数据的规律

# matplotlib绘制图形
# 主要用于2-d图形绘制，也可以绘制3-d图形

# 绘制流程
# 1、创建画布
# 2、绘制图形
# 3、图形展示

import matplotlib.pyplot as plt
import numpy as np

# 以简单的折线图为例，绘制图形
# 1、创建画布
plt.figure()
# 2、绘制图形
# 折线图---点 --->(x,y)
# (x1,y1),(x2,y2),(x3,y3),...,
# 准备横轴
x = np.array([1, 2, 3])

# 准备纵轴
y = np.array([7, 6, 8])
# 绘制折线图
plt.plot(x, y)

# 3、图形展示
plt.show()
