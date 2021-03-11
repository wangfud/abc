import numpy as np

# sum(和)、mean(均值)、
# std(标准差)、var(方差) ：标准差=根号下方差
# min（最小值）、max（最大值）、
# argmin（最小值的下标）、argmax（最大值的下标）、
# cumsum（累计和）、cumprod（累计积）

# 创建数组
arr = np.array([[3, 5, 2],
                [7, 4, 6],
                [4, 6, 5]])
print('arr:\n', arr)
# 对arr进行统计指标计算 --->列的方向 ---->向右
print('获取arr的和：', np.sum(arr, axis=None))
# print('获取arr的最大值：', np.max(arr, axis=-1))
# print('获取arr的最小值：', np.min(arr, axis=-1))
# print('获取arr的最大值下标：', np.argmax(arr, axis=-1))
# print('获取arr的最小值下标：', np.argmin(arr, axis=-1))
#
# print('获取arr的均值：', np.mean(arr, axis=-1))
# print('获取arr的方差：', np.var(arr, axis=-1))
# print('获取arr的标准差：', np.std(arr, axis=-1))
#
# print('获取arr的累积和：\n', np.cumsum(arr, axis=-1))
# print('获取arr的累计积：\n', np.cumprod(arr, axis=-1))

# 当axis=0时， 沿着行的方向、即向下进行统计指标
# 当axis为None时。展开数组然后进行统计指标
# print('获取arr的累积和：\n', np.cumsum(arr, axis=None))


# 注意：np.统计指标 --->numpy里面的方法
# 在统计指标的时候，也可以使用ndarray.统计指标 --->ndarray里面的方法
# print('对arr求和：\n', arr.sum(axis=-1))
