import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans  # K-MEANS
from sklearn.metrics import silhouette_score  # 轮廓系数


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


def show_res(center, data, y_predict):
    """
    结果可视化
    :param center: 聚类中心
    :param data: 原来的样本
    :param y_predict: 预测类别
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
                    c=color_list[y_predict[i]],  # 颜色
                    marker=marker_list[y_predict[i]],  # 点的样式
                    )

    # 绘制聚类中心
    plt.scatter(center[:, 0], center[:, 1], c='b', marker='x')
    # 增加标题
    plt.title('超市客户聚类结果')
    # 横轴
    plt.xlabel('平均每次消费金额')
    # 纵轴
    plt.ylabel('平均消费周期（天）')
    # 保存图片
    plt.savefig('./png/超市客户聚类结果_sklearn.png')

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

    # 2、进行聚类
    # 确定聚类的类别数目
    k = 3
    # (1) 实例化算法对象
    # n_clusters --->聚类的类别数目
    # init='k-means++' 聚类中心初始化的方式，一种优于 random的方式
    km = KMeans(n_clusters=k, init='k-means++')
    # (2)训练数据并构建模型
    km.fit(data)

    # (3)进行预测
    y_predict = km.predict(data)

    print('y_predict:\n', y_predict)

    # 获取聚类中心
    center = km.cluster_centers_
    print('最终的聚类中心：\n', center)

    show_res(center, data, y_predict)

    # 内聚度高，外离度 高
    # ai 小， bi 大
    # k-means评估
    # 轮廓系数 ---(-1,1) ---越趋近于1，效果越好，越趋近0甚至负数，效果差
    score = silhouette_score(data, y_predict)
    print('轮廓系数为：\n',score)


if __name__ == '__main__':
    main()
