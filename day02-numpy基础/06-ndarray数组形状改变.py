import numpy as np

# 创建一个一维数组
arr = np.arange(6)
# print('arr:\n', arr)
# print('arr:\n', arr.shape)
# # print('*' * 100)

# 修改形状
# (1)可以通过shape属性重新赋值来修改形状
# arr.shape = (2, 3)
# print('arr:\n', arr)
# print('arr:\n', arr.shape)

# (2)可以使用reshape来修改形状
# arr = arr.reshape((2, 3))
arr.resize((2, 3))
print('arr:\n', arr)
# print('arr:\n', arr.shape)


# 注意：修改形状时的占位
# 其中-1，为占位。
# arr = arr.reshape((-1, 1))
# print('arr:\n',arr)

# 注意:修改的形状的时候，需要保证元素个数必须一致，不能凭空产生、与消失

# # 直接创建一个二维数组
# arr = np.arange(16).reshape((4, 4))
# print('arr:\n', arr)

# 展开为一维
# (1) shape属性重新赋值
# arr.shape = (-1,)
# print('arr:\n', arr)
# # (2) reshape
# arr = arr.reshape((-1,))
# print('arr:\n',arr)

# flatten ---拷贝一份新的数组
arr = arr.flatten('C')
arr = arr.flatten('F')  # 列优先
# print('arr:\n', arr)

# ravel  ----不需要拷贝---返回数组自身的视图
arr = arr.ravel('C')
arr = arr.ravel('F') #列优先
# print('arr:\n', arr)
