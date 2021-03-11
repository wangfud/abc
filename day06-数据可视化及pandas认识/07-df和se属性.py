import pandas as pd

# 创建dataframe
df = pd.DataFrame(data=[['zs', 17, 187.5, 1],
                        ['ls', 18, 173.5, 1],
                        ['ww', 19, 175.0, 2],
                        ['zl', 18, 177, 2]],
                  index=['stu0', 'stu1', 'stu2', 'stu3'],
                  columns=['name', 'age', 'hight', 'group']
                  )
# print('df:\n', df)
# print('df的维度：', df.ndim)
# print('df的形状：', df.shape)
# print('df的元素个数：', df.size)  # 元素个数，不算行、列索引，只算数据
# print('df的元素的数据类型：\n', df.dtypes)  # 没有dtype，只有dtypes，返回的各列的数据类型
# # print('df的元素的数据类型：\n', df.dtype)  # 错误的，没有dtype，只有dtypes，返回的各列的数据类型
# # print('df的元素的占位大小：', df.itemsize)  # 错误的，没有itemsize，
#
# print('df的行索引：\n', df.index)
# print('df的列索引：\n', df.columns)
# # 可以通过df.values获取df中保存的ndarray
# print('df的数据：\n', df.values)
# print('df的数据：\n', type(df.values))

# 获取一列数据 得到Series
se = df['age']
print('se:\n', se)
print('se:\n', type(se))
print('se的维度：', se.ndim)
print('se的形状：', se.shape)
print('se的元素个数：', se.size)
print('se 元素的数据类型：\n', se.dtype)
print('se 元素的数据类型：\n', se.dtypes)
# print('se 元素的占位大小：\n', se.itemsize)  # 该版本没有该属性

print('se 的行索引：\n', se.index)  # 只有行索引
print('se 的数据：\n', se.values)  # 一维数组

# 修改元素类型---astype
