import numpy as np
import matplotlib.pyplot as plt

# 创建子图
# 返回值1 画布对象
# 返回值2 坐标系对象
fig, ax = plt.subplots()

size = 0.3
vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

cmap = plt.get_cmap("tab20c")  # 颜色
outer_colors = cmap(np.arange(3) * 4)
inner_colors = cmap([1, 2, 5, 6, 9, 10])

ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
       wedgeprops=dict(width=size, edgecolor='r'))

ax.pie(vals.flatten(),  # 数据
       radius=1 - size,  # 半径
       colors=inner_colors,  # 颜色
       wedgeprops=dict(width=size, edgecolor='k'),  # 边缘设置
       )

# 设置
ax.set(aspect="equal", title='Pie plot with `ax.pie`')

plt.show()

# 其他图形绘制参考：https://matplotlib.org/gallery/index.html
