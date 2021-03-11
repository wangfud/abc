import numpy as np
#
# # 创建数组
# arr = np.zeros(shape=(2, 2), dtype=np.int32)
# print('arr:\n', arr)
#
# # 二进制形式保存、文本形式保存
#
# # 将arr进行保存 --二进制形式
# # 可以使用np.save将单个数组保存起来
# # 参数1：文件的路径+名称,可以省略后缀名，默认会保存为.npy为结尾的文件。
# # 参数2：需要保存的数组
# # np.save(
# #         file, #文件的路径+名称,可以省略后缀名，默认会保存为.npy为结尾的文件
# #         arr,#需要保存的数组
# #         )
#
# # 加载.npy文件
# # 参数：文件路径+名称，此时不可省略后缀名。
# # data = np.load('./data/arr.npy')
# # print('data:\n', data)
#
# # 创建2个数组
# arr1 = np.ones(shape=(3, 3), dtype=np.int32)
# print('arr1:\n', arr1)
# arr2 = np.arange(6).reshape((2, 3))
# print('arr2:\n', arr2)
#
# # 将多个数组以二进制的形式进行保存
# # 可以使用np.savez将多个数组保存
# # 参数1：文件路径 + 名称，此时后缀名可以省略，默认保存为.npz文件
# # 后续参数：需要保存的各个数组
# np.savez('文件路径', arr1, arr2)
#
# # .npz文件保存的时候，是以 key:value 映射的关系进行保存,且默认的key为：arr_0,arr_1,...,arr_n
#
# # # 加载.npz文件
# # 可以使用np.load来加载.npz文件
# fp = np.load('./data/arr.npz')
# print('fp:\n', fp)  # <numpy.lib.npyio.NpzFile object at 0x000000000226C488>
# # 可以通过遍历io对象获取保存到.npz里面的key
# for tmp in fp:
#     print(tmp)
# #
# # 获取数组
# arr_0 = fp['arr_0']
# arr_1 = fp['arr_1']
# #
# print('arr_0:\n', arr_0)
# print('arr_1:\n', arr_1)
#
# # 如果默认保存.npz文件，如果数组过多，会导致加载数据的时候，无法区分各个数组的功能
# # 可以在保存.npz的时候，指定key值来保存
# a = np.array([1,2,3,4])
# b = np.array([3,4,5,6])
# c = np.array([3,4,5,6])
# d = np.zeros(10)
# np.savez('./data/demo', a=a, b=b,c=c,d=d)
#
#
# # 加载.npz --->
# # fp = np.load('./data/arr_key.npz')
# fp = np.load('./data/demo.npz')
# # print('fp:\n', fp)
# # # 遍历获取key
# # for tmp in fp:
# #     print(tmp)
# # # 获取数组
# a = fp['a']
# b = fp['b']
# c = fp['c']
# d = fp['d']
# print('x:\n', a)
# print('y:\n', b)


# arr = np.arange(16).reshape((4, 4))
# print('arr:\n', arr)

# 可以使用np.savetxt 以文本形式进行保存数组
# 参数1：文件路径 + 文件名称
# 参数X：数组
# 参数fmt:保存的格式
# 参数delimiter：分隔符
# np.savetxt('./data/arr.txt', X=arr, fmt='%d', delimiter=',')
# np.savetxt(
#         './data/arr.txt', #文件路径 + 文件名称
#         X=arr, #数组
#         # fmt='%d', #以整数形式保存
#         fmt='%0.2f', #精确到小说点后两位
#         delimiter=','#分隔符
# )


# 加载以文本保存的数组文件
# 参数1：文件路径+ 名称
# 参数dtype：数据类型
# 参数delimiter：分隔符，注意：保存的时候，以某种字符为分隔符，加载的时候，必须以该字符为分隔符
# data = np.loadtxt('./data/arr.txt', dtype=np.int32, delimiter=',')
# data = np.loadtxt(
#         './data/arr.txt', #文件路径+ 名称
#         dtype=np.int32, #数据类型
#         delimiter=','#分隔符，注意：确保和保存时的分隔符一致即可。
# )
# print('data:\n', data)

# 加载数据
# genfromtxt比较安全，可以读取含有缺失数据的文件
# 会在缺失的位置给一个占位符
#文件数据格式
'''
0.00,1.00,2.00,3.00
4.00,5.00,,7.00
8.00,9.00,10.00,11.00
12.00,13.00,14.00,
'''
data = np.genfromtxt(
      './data/arr.txt',
        dtype=np.int32,
        delimiter=','
)
print('data:\n',data)
'''
data:
 [[ 0  1  2  3]
 [ 4  5 -1  7]
 [ 8  9 10 11]
 [12 13 14 -1]]
'''

