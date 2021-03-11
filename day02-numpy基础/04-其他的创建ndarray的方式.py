import numpy as np

# 固定值数组的创建
# 可以使用np.array来创建一个数组
# arr = np.array([1, 2, 3, 4])
# print('arr:\n', arr)
# print('arr类型：\n', type(arr))

# 可以使用np.arange来创建一维数组
# 参数1:开始位置
# 参数2：结束位置(不包含)
# 参数3：步长
# arr = np.arange(0, 6, 1)
# print('arr:\n', arr)
# print('arr类型：\n', type(arr))
# 如果此时，开始位置为0，且步长为1，此时开始位置，及步长可省略
# arr = np.arange(6)
# print('arr:\n', arr)
# print('arr类型：\n', type(arr))
# 注意：步长可以省略的，默认步长就是1
arr = np.arange(1, 6)
print('arr:\n', arr)
print('arr类型：\n', type(arr))
# 不能省略开始位置，而去填充步长

# 也可以使用np.linspace创建等差数组
# 等差数组---->后一个元素-前一个元素 的差值 是恒定的，那么此时这个数组被称为等差数组
# 参数1：开始位置
# 参数2：结束位置(包含)
# 参数3：生成数组的元素的个数
# arr = np.linspace(1, 5, 7)
# print('arr:\n', arr)
# print('arr的类型：\n', type(arr))

# 可以使用np.logspace来创建等比数组
# 等比数组 -->后一个元素 / 前一个元素的  商值 是恒定的，那么此时这个数组被称为等比数组
# 参数1：开始位置
# 参数2：结束位置(包含)
# 参数3：生成数组的元素的个数
# base: 底数
arr = np.logspace(0, 2, 20, base=10.0)  # 生成[底数^开始，底数^结束]之间的等比数组
# arr = np.logspace(0, 2, 3, base=2.0)
print('arr:\n', arr)
print('arr的类型:\n', type(arr))

# 创建一个全部为0的数组
# 参数shape: 生成数组的形状   ---->占位
# arr = np.zeros(shape=(2, 3))
# print('arr:\n', arr)
# print('arr的类型:\n', type(arr))

# 创建一个全部为1的数组
# 参数shape:生成数组的形状 ---->占位
# arr = np.ones(shape=(2, 3))
# print('arr:\n', arr)
# print('arr的类型:\n', type(arr))


# # 可以使用np.diag来创建类似于对角矩阵的数组
# # 当v的值为一维的时候，且k=0时,此时创建的数组，类似于对角矩阵的数组（将v的值放置在对角线位置）
# # arr = np.diag(v=[1, 2, 3], k=0)
# # 当v的值为一维的时候，k>0，此时创建的数组，将v的值沿着反对角线向上挪动k个单位
# # arr = np.diag(v=[1, 2, 3], k=2)
# # 当v的值为一维的时候，k<0时，此时创建的数组，将v的值沿着反对角线向下挪动|k|个单位
# # arr = np.diag(v=[1, 2, 3], k=-1)
# # 创建一个二维数组
# v = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print('v:\n', v)
# print('v的形状：\n', v.shape)
# # 当v的值为二维时，且k=0时，此时生成的数组为v的对角线元素。
# # arr = np.diag(v=v, k=0)
# # 当v的值为二维时，k>0，此时生成的数组为v的对角线沿着反对角线向上挪动k个值时，此时的正对角线位置元素
# # arr = np.diag(v=v, k=1)
# # 当v的值为二维时，k<0，此时生成的数组为v的对角线沿着反对角线向下挪动|k|个值时，此时的正对角线位置元素
# arr = np.diag(v=v, k=-1)
# print('arr:\n', arr)
# print('arr的类型:\n', type(arr))

# 使用np.eye生成一个类似于单位矩阵的数组
# 只传递一个N值时，此时，表示的生成一个N行、N列的类似于单位矩阵的数组
# arr = np.eye(N=3, M=None, k=0)
# 如果此时k>0，此时 正对角线的1沿着反对角线向上移动k个值
# arr = np.eye(N=3, M=None, k=1)
# 如果此时k<0时，此时 正对角线的1沿着反对角线向下移动|k|个值
# arr = np.eye(N=3, M=None, k=-1)
# 如果此时 N=M, 同上
# arr = np.eye(N=3, M=3, k=0)
# 如果M > N
# 可以理解为先生成一个 N行,N列的单位矩阵数组，再补 M-N列的0
# arr = np.eye(N=2, M=3, k=0)
# # 如果 M < N
# # 可以理解为先生成一个 M行，M列的单位矩阵数组，再补 N-M行的0
# print('arr:\n', arr)
# print('arr的类型:\n', type(arr))

# 创建随机数组
# 可以使用np.random.random创建一个[0,1)均匀分布的数组
# 均匀分布---->在[0,1)内部，随机数出现的概率是相同的。
# 确定数据集 --->满足何种分布？ ---->大量数据
# 参数：生成数组的形状，生成的数组元素个数。
# arr = np.random.random((2, 2))
# arr = np.random.random(10)
# # print('arr:\n', arr)
#
# # 同np.random.rand一样，生成一个[0,1)均匀分布的数组
# # 参数：生成数组的元素个数，生成数组的行、列数，而不能是形状
# arr = np.random.rand(10)
# arr = np.random.rand(2, 2)
# # arr = np.random.rand((2,2))  # 错误的，不能为形状
# print('arr:\n', arr)

# 创建一个服从标准正态分布的数组
# 可以使用 np.random.randn 来创建服从标准正态分布的数组
# 如果数据量足够大，才能显示出分布规律
# 参数：可以为生成数组的元素个数、生成数组的行、列数
# arr = np.random.randn(10)
# arr = np.random.randn(2, 2)
# print('arr:\n', arr)


# 创建指定范围内的随机整数数组
# 会创建指定范围[low,high)随机整数数组
# arr = np.random.randint(low=0, high=2, size=(10,))
# print('arr:\n', arr)

# 创建指定范围内的随机小数数组
# 会创建指定范围[low,high)随机小数数组
# arr = np.random.uniform(low=0, high=2, size=(10,))
# print('arr:\n', arr)

# a = np.random.random(2,3,4)
a = np.random.randn(3,4)
print(a)
print(a.shape)
