import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def min_max_scalar(data):
    """
    离差标准化
    :param data: Series数据
    :return: 标准化之后的数据
    """
    # new_x = (x - min) / (max - min)

    data = (data - data.min()) / (data.max() - data.min())

    return data


def build_data():
    """
    数据加载并数据处理
    :return:
    """
    # 加载
    data = pd.read_csv('./data/company.csv', encoding='gbk')
    # print('data:\n', data)

    # 可以使用 平均每次消费金额、 平均消费周期（天） 对客户进行聚类
    # 筛选特征 --特征选择
    data = data.loc[:, ['平均每次消费金额', '平均消费周期（天）']]
    print('data:\n', data.columns)

    # 数据处理
    # 检测缺失值
    res_null = pd.isnull(data).sum()
    # print('缺失值检测结果：\n', res_null)

    # 无缺失值 ---不需要缺失值处理
    #
    # 异常值  ---无异常值

    # 标准化
    # 离差标准化
    for column in data.columns:
        data.loc[:, column] = min_max_scalar(data.loc[:, column])

    # print('标准化之后的数据:\n', data)

    # 转化为 ndarray
    data = data.values

    return data


def center_init(data, k):
    """
    随机初始化k个聚类中心
    :param data: 客户数据
    :param k: 聚类中心的数量
    :return: center
    """
    # 可以随机生成
    # 随机在所有数据中选择k个样本作为刚开始的聚类中心
    # --->量级刚好，不会增加新的数据，随机的
    # 随机选择k个不同的行下标 ---选择这k行作为刚开始的聚类中心
    # 1、获取行数
    index_num = data.shape[0]
    print('index_num:', index_num)

    # 2、获取所有的行下标
    index = np.arange(index_num)
    print('行下标：', index)

    # 3、在所有的行下标里面 随机选择 k个行下标
    # 保证k个聚类中心不重复，replace=False
    # 参数1：随机选择的数组
    # 参数2：选择的个数
    cener_index = np.random.choice(index, k, replace=False)
    print('聚类中心的行下标：', cener_index)

    # 4、筛选出聚类中心
    center = data[cener_index, :]

    return center


def distance(v1, v2):
    """
    欧式距离计算
    :param v1: 点1
    :param v2: 点2
    :return: dist
    """
    dist = np.sqrt(np.sum(np.power((v1 - v2), 2)))

    return dist


def k_means(data, k):
    """
    超时客户聚类
    :param data: 客户数据
    :param k: 聚类的类别数目
    :return:
    """
    # 1、聚类中心初始化
    center = center_init(data, k)
    print('刚初始化的聚类中心：\n', center)

    # 获取数据行数
    index_num = data.shape[0]

    # 构建一个二维数组 --来保存各个样本的最小距离，及所属的聚类中心的下标
    new_data = np.zeros(shape=(index_num, 2))
    # 开关
    flag = True
    while flag:
        # 打开开关
        flag = False
        # 2、计算距离---计算各个样本与各个聚类中心的距离
        # 循环
        for i in range(index_num):
            # i --->所有样本的行下标
            # 定义一个临时变量
            min_dist = 100000000
            # 定义一个临时变量
            min_index = -1
            for j in range(k):
                # j ----->所有聚类中心的行下标
                dist = distance(data[i, :], center[j, :])
                print('第%d个样本与第%d个聚类中心的距离为%f' % (i, j, dist))
                # 判断
                if dist < min_dist:
                    min_dist = dist
                    min_index = j
            print('第%d个样本距离第%d个聚类中心最近，且该距离为：%f' % (i, min_index, min_dist))
            if new_data[i, 1] != min_index:
                # 将样本的最小距离、及所属的聚类中心的行下标
                new_data[i, 0] = min_dist
                new_data[i, 1] = min_index
                # 闭合开关，继续聚类
                flag = True

            print('*' * 100)
        print('new_data:\n', new_data)
        if flag:
            # 3、判断---是否聚类结束
            # 根据各个样本所属的聚类中心的行下标 --将所有的样本划分为k簇
            for p in range(k):
                # p ---> 0,1,2
                # 判定为第0,1,2簇
                mask = new_data[:, 1] == p
                # 筛选 数据 ---->p_cluster各个簇的数据
                p_cluster = data[mask, :]

                # 计算各个簇的中心
                center[p, :] = p_cluster[:, 0].mean(), p_cluster[:, 1].mean()

    return center, new_data

    # 思考 ？
    # 如何判定 是否聚类结束？
    # 判定聚类结束 ---聚类中心=新的簇的中心 ---可能会增加多次无意义的计算
    # 如果所有的样本 ---当前次 所属的簇 = 上一次该样本所属的簇 --->聚类结束，
    # 如果有一个样本所在的簇发生改变，--->需要调整聚类中心，然后再继续聚类


def show_res(center, data, new_data):
    """
    结果可视化
    :param center: 聚类中心
    :param data: 原来的样本
    :param new_data: 用来保存预测类别的数据
    :return: None
    """
    # 1、创建画布
    plt.figure()

    # 默认不支持中文，需要修改参数，让其支持中文
    plt.rcParams['font.sans-serif'] = 'SimHei'  # 雅黑字体
    # 继续修改参数，让其继续支持负号
    plt.rcParams['axes.unicode_minus'] = False

    # 构建
    color_list = ['r', 'g', 'k']

    # 构建
    marker_list = ['d', 'o', '*']

    # 2、绘图
    # 绘制所有样本的数据 ---散点图
    for i in range(data.shape[0]):
        # i --->样本的行下标
        plt.scatter(data[i, 0],  # 横坐标
                    data[i, 1],  # 纵坐标
                    c=color_list[int(new_data[i, 1])],  # 颜色
                    marker=marker_list[int(new_data[i, 1])],  # 点的样式
                    )

    # 绘制聚类中心
    plt.scatter(center[:,0],center[:,1],c='b',marker='x')
    # 增加标题
    plt.title('超市客户聚类结果')
    # 横轴
    plt.xlabel('平均每次消费金额')
    # 纵轴
    plt.ylabel('平均消费周期（天）')
    # 保存图片
    plt.savefig('./png/超市客户聚类结果.png')

    # 3、展示
    plt.show()


def main():
    """
    主函数
    :return:
    """
    # 1、数据加载、数据处理
    data = build_data()
    print('data:\n', data)

    # 2、实现用户聚类
    # 确定聚类的类别数目
    # k = 3
    # center, new_data = k_means(data, k)
    # print('最终的聚类中心：\n', center)
    # print('所有样本最终的所属的簇：\n', new_data[:, 1])
    #
    # # 3、结果可视化
    # show_res(center, data, new_data)



if __name__ == '__main__':
    main()
