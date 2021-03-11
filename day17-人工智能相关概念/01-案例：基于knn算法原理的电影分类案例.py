import pandas as pd
import numpy as np


def build_data():
    """
    加载数据
    :return: train, test
    """
    data = pd.read_excel('./data/电影分类数据.xls', index_col=0)
    # print('data:\n', data)

    # 数据集拆分
    # 训练集
    train = data.loc[:, '电影名称':'电影类型']
    # print('train:\n', train)
    # print('*' * 100)
    # 测试集
    test = data.columns[-4:]
    # print('test:\n', test)

    return train, test


def distance(v1, v2):
    """
    欧式距离计算
    :param v1: 点1
    :param v2: 点2
    :return: dist
    """
    dist = np.sqrt(np.sum(np.power((v1 - v2), 2)))
    return dist


def knn_owns(train, test, k):
    """
    唐人街探案电影预测分类
    :param train: 数据集
    :param test: 唐人街探案数据
    :param k: 邻居个数
    :return: None
    """
    # 构建一个 dist_array 来保存距离
    dist_array = np.zeros((train.shape[0], 1))

    # 1、计算距离
    for i in range(train.shape[0]):
        # i ---> train 的行下标
        dist = distance(train.iloc[i, 1:4], test[1:])
        print('第 %d 个电影 与唐人街探案的距离为：%f' % (i, dist))
        # 保存距离
        dist_array[i, 0] = dist
    # print('dist_array:\n', dist_array)
    # 获取 电影类型
    movie_type_array = train.loc[:, '电影类型':].values
    # print('movie_type_array:\n', movie_type_array)

    # 和 距离尽心合并
    all_array = np.concatenate((movie_type_array, dist_array), axis=1)

    # print('all_array:\n', all_array)

    # 转化为df
    df = pd.DataFrame(
        data=all_array,
        columns=['movie_type', 'dist']
    )
    # print('df:\n', df)

    # 2、按照距离进行升序排序
    df_sorted = df.sort_values(by='dist')
    # print('df_sorted:\n', df_sorted)

    # 3、获取距离近的k个邻居
    df_k = df_sorted.head(k)
    print('df_k:\n', df_k)

    # 4、计算 movie_type 的众数
    mode = df_k.loc[:, 'movie_type'].mode()[0]
    # print('mode:\n', mode)

    # 5、预测
    print('唐人街探案的类别预测为：', mode)


def main():
    """
    主函数
    :return:
    """
    # 1、加载数据
    train, test = build_data()
    print('train:\n', train)
    print('*' * 100)
    print('test:\n', test)

    # 2、基于knn算法的电影分类
    # 确定邻居个数
    k = 5

    knn_owns(train, test, k)

if __name__ == '__main__':
    main()

