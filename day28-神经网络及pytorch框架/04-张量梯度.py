import torch

# 创建一个计算梯度的张量
# t1 = torch.ones((2, 2), requires_grad=True)
# print('t1:\n', t1)
# print('t1是否计算梯度:\n', t1.requires_grad)

# # 创建一个计算梯度的张量
# t1 = torch.randn((2, 2), requires_grad=False)
# print('t1:\n', t1)
# print('t1是否计算梯度:\n', t1.requires_grad)
#
# # 修改t1让其支持计算梯度
# t1.requires_grad_(True)
# print('t1是否计算梯度：\n', t1.requires_grad)


# 创建一个计算梯度的张量
t1 = torch.ones((2, 2), requires_grad=True)
print('t1:\n', t1)
print('t1是否计算梯度：\n', t1.requires_grad)  # True
print('t1是否叶子节点：\n', t1.is_leaf)  # True
print('t1的生成函数：\n', t1.grad_fn)  # None
print('*' * 100)

# 利用t1参与计算
t2 = t1 + 2
print('t2:\n', t2)
print('t2是否计算梯度：\n', t2.requires_grad)  # True
print('t2是否叶子节点：\n', t2.is_leaf)  # False
print('t2的生成函数：\n', t2.grad_fn)  # <AddBackward0 object at 0x000000000277C588>
print('*' * 100)

# 利用t2 继续参与运算
t3 = t2 * t2 + 3
print('t3:\n', t3)
print('t3是否计算梯度：\n', t3.requires_grad)  # True
print('t3是否叶子节点：\n', t3.is_leaf)  # False
print('t3的生成函数：\n', t3.grad_fn)  # <AddBackward0 object at 0x00000000021AC648>
print('*' * 100)

# 利用t3继续参与运算
t4 = t3.mean()  # 标量
print('t4:\n', t4)
print('t4是否计算梯度：\n', t4.requires_grad)  # True
print('t4是否叶子节点：\n', t4.is_leaf)  # False
print('t4的生成函数：\n', t4.grad_fn)  # <MeanBackward0 object at 0x0000000002778648>
print('*' * 100)

print('t1中的梯度值为：\n', t1.grad)

# 利用t4对叶子节点计算梯度  ---t4生成过程中的叶子节点为t1
t4.backward()
print('t1中的梯度值为：\n', t1.grad)

# t4 = t3/4 = (t2*t2+3)/4  = ((t1+2)*(t1+2)+3)/4 = ((t1^2 + 4t1 + 4) + 3)/4
# t4 = 1/4*t1^2 + t1 + 7/4
# 利用t4对t1求一阶偏导 可得 ---梯度= 1/2*t1 + 1
# --->将t1代入梯度可得
# --->梯度=1/2 * tensor([[1., 1.],                       + 1
#                        [1., 1.]], requires_grad=True)
# 梯度值： tensor([[1.5000, 1.5000],
#                 [1.5000, 1.5000]])

# 梯度值是积累的

# 利用t1参与其他的运算
out = (t1 + 2) * 2
print('out:\n', out)
print('out是否计算梯度：\n', out.requires_grad)  # True
print('out是否叶子节点：\n', out.is_leaf)  # False
print('out的生成函数：\n', out.grad_fn)  # <MulBackward0 object at 0x000000000ED698C8>

# out = 2*t1 + 4 --->偏导 ---> 2  --->
# [[0.5 0.5]
#  [0.5 0.5]]
# 此时out为非标量的值
# 如果得到的结果不是一个标量，在调用backward反向传播时需要传入一个和结果同形的权重向量进行加权求和得到一个标量---再进行反向传播
weight = torch.tensor([[0.25, 0.25], [0.25, 0.25]])

# 利用out 对叶子节点计算梯度
out.backward(weight)
print('t1的梯度值为：\n', t1.grad)

# 注意：梯度值是积累的，如果在神经网络中，训练完一个样本，需要对梯度进行清0
