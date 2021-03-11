import numpy as np

# 一维数组索引
arr = np.array([1, 2, 3, 4, 5, 6])
print('arr:\n', arr)
#
# # 获取 arr 中的单个元素  ---可以通过下标
# print('获取arr中3元素：', arr[2])
#
# # 通过切片
# print('获取arr中的3元素：', arr[2:3])
# print('获取arr中的3元素：', type(arr[2:3]))
# # 使用下标，会造成数据降低维度，使用切片不会降低维度。
#
# # 获取arr 中 多个元素 ---可以通过切片
# print('获取arr 中的2  4   6 元素：', arr[1::2])
# # 注意：切片的时候，下标必须有规律可寻。
#
# # 获取arr中的多个元素 ---可以通过下标列表
# print('获取arr中 2  4  5元素：', arr[[1, 3, -2]])
#
# print('获取arr中 1 3 5 6元素：', arr[[0, 2, 4, 5]])
# # 注意：使用下标的列表的时候，先获取对应下标的结果，再将获取到的各个结果组合起来


# 二维数组索引
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])
# print('arr:\n', arr)
#
# # 获取arr中的单个元素 ---下标
# print('获取arr中的6元素：', arr[1, 1])
# print('获取arr中的11元素：', arr[2, 2])
#
# # 切片
# print('获取arr中的6元素：', arr[1:2, 1:2])
# print('获取arr中的11元素：', arr[2:3, 2:3])
#
# # 可以使用下标、切片
# print('获取arr中的6元素：', arr[1, 1:2])
#
# # 获取多个元素
# print('获取6 7 10 11:\n', arr[1:3, 1:3])
#
# print('获取6 7 10 11:\n', arr[[1, 1, 2, 2], [1, 2, 1, 2]])
#
# print('获取 6 7  10 12:\n', arr[[1, 1, 2, 2], [1, 2, 1, 3]])

# arr ---三维 ---->arr[块,行,列]

# arr ---n维 ----->arr[n-1个逗号] 在各个维度上进行索引

# 利用bool数组索引
mask = np.array([1, 0, 0, 1], dtype=np.bool)
print('mask:\n', mask)

# 利用mask来索引arr
# print('利用bool数组索引：\n', arr[mask, :])
# 注意：bool数组索引，保留True的，干掉False, 且bool数组的长度必须和索引数组的对应维度上的值的大小相同，否则报错
# print('利用bool数组索引：\n', arr[:, mask])

# arr --
arr = np.array([[1, 2, 3],
                [5, 6, 7],
                [9, 10, 11],
                [13, 14, 15]])
print('arr:\n', arr)

# print('利用mask索引行：\n', arr[mask, :])
# print('利用mask索引列：\n', arr[:, mask])  # 报错
