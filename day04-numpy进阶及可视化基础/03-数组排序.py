import numpy as np

# 创建数组
arr = np.array([5, 4, 6, 7, 3, 8])
print('arr:\n', arr)
# 直接排序 --sort ---直接对数组进行操作
# arr.sort()
print('排序之后的数组：\n', arr)

# 间接排序 --argsort ---返回索引
x = arr.argsort()
print('排序结果为：\n',x)

# 创建数组
arr = np.array([[3, 5, 2],
                [7, 4, 6],
                [4, 6, 5]])
print('arr:\n', arr)
# # 排序 --sort  ---默认按照列的方向排序
arr.sort(axis=-1)
print('排序之后的结果：\n',arr)
#
# # 注意：数组排序---自己管自己
# # 间接排序 ---返回索引
# x = arr.argsort(axis=0)
# print('x:\n',x)
