import numpy as np

# 在numpy具有元素的数据类型
# numpy封装了Python中的基本的数据类型，并进行了细致划分。  ---numpy.数据类型


# (1) 可以在创建数组的时候，通过dtype参数来指定ndarray的数据类型
# arr = np.array([1, 2, 3, 4], dtype=np.float32)
arr = np.array([1, 2, 3, 4], dtype='f8')
print('arr:\n', arr)
print('arr元素的数据类型:\n', arr.dtype)

# 如果一个数组的元素全部都是bool类型-----bool数组
# 转化的时候，0指的是False，非0指的是True
# arr = np.array([1, 0, 0, 4], dtype=np.bool)
# print('arr:\n', arr)
# print('arr元素的数据类型:\n', arr.dtype)

# (2) 也可以进行数据的强制转化
# print(np.float32(1))
# print(np.bool(1))
# # print(np.float32('a')) # 不能的，错误的
# print(np.float32('10'))

# (3) 可以通过 astype 进行修改数据类型
# arr = np.array([1, 2, 3, 4], dtype=np.int32)
# print('arr:\n', arr)
# print('arr的元素的数据类型：\n', arr.dtype)
# print('*' * 100)
# # 修改数组的类型
# arr = arr.astype(np.float32)
# print('arr:\n', arr)
# print('arr的元素的数据类型：\n', arr.dtype)
# print('arr的元素的占位大小：\n', arr.itemsize)

# (4)可以存储复合类型 ---（了解）
# # ['zs',18,173.5,50.0] ---可以存储该数据类型
# 自定义dtype来完成
df = np.dtype([('name', np.str, 40), ('age', np.int32), ('hight', np.float64), ('weight', np.float32)])
# 完成数组创建，通过dtype来指定数据类型为df
arr = np.array([('bq', 40, 168.5, 55.0), ('yf', 38, 178.5, 65.0), ('nl', 42, 183.0, 75.0)], dtype=df)
print('arr:\n', arr)
print('arr的类型：\n', type(arr))
print('arr的元素的数据类型：\n', arr.dtype)  # arr元素对象各个字段的类型
#  [('name', '<U40'), ('age', '<i4'), ('hight', '<f8'), ('weight', '<f4')]
# <U  <i  <f --->只是对数据类型进行简写
print('arr的元素个数为：\n', arr.size)# 3
print('arr的每个元素的占位大小：\n', arr.itemsize)# 176
# 要求开辟的空间大小，必须包含数据的最大的那个元素。

# 后续有专门的存储复合数据的数据结构
# ndarray 主要用来存储 数值型数据---->科学计算的
