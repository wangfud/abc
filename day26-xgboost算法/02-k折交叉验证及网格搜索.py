from sklearn.neighbors import KNeighborsClassifier  # knn算法
from sklearn.model_selection import GridSearchCV  # 超参数网格搜索及交叉验证
import numpy as np
import matplotlib.pyplot as plt


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


def knn_skearn(train, test, k):
    """
    基于sklearn封装的knn算法 对 手写数字进行分类
    :param train: 训练集
    :param test: 测试集
    :param k: 邻居个数
    :return: y_predict, score
    """
    # 1、实例化算法对象
    # 参数：n_neighbors---邻居个数
    # weights---表示样本的权重， 如果为'uniform' ---表示影响相同
    # 如果为distance  ---距离倒数权重
    # 自定义 权重 ---高斯权重
    # metric ---默认'minkowski' ---闵可夫斯基距离
    # p  ---默认为2，表示欧式距离，p=1,曼哈顿距离，p>2--切比雪夫距离
    # n_jobs ---默认为1，表示开启单进程进行计算
    # 如果为-1,表示开启所有的处理器
    # algorithm ---查找邻居的算法的计算方式 ---默认auto
    knn = KNeighborsClassifier(n_neighbors=k)
    # 2、训练数据并构建模型
    # 参数1：训练集的特征值
    # 参数2：训练集的目标值
    knn.fit(train[:, :1024], train[:, 1024])

    # 3、测试集预测
    # 参数：测试集的特征值
    y_predict = knn.predict(test[:, :1024])

    # 获取准确率
    # 参数：测试集的特征值
    # 参数：测试集的目标值
    score = knn.score(test[:, :1024], test[:, 1024])

    return y_predict, score


def show_res(k_list, score_list):
    """
    查看不同k值时，score的变化趋势
    :param k_list: 邻居个数列表
    :param score_list: 准确率列表
    :return: None
    """
    # 1、创建画布
    plt.figure()
    # 默认不支持中文，需要修改参数，让其支持中文
    plt.rcParams['font.sans-serif'] = 'SimHei'  # 雅黑字体
    # 继续修改参数，让其继续支持负号
    plt.rcParams['axes.unicode_minus'] = False
    # 2、绘图
    # 横轴 ---k
    # 纵轴 ---score
    plt.plot(k_list, score_list, marker='*', markersize=12, color='r')
    # 增加标题
    plt.title('随着k的变化，score的变化趋势')
    # 横轴
    plt.xlabel('k值')
    # 纵轴
    plt.ylabel('准确率')
    # 保存
    plt.savefig('./png/随着k的变化，score的变化趋势.png')
    # 3、展示
    plt.show()


def main():
    """
    朱函数
    :return:
    """
    # 1、加载数据
    train, test = load_data()

    # # 2、实现超参数网格搜索
    # # （1）实例化knn算法对象
    # knn = KNeighborsClassifier()
    #
    # #
    # param_grid = {'n_neighbors': [2, 3, 4, 5, 6, 7, 8, 9, 10]}
    #
    # # （2）实例化 交叉验证对象
    # gcv = GridSearchCV(estimator=knn,  # 算法对象
    #                    param_grid=param_grid,  # 指定超参数组合
    #                    cv=3,  # K折交叉验证
    #                    n_jobs=-1,  # 使用所有的cpu
    #                    )
    #
    # # （3）训练
    # gcv.fit(train[:, :1024], train[:, 1024])
    #
    # # （4）获取模型
    # print('每次的结果为：\n', gcv.cv_results_)
    # print('最优模型为：\n', gcv.best_estimator_)
    # print('最优的准确率为：\n', gcv.best_score_)

    # (1)实例化对象
    knn = KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
                               metric_params=None, n_jobs=None, n_neighbors=3, p=2,
                               weights='uniform')
    # （2）训练数据并构建模型
    knn.fit(train[:, :1024], train[:, 1024])

    # (3) 预测
    y_pre = knn.predict(test[:, :1024])

    score = knn.score(test[:, :1024], test[:, 1024])

    print('预测值：\n', y_pre)
    print('准确率：\n', score)


if __name__ == '__main__':
    main()
