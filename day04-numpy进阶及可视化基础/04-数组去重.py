import numpy as np

# 数组去重
# 剔除数组中重复的值

# arr = np.array([1, 2, 3, 1, 2, 3, 3, 2, 1, 5, 5, 7, 9, 8, 8])
# arr = np.array(['tom', 'Bob', 'kuli', 'marry', 'tom', 'jek', 'jerry'])
arr = np.array(['小花', '小华', '小化', '小明', '小李', '小张', '小芳', '小张'])
print('arr:\n', arr)
# 可以使用np.unique来对数组进行去重
# 兼并着排序
# 英文数组--按照anscii码进行排序
# 中文数组-- 按照unicode编码，然后排序
arr = np.unique(arr)
# 去重后的数组 = np.unique('原数组')
print('arr:\n', arr)
