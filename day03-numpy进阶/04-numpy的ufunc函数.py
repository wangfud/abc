import numpy as np

# ufunc---对ndarray中所有元素进行操作的函数，整个数组一块运算。 ---比math库要快
# 同型数组之间运算
# 创建数组
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[1, 2], [2, 3]])
print('arr1:\n', arr1)  # shape (2,2)
print('arr2:\n', arr2)  # shape(2,2)

# 四则运算 --- +-*/ **  # 对应位置元素进行四则运算
print('arr1 + arr2:\n', arr1 + arr2)  # 对应位置元素进行相加
print('arr1 - arr2:\n', arr1 - arr2)  # 对应位置元素进行相减
print('arr1 * arr2:\n', arr1 * arr2)  # 对应位置元素进行相乘
print('arr1 / arr2:\n', arr1 / arr2)  # 对应位置元素进行相除
print('arr1 ** arr2:\n', arr1 ** arr2)  # 对应位置元素进行求幂

# 比较运算 --- > < >= <= == !=
# 对应位置元素进行比较，满足条件，此处为True,不满足条件，此处为False ----组合成bool数组返回
# print('arr1 >= arr2:\n', arr1 >= arr2)
# print('arr1 <= arr2:\n', arr1 <= arr2)
# print('arr1 == arr2:\n', arr1 == arr2)
# 后续用法：比较运算返回bool数组，然后利用该返回的bool数组进行索引

# 逻辑运算 ---> np.all  np.any
# np.all 相当于and --->必须全部为True,结果才为True
# np.any 相当于or --->只要有一个为True，结果就为True
# 返回值：bool值
print('np.all:\n', np.all(arr1 >= arr2))
print('np.all:\n', np.all(arr1 <= arr2))
print('np.any:\n', np.any(arr1 <= arr2))
print('np.any:\n', np.any(arr1 >= arr2))
