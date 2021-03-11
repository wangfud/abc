import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def build_data():
    """
    加载数据，并数据处理
    :return: nba_data
    """
    # 加载
    nba_data = pd.read_excel('./data/nba_data.xlsx')

    # 筛选特征
    nba_data = nba_data.loc[:, ['时间', '得分', '助攻']]
    print('nba_data:\n', nba_data)

    # 先将 ' '这样的特殊的缺失值 替换为 np.nan
    nba_data.replace(' ', np.nan, inplace=True)

    # 检测缺失值
    res_null = pd.isnull(nba_data).sum()
    print('缺失值检测结果：\n', res_null)

    # 处理缺失值
    # 填充 ---使用邻居来填充 时间（有规律---从大到小）的缺失值
    nba_data.loc[:, '时间'].fillna(method='pad', inplace=True)

    # 异常值：
    # 时间--->(0,48] --正常
    # 得分、[0,60) --正常
    # 助攻  [0,40)-- 正常

    # 需要将 时间转化为 float64
    nba_data.loc[:, '时间'] = nba_data.loc[:, '时间'].astype(np.float64)
    # 查看数据类型
    print('数据类型为：\n', nba_data.dtypes)

    # 构建  得分/分钟  助攻/分钟
    nba_data.loc[:, '得分/分钟'] = nba_data.loc[:, '得分'] / nba_data.loc[:, '时间']
    nba_data.loc[:, '助攻/分钟'] = nba_data.loc[:, '助攻'] / nba_data.loc[:, '时间']

    # 筛选
    nba_data = nba_data.loc[:, ['得分/分钟', '助攻/分钟']]
    print('nba_data:\n', nba_data)

    # 不需要标准化

    return nba_data


def show_res(nba_data, y_pre, center):
    """
    散点图绘制
    :param nba_data: 数据 ---dataframe
    :param y_pre: 预测类别
    :param center: 聚类中心
    :return: None
    """
    # 创建画布
    plt.figure()
    # 默认不支持中文，需要修改参数，让其支持中文
    plt.rcParams['font.sans-serif'] = 'SimHei'  # 雅黑字体
    # 继续修改参数，让其继续支持负号
    plt.rcParams['axes.unicode_minus'] = False

    #
    color_list = ['r', 'g', 'k', 'pink']

    # 绘图
    for i in range(nba_data.shape[0]):
        # i --->nba_data 的行下标
        plt.scatter(nba_data.iloc[i, 0],  # 横坐标
                    nba_data.iloc[i, 1],  # 纵坐标
                    c=color_list[y_pre[i]],  # 颜色
                    )
    # 聚类中心
    plt.scatter(center[:, 0], center[:, 1], c='b', marker='x', s=30)

    # 标题
    plt.title('nba球员聚类结果展示')
    # 横轴
    plt.xlabel(nba_data.columns[0])
    # 纵轴
    plt.ylabel(nba_data.columns[1])
    # 保存
    plt.savefig('./png/nba球员聚类结果展示.png')
    # 展示
    plt.show()


def main():
    """
    主函数
    :return:
    """
    # 1、加载数据 --数据处理
    nba_data = build_data()

    # 2、聚类
    km = KMeans(n_clusters=4)
    #
    km.fit(nba_data)
    #
    y_pre = km.predict(nba_data)
    # 获取聚类中心
    center = km.cluster_centers_

    # 3、结果可视化
    # 散点图
    show_res(nba_data, y_pre, center)


if __name__ == '__main__':
    main()
