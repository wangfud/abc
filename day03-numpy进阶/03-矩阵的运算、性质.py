import numpy as np

# 创建矩阵
m1 = np.mat([[1, 2], [3, 4]])
m2 = np.mat([[2, 2], [2, 1]])
print('m1:\n', m1)
print('m2:\n', m2)

# 矩阵加法
# print('m1+m2:\n', m1 + m2)  # 对应位置元素进行相加
# # 矩阵与数进行相乘
# print('m1*2:\n', 2 * m1)  # 数与矩阵中的各个元素进行相乘
# 矩阵与矩阵相乘
# 相乘规则：左矩阵的列=右矩阵的行，生成一个左矩阵行*右矩阵列的新矩阵
# m1 (2,2) m2(2,2)
print('m1*m2:\n', m1 * m2)
print('m1*m2:\n', )
print('m1*m2:\n', np.dot(m1, m2))

# 矩阵对应位置元素进行相乘
# print('矩阵对应位置元素进行相乘：\n', np.multiply(m1, m2))

# 矩阵转置
# print('矩阵转置：\n', m1.T)
# # 矩阵的逆
# print('矩阵的逆：\n', m1.I)
# 矩阵*矩阵的逆 = E
# print('验证矩阵逆：\n', m1 * m1.I)
# 矩阵的共轭转置
print('m1的共轭转置为:\n', m1.H)
# 矩阵的视图
# 可使用np.mat将数组转化为矩阵
# 可以使用矩阵视图将矩阵转化为数组
# print('矩阵的视图：\n', m1.A)
# print('矩阵的视图：\n', type(m1.A))  # <class 'numpy.ndarray'>
