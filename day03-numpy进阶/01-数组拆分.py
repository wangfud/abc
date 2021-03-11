import numpy as np

# 可以使用np.hsplit  np.vsplit np.split来进行数组的拆分

# 创建一个二维数组
arr = np.arange(16).reshape((4, 4))
print('arr:\n', arr)
print('*' * 100)

# 拆分
# np.hsplit --水平拆分 ---->将水平方向，打断为n部分
# 参数1：需要拆分的数组
# 参数2：拆分的数目
# res_split = np.hsplit(arr, 2)
# print('res_split:\n', res_split[0])
# print('res_split:\n', res_split[1])

# np.vsplit ---垂直拆分 ---将垂直方向，打断为n部分
# res_split = np.vsplit(arr, 2)
# print('res_split:\n', res_split)

# 以上的拆分为平均拆分，所以，要整除，才能进行拆分
# 将该数组进行拆分--->[:1],[1:2],[2:]
# res_split = np.hsplit(arr, [1, 2])
# print('res_split:\n', res_split)

# 可以使用np.split来代替np.hsplit  np.vsplit
# res_split = np.split(arr, 2, axis=0)  #  同 np.vsplit一致
# print('res_split:\n', res_split)

# res_split = np.split(arr, 2, axis=1)  # 同 np.hsplit一致
# print('res_split:\n', res_split)

# [:1],[1:2],[2:] --三部分
# res_split = np.split(arr, [1, 2], axis=1)  # 同 np.hsplit一致
# print('res_split:\n', res_split)

# 由于拆分的限制性， 拆分不常用
# 一般使用数组索引来代替数组拆分
# arr拆分为2部分 ---第一部分为前n列，第二部分为最后一列
x = arr[:, :-1]
y = arr[:, -1:]
print('x:\n', x)
print('y:\n', y)
