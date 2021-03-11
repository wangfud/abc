import torch
import numpy as np

# # 创建全部为1的张量
# t1 = torch.ones((2, 2))
# print('t1:\n', t1)
# print('t1:\n', type(t1))  # <class 'torch.Tensor'>

#  参考ndarray 的创建方式
# torch.arange()
# torch.linspace()
# torch.logspace()
# torch.randint()
# torch.random()

# # 创建一个ndarray
# arr = np.array([1, 2, 3, 4])
#
# # 基于 torch.from_numpy来创建张量  和 ndarray是内存共享的
# t2 = torch.from_numpy(arr)
# print('t2:\n', t2)
# print('t2:\n', type(t2))
#
# # 修改ndarray 中数值
# arr[-1] = 0
#
# # 查看 t2 中是否修改？
# print('t2:\n', t2)
#
# print('id--t2:\n', id(t2))
# print('id--arr:\n', id(arr))

# 注意：id不同，值共享

# # 可以获取张量中保存的ndarray
# # 创建一个张量
# t3 = torch.arange(1, 6, 2)
# print('t3:\n', t3)
#
# # 获取张量中保存的ndarray
# arr = t3.numpy()
#
# print('arr:\n', arr)
#
# # 修改张量中的值
# t3[0] = 10
#
# # 查看arr 是否修改
# print('arr:\n',arr)
#
# print('id--t3:\n', id(t3))
# print('id--arr:\n', id(arr))


