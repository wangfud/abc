import numpy as np

# 可以使用np.mat np.asmatrix来创建矩阵
# np.mat、np.asmatrix本质是一样的
# (1)可以将特殊字符串转化为矩阵
# m1 = np.mat('1 2 3;4 5 6;7 8 9')
# print('m1:\n', m1)
# print('m1的类型：\n', type(m1))  # <class 'numpy.matrix'>
# (2)可以将列表嵌套转化为矩阵
# m1 = np.asmatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print('m1:\n', m1)
# print('m1的类型：\n', type(m1))
# (3)可以将二维数组转化为矩阵
# m1 = np.mat(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print('m1:\n', m1)
# print('m1:\n', type(m1))

# 注意：矩阵只能是二维的
# 矩阵的索引，类似于数组索引
# 注意：在使用下标索引矩阵不降低维度。
# print('获取m1中的元素：\n', m1[0, :])

# 可以使用np.bmat来组合矩阵
# 使用bmat来组合矩阵
# 使用数组来组合生成一个大矩阵
# 创建数组
a1 = np.array([[1, 2], [3, 4]])
# a2 = np.zeros(shape=(2, 2), dtype=np.int32)
# '''
# a1:
#  [[1 2]
#  [3 4]]
# a2:
#  [[0 0]
#  [0 0]]
# '''
# #组合
# m1 = np.bmat('a1 a2;a2 a1')
# '''
# m1:
#  [[1 2 0 0]
#  [3 4 0 0]
#  [0 0 1 2]
#  [0 0 3 4]]
# '''
# print('m1:\n', m1)
# print('m1:\n', type(m1))


# 使用bmat将二维数组转化为矩阵
m1 = np.bmat(a1)
print('m1:\n', m1)
print('m1:\n', type(m1))

# 注意：bmat不能转化列表和特殊字符串为矩阵
# m1 = np.bmat('1 2 3;4 5 6;7 8 9') # 错误的
# m1 = np.bmat([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # 错误的
# print('m1:\n', m1)
# print('m1的类型：\n', type(m1))

