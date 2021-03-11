import numpy as np

# 将多个数组合并到一起
# (1) 一维数组
arr1 = np.array([1, 2, 3])
print('arr1:\n', arr1)
# (2) 二维数组
arr2 = np.arange(9).reshape((3, 3))
print('arr2:\n', arr2)

# 拼接的时候，只有两种方式：
# 向下拼接 ---> 垂直拼接  ---np.vstack
# 向右拼接 ---> 水平拼接  ---np.hstack


# arr2 拼接到 arr1 下边 --向下拼接
# 得把arr1 转化为2维 ，然后再和2维的 arr2进行拼接
'''
arr1:
 [1 2 3]
arr2:
 [[0 1 2]
 [3 4 5]
 [6 7 8]]
'''
# res = np.hstack((arr1, arr2))
# print('res:\n',res)
'''
res:
 [[1 2 3]
 [0 1 2]
 [3 4 5]
 [6 7 8]]
'''

# # 如果拼接，注意：不同维度的数组不能拼接的。
# np.concatenate()可以实现 横向、纵向拼接
res = np.concatenate((arr1.reshape(1, -1), arr2), axis=0)
print('res:\n', res)

# 把arr1 拼接到arr2右边
# 水平拼接
# res = np.hstack((arr2, arr1.reshape(-1, 1)))
# print('res:\n',res)

# res = np.concatenate((arr2, arr1.reshape(-1, 1)), axis=1)
# print('res:\n', res)


