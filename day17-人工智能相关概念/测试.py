import numpy as np

# 欧式距离：
# 方法1：必须要求 v1 v2 必须都为一维数组
# [1,2]   [3,4]
v1 = np.array([1, 2])
v2 = np.array([3, 4])
#
# sum_ = 0
#
# for i in range(v1.shape[0]):
#     # i -->元素的下标
#     sum_ += (v1[i] - v2[i]) ** 2
#
# # 开根号
# dist = np.sqrt(sum_)
# print('距离为：\n', dist)


# 方法2：
# dist = np.sqrt(np.sum(np.power((v1 - v2), 2)))
# print('距离为：\n', dist)
