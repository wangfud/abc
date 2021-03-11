import numpy as np

# 创建数组
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([2, 5])
print('arr1:\n', arr1)
print('arr1:\n', arr1.shape)  # arr1 shape(2,2)

print('arr2:\n', arr2)
print('arr2:\n',
      arr2.shape)  # arr2 shape(2,) ---->规则(1) ---->(1,2) --->arr2 = [[2,5]] --->规则(4) --->沿着arr2行轴的上的运算---第一组值
# ---->(2,2),将行的上第一组值进行复制
#            [[2 5]
# ---->arr2 = [2 5]]                      [[3 7]
# ---->ufunc规则---对应位置进行相加  ---->   [5 9]] --->shape(2,2) ---规则(2)--输出数组的shape是输入数组各个轴上的最大值
# 不同型数组相加
# print('arr1 + arr2:\n', arr1 + arr2)

# 创建数组
arr3 = np.array([1, 2, 3])
print('arr3:\n', arr3)
print('arr3:\n', arr3.shape)
# 不同型数组相加
# print('arr1 + arr3 :\n', arr1 + arr3)  # 不能相加
# 规则(3) ---判定两个不同型数组是否可以计算的规则
# arr3 shape(3,)
# 如果arr1 和arr3 进行计算 --->(2,3)  --->规则(3)，比较该输出数组与arr1 和arr3在不同轴上的值，发现输出数组的列的值与arr1列的值不相等 --->报错

# 不同型数组需要进行计算---需要的满足的规则：广播机制
# 创建数组
arr4 = np.array([[1], [2]])
print('arr4:\n', arr4)
print('arr4:\n', arr4.shape)  # （2,1）
# 不同型数组相加
print('arr1 + arr4:\n', arr1 + arr4)
# arr1 + arr4  --->(2,2) --->规则(3)  --->输出数组与arr1 arr4进行比较，在arr4列维度值不相等，但是此时arr4的列维度为1，所以也可以计算

# arr1 ->shape (1,2,3,4,5,6,7)
# arr2 ->shape (2,3,4,1,1,1) --->(1,2,3,4,1,1,1)

# arr1 --->shape (1,2,3)
# arr2 ---> shape (1,1,1,4,2,3)

# arr1 --> shape (1,2,4,5)
# arr2 ---> shape  (1,2,1,3,4,5) # 不能计算
