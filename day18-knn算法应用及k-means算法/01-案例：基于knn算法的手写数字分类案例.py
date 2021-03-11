import os
import numpy as np
import pandas as pd


def build_data(dir_name):
    """
    加载数据并处理
    :param dir_name: 文件夹路径
    :return:
    """
    # 获取 文件夹中所有的文件名称
    file_name_list = os.listdir(dir_name)
    print('file_name_list:\n', file_name_list)
    # 占位 ---用来存储数据集
    data = np.zeros(shape=(len(file_name_list), 1025))
    # 需要对每一个文件单独处理 ---循环
    for file_name_index, file_name in enumerate(file_name_list):
        # # 表示的是 file_name这个文件在file_name_list中的下标  ---->最重该file_name数据在数据集中的行下标
        # print('file_name_index:', file_name_index)
        # print('file_name:', file_name)  # 文件名称
        # 需要加载 file_name 中的数据
        # 加载
        # np.loadtxt
        # with ... open
        # pd.read_csv
        # file_data ---单个文件的所有数据
        file_data = np.loadtxt(dir_name + file_name, dtype=np.str)
        # print('file_data:\n', file_data)
        # print('file_data:\n', file_data.shape)  # (32,)
        # 占位 --构建一个32*32的数值型数组来存储单个文件中的所有数据
        single_text_num = np.zeros(shape=(32, 32))
        # 对 file_data 中的每一行元素进行处理
        for file_content_index, file_content in enumerate(file_data):
            # file_content_index # 单独的file_data 的行下标
            # print('file_content_index：', file_content_index)
            # file_content # 每一行的数据
            # print('file_content:', file_content)

            #  file_content 转化为数值型
            arr = np.array([int(i) for i in file_content])
            # print('arr:', arr)

            # 将arr  添加 到 single_text_num 中的file_content_index 行
            single_text_num[file_content_index, :] = arr

        # print('转化为32*32的数值型数组的结果为：\n', single_text_num)
        # print('转化为32*32的数值型数组的结果为：\n', single_text_num.shape)

        # 展开成一维
        single_simple_feature = single_text_num.ravel()
        # print('展开成一维的结果为：\n', single_simple_feature)
        # print('展开成一维的结果为：\n', single_simple_feature.shape)

        # 获取目标值
        single_simple_target = np.array([float(file_name.split('_')[0])])
        # print('该样本的目标值为：', single_simple_target)

        # 合并 特征与目标
        single_simple = np.concatenate((single_simple_feature, single_simple_target), axis=0)
        # print('单个样本：\n', single_simple)
        # print('单个样本：\n', single_simple.shape)

        # 该样本 添加到 data 中的 第file_name_index 行
        data[file_name_index, :] = single_simple

    # print('data:\n',data)
    # print('data:\n',data.shape)

    return data


def save_data(train, test):
    """
    保存数据
    :param train: 训练集
    :param test: 测试集
    :return:
    """
    np.savez('./data/data', train=train, test=test)


def distance(v1, v2):
    """
    欧氏距离计算
    :param v1: 点1
    :param v2: 点2
    :return: dist
    """
    dist = np.sqrt(np.sum(np.power((v1 - v2), 2)))

    return dist


def knn_owns(train, test, k):
    """
    手写数字分类
    :param train:训练集
    :param test: 测试集
    :param k: 邻居个数
    :return: None
    """
    # 统计预测准确的样本个数
    count = 0
    # 对每一个测试集样本 进行预测
    for i in range(test.shape[0]):
        # i --->表示的是测试集样本的行下标
        # 构建一个dist_arr --保存距离
        dist_arr = np.zeros(shape=(train.shape[0], 1))
        # 1、计算距离
        for j in range(train.shape[0]):
            # j --->表示的是训练集样本的行下标
            # 计算距离
            dist = distance(train[j, :1024], test[i, :1024])
            # 保存起来
            dist_arr[j, 0] = dist
        # 距离 --dist_arr
        # 获取 train 目标值
        type_num = train[:, 1024:]

        # 合并 距离 和 类型
        all_arr = np.concatenate((type_num, dist_arr), axis=1)

        # 转化为df
        df = pd.DataFrame(
            data=all_arr,
            columns=['type_num', 'dist']
        )

        # 2、升序排序
        df_sorted = df.sort_values(by='dist')

        # 3、获取前K个邻居
        df_k = df_sorted.head(k)

        # 4、计算类别的众数
        mode = df_k.loc[:, 'type_num'].mode()[0]

        # 5、预测
        # print('第%d个测试样本的预测类别为：%f' % (i, mode))

        # 判断
        #  预测值与 真实值进行对比
        if mode == test[i, 1024]:
            # 该样本预测准确
            count += 1
    #
    print('总共预测准确的样本个数为：', count)
    # 准确率
    socre = count / test.shape[0]
    print('score:\n', socre)


def load_data():
    """
    加载数据
    :return: train, test
    """
    fp = np.load('./data/data.npz')
    # 从fp获取数组
    train = fp['train']
    test = fp['test']

    return train, test


def main():
    """
    主函数
    :return:
    """
    # # 1、加载数据并处理数据
    # train = build_data('./data/trainingDigits/')
    # test = build_data('./data/testDigits/')
    # print('train:\n', train)
    # print('train:\n', train.shape)
    # print('test:\n', test)
    # print('test:\n', test.shape)
    #
    # # 2、保存
    # save_data(train, test)

    # 3、加载数据
    train, test = load_data()
    print('train:\n', train)
    print('train:\n', train.shape)
    print('test:\n', test)
    print('test:\n', test.shape)

    # 4、手写数字分类
    # 确定邻居个数k
    k = 5

    knn_owns(train, test, k)

if __name__ == '__main__':
    main()
