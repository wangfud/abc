import numpy as np

# 创建一个ndarray对象
# 可以使用np.array将list对象转化为ndarray对象
arr = np.array([1.0, 2.0, 3.0, 4.0])
print('arr:\n', arr)  # [1. 2. 3. 4.]
print('arr的类型:\n', type(arr))  # <class 'numpy.ndarray'>

arr = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[1, 2, 3, 4], [5, 6, 7, 8]]])
# print('arr:\n', arr)
# print('arr的类型：\n', type(arr))  # <class 'numpy.ndarray'>

# ndarray属性
# ndim  shape  size  dtype  itemsize
print('获取arr的维度属性：', arr.ndim)  # 维度个数
print('获取arr的形状属性：', arr.shape)  # 形状--->元组类型
# print('获取arr的元素个数：', arr.size)  # 元素个数
# print('获取arr的元素的数据类型：', arr.dtype)  # int32 --->numpy中的数据类型 --->表示的是32位平台的int类型
# print('获取arr的各个元素的占位大小为：', arr.itemsize)  # 4  # ndarray中每个元素的占位大小 --->此时表示的32位平台的int类型每个元素占位4个字节
