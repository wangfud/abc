import numpy as np

# 将已存在的数据进行复制
arr = np.arange(9).reshape((3, 3))
print('arr:\n', arr)

# np.tile ---以整个数组为对象进行重复
# 参数1：需要重复的数组
# 参数2：传递一个array_like
'''
arr:
 [[0 1 2]
 [3 4 5]
 [6 7 8]]
'''
# arr = np.tile(
#     arr, #需要重复的数组
#     [2, 2, 2]#传递一个array_like,表示每个维度重复的次数
# )
# print('arr:\n', arr)
'''
arr:
 [[[0 1 2 0 1 2]
  [3 4 5 3 4 5]
  [6 7 8 6 7 8]
  [0 1 2 0 1 2]
  [3 4 5 3 4 5]
  [6 7 8 6 7 8]]

 [[0 1 2 0 1 2]
  [3 4 5 3 4 5]
  [6 7 8 6 7 8]
  [0 1 2 0 1 2]
  [3 4 5 3 4 5]
  [6 7 8 6 7 8]]]
'''
# np.repeat ---重复对象是整行、整列、数组中的元素。
# 参数1：数组
# 参数2：重复次数
# 参数axis:方向

# arr = np.repeat(arr, 2, axis=-1)
# arr = np.repeat(arr, 2, axis=0)
arr = np.repeat(arr, 2)
print('arr:\n', arr)
