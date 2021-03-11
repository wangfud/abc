# 张量（也可以叫做 Tensors）是 pytorch 中数据存储和表示的一个基本数据的结构和形式，
# 能够存储数据的梯度信息。
# 相当于numpy中的 ndarray

import torch
import numpy as np

# 可以使用torch.tensor来创建张量
# 可以将列表对象转化为张量
# t1 = torch.tensor([1, 2, 3, 4, 5])
# print('t1:\n', t1)  # tensor([1, 2, 3, 4, 5])
# print('t1的类型：\n', type(t1))  # <class 'torch.Tensor'>

# 也可以将ndarray转化为张量
arr = np.arange(16).reshape((4, 4))
print('arr:\n', arr)
print('arr:\n', type(arr))
print('*' * 100)

t2 = torch.tensor(arr)
t1 = t2
print('t2:\n', t2)
print('t2的类型：\n', type(t2))  # <class 'torch.Tensor'>
print('*' * 100)

# 张量的属性
print('张量的值：\n', t2.data)  # 张量的值
print('张量的数据类型：\n', t2.dtype)  # 张量的数据类型 ----torch.int32
# torch中数据类型类似于numpy中的数据类型，封装了python基础数据类型，并进行了细致划分
# 区分CPU（torch.数据类型） 和GPU

# print('张量的形状：\n',t2.shape)  # 张量的形状  # torch.Size([4, 4])
print('张量的形状：\n', t2.size())  # 张量的形状

print('张量所处的设备：\n', t2.device)  # cpu

print('张量是否计算梯度：\n', t2.requires_grad)  # 不计算的梯度  False

print('张量的梯度：\n', t2.grad)  # 张量的梯度值

print('创建张量的函数：\n', t2.grad_fn)
# None  --->如果张量是直接自己创建的，那么grad_fn为None, 如果张量是通过运算得到的，那么grad_fn就为运算函数

print('张量是否为叶子节点：\n', t2.is_leaf)
# 叶子节点 --->自己创建的张量永远都是叶子节点，---通过运算得到的张量用于为非叶子节点 ---针对的是计算梯度的张量
print('*' * 100)

# 注意：
# 创建的张量不计算梯度值，那么通过该张量后续计算得到的张量以及该张量 皆为 叶子节点,且创建函数皆为None
# t3 = t2 + 1
# print('t3:\n', t3)
# print('t3是否是叶子节点：\n', t3.is_leaf)  # True
# print('t3的创建函数：\n', t3.grad_fn)  # None


# 创建一个计算梯度的张量
# 创建张量的时候，指定requires_grad=True，那么该张量 计算梯度值
t3 = torch.tensor([1, 2, 3, 4, 5], dtype=torch.float64,
                  requires_grad=True)
print('t3:\n', t3)
print('t3是否为叶子：\n', t3.is_leaf)  # True
print('t3的创建函数：\n', t3.grad_fn)  # None
print('*' * 100)

#
t4 = t3 + 1
print('t4:\n', t4)  # tensor([2., 3., 4., 5., 6.], dtype=torch.float64, grad_fn=<AddBackward0>)
print('t4是否为叶子：\n', t4.is_leaf)  # False
print('t4的创建函数：\n', t4.grad_fn)  # <AddBackward0 object at 0x0000000001E38D08>
