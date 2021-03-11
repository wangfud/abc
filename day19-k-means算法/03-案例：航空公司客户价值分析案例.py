# 要求：
# 信息时代的来临使得企业营销焦点从产品转向了客户，
# 客户关(Customerrelationship management，CRM)成为企业的核心问题。
# 客户关系管理的关键问题是客户分群。
# 需要利用客户的价值，将客户划分不同的簇，再根据价值对不同簇的用户执行不同类型的营销方式
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np


def load_data():
    """
    加载数据
    :return:data
    """
    air_data = pd.read_csv('./data/air_data.csv', encoding='ansi')

    return air_data


def min_max_scalar(data):
    """
    离差标准化
    :param data:需要标准化的series数据
    :return: 标准化之后的数据
    """
    # new_x = (x- min) / (max -min)
    data = (data - data.min()) / (data.max() - data.min())

    return data


def deal_data(air_data):
    """
    数据处理
    :param air_data: 数据
    :return: 处理之后的air_data
    """
    # （1）处理数据缺失值与异常值
    #  a、丢弃票价为空的记录。
    #  票价列 为： SUM_YR_1 SUM_YR_2
    #  保留法： 保留票价不为空的记录
    # 思路1：必须SUM_YR_1 和 SUM_YR_2 都不为空---->才认为票价不为空
    bool_mask_1 = air_data.loc[:, 'SUM_YR_1'].notnull()
    bool_mask_2 = air_data.loc[:, 'SUM_YR_2'].notnull()
    # 同时不为空，才认为票价不为空
    bool_mask = bool_mask_1 & bool_mask_2
    # 筛选数据
    air_data = air_data.loc[bool_mask, :]
    # print('丢弃票价为空的结果：\n', air_data)

    # 思路2：只要SUM_YR_1 和 SUM_YR_2 有一个不为空 ---->认为票价不为空
    # pass

    #  b、丢弃票价为 0、平均折扣率不为 0、总飞行千米数大于 0 的记录
    # 站在航空公司角度：丢弃不盈利的数据 --->保留盈利数据
    # 盈利数据：票价 >0, 折扣 > 0,  飞行里程  > 0
    # 票价 SUM_YR_1 SUM_YR_2
    # 思路： 只要有一个票价 > 0 ---->认为票价 >0
    mask1 = air_data.loc[:, 'SUM_YR_1'] > 0
    mask2 = air_data.loc[:, 'SUM_YR_2'] > 0

    # 思路：必须两个票价都 >0 ---->认为票价>0
    # pass

    # 折扣 > 0  avg_discount----平均折扣
    mask3 = air_data.loc[:, 'avg_discount'] > 0
    # 飞行里程 > 0  SEG_KM_SUM---窗口内的飞行里程
    mask4 = air_data.loc[:, 'SEG_KM_SUM'] > 0

    # 票价> 0 且 折扣 >0 且 飞行里程>0
    mask = (mask1 | mask2) & mask3 & mask4

    # 筛选数据
    air_data = air_data.loc[mask, :]
    # print('丢弃票价为 0、平均折扣率不为 0、总飞行千米数大于 0 的记录之后的结果为：\n', air_data)

    # （2）构建航空客户价值分析关键特征 --->LRFMC模型
    # # L --->会员入会时间距离窗口结束的月数
    #  FFP_DATE ---入会时间
    #  LOAD_TIME ---窗口结束时间
    air_data.loc[:, 'L_days'] = pd.to_datetime(air_data.loc[:, 'LOAD_TIME']) - pd.to_datetime(
        air_data.loc[:, 'FFP_DATE'])

    air_data.loc[:, 'L'] = air_data.loc[:, 'L_days'].dt.days / 30
    # print('L:\n',air_data.loc[:,'L'])
    # # R --->客户最近一次乘 坐公司飞机距观测窗口结束的月数 ---日
    air_data.loc[:, 'R'] = air_data.loc[:, 'LAST_TO_END'] / 30
    # print('R:\n',air_data.loc[:,'R'])

    # 　F --->客户在观测窗口内乘坐公司飞机的次数
    air_data.loc[:, 'F'] = air_data.loc[:, 'FLIGHT_COUNT']
    #   M---->客户在观测窗口内累计的飞行里程
    air_data.loc[:, 'M'] = air_data.loc[:, 'SEG_KM_SUM']
    #   C --->客户在观测窗口内乘坐舱位所对应的折扣系数的平均值
    air_data.loc[:, 'C'] = air_data.loc[:, 'avg_discount']

    # 筛选数据
    air_data = air_data.loc[:, ['L', 'R', 'F', 'M', 'C']]

    # （3）标准化 ---离差标准化
    for column in air_data.columns:
        air_data.loc[:, column] = min_max_scalar(air_data.loc[:, column])

    # print('air_data:\n', air_data)

    return air_data


def show_res(center):
    """
    结果可视化
    :param center: 聚类中心
    :return: None
    """
    # 1、创建画布
    plt.figure()

    # 默认不支持中文，需要修改参数，让其支持中文
    plt.rcParams['font.sans-serif'] = 'SimHei'  # 雅黑字体
    # 继续修改参数，让其继续支持负号
    plt.rcParams['axes.unicode_minus'] = False

    # 2、绘图
    # 角度 --
    datalength = center.shape[1]  # 从多少个角度去描述对象
    # 生成角度
    angle = np.linspace(0, 2 * np.pi, datalength, endpoint=False)

    # 闭合角度
    angle = np.concatenate((angle, [angle[0]]), axis=0)
    print('angle:\n', angle)

    # 准备数据 ---闭合数据
    data = np.concatenate((center, center[:, :1]), axis=1)
    print('闭合后的数据：\n', data)

    # 绘制雷达图
    for i in range(data.shape[0]):
        # i --->行下标
        plt.polar(angle, data[i, :])

    # 增加标题
    plt.title('航空公司客户价值分析结果展示')

    # 修改刻度
    plt.xticks(angle[:-1], ['L', 'R', 'F', 'M', 'C'])

    # 增加图例
    plt.legend(['第一类客户', '第二类客户', '第三类客户', '第四类客户', '第五类客户'],loc='lower right')

    # 保存
    plt.savefig('./png/航空公司客户价值分析结果展示.png')

    # 3、展示
    plt.show()


def main():
    """
    主函数
    :return:
    """
    # 1、了解航空公司的现状
    # 常旅客流失、竞争力下降和资源未充分利用等经营危机
    # 数据：
    # 2012-3-3---2014-3-3两年的数据---共计62988条关于vip及其乘坐航班的信息
    # 客户基本信息、乘机信息、积分信息
    # 客户价值：
    # a、公司收入的 80%来自顶端的 20%的客户。
    # b、20%的客户其利润率为 100%。
    # c、90%以上的收入来自现有客户。
    # d、大部分的营销预算经常被用在非现有客户上。
    # e、5%~30%的客户在客户金字塔中具有升级潜力。
    # f、客户金字塔中的客户升级 2%，意味着销售收入增加 10%，利润增加 50%

    # 2、加载数据 --pandas加载
    air_data = load_data()
    print('air_data:\n', air_data)
    print('air_data:\n', air_data.columns)
    print('air_data:\n', air_data.shape)
    print('*' * 100)

    # 3、数据处理
    air_data = deal_data(air_data)
    print('air_data:\n', air_data)

    # 4、聚类 --K-Means
    # 确定聚类的类别数目
    k = 5
    # (1)实例化算法对象
    km = KMeans(n_clusters=k)
    # (2)训练数据并构建模型
    km.fit(air_data)
    # (3)预测
    y_pre = km.predict(air_data)
    # 获取最终的聚类中心
    center = km.cluster_centers_
    print('预测类别为：\n', y_pre)
    print('最终的聚类中心：\n', center)

    # 5、结果可视化
    # 绘图雷达图 ---利用聚类中心来代替所有客户进行可视化
    show_res(center)

    # 6、分析--客户价值

    # 7、按照不同价值的客户---执行不同的营销策略

if __name__ == '__main__':
    main()
