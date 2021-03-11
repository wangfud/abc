#导包
import matplotlib.pyplot as plt
import numpy as np
#1、创建画布
plt.figure()
#2、准备数据
x = np.array([4,7,9])
y = np.array([10,-1,5])

#3、绘制图形
plt.plot(x,y)
#4、展示图形
plt.show()