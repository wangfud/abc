import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression  # 逻辑回归
from sklearn.metrics import classification_report  # 分类评估报告
from sklearn.metrics import roc_auc_score  # auc指标


def load_data():
    """
    数据加载
    :return:  data
    """
    # 准备列索引
    columns = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size',
               'Uniformity of Cell Shape', 'Marginal Adhesion', 'Single Epithelial Cell Size',
               'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli',
               'Mitoses', 'Class']

    data = pd.read_csv('./data/breast-cancer-wisconsin.data', header=None, names=columns)

    return data


def deal_data(data):
    """
    数据处理
    :param data: 原始数据
    :return: train_x, test_x, train_y, test_y
    """
    # 缺失值处理
    # (1) 将 ? 替换为 np.nan
    data.replace('?', np.nan, inplace=True)
    # (2) 检测
    res_null = pd.isnull(data).sum()
    print('缺失值检测结果为：\n', res_null)
    # (3)删除缺失值
    data.dropna(axis=0, how='any', inplace=True)
    # (4)再检测
    res_null = pd.isnull(data).sum()
    print('缺失值检测结果为：\n', res_null)

    # 筛选数据
    data = data.loc[:, 'Clump Thickness':]
    print('筛选数据之后的结果为：\n', data)

    # 数据集拆分
    train_x, test_x, train_y, test_y = train_test_split(data.iloc[:, :-1].values,
                                                        data.iloc[:, -1].values,
                                                        test_size=0.2,
                                                        random_state=2,
                                                        )
    print('train_x:\n', train_x)
    print('train_x:\n', train_x.shape)
    print('*' * 100)

    print('test_x:\n', test_x)
    print('test_x:\n', test_x.shape)
    print('*' * 100)

    print('train_y:\n', train_y)
    print('train_y:\n', train_y.shape)

    print('test_y:\n', test_y)
    print('test_y:\n', test_y.shape)

    # 标准化处理 ---标准差标准化
    # (1) 实例化对象
    stand = StandardScaler()
    # (2)标准化数据
    train_x = stand.fit_transform(train_x)
    test_x = stand.fit_transform(test_x)

    return train_x, test_x, train_y, test_y


def main():
    """
    主函数
    :return:
    """
    # 1、加载数据
    data = load_data()
    print('data:\n', data)

    # 2、数据处理
    train_x, test_x, train_y, test_y = deal_data(data)

    # 3、构建模型
    # 实例化对象
    # penalty='l2' --L2正则化
    #  C=1.0, ---正则化力度
    # solver='sag' ---随机平均梯度下降优化
    lr = LogisticRegression(solver='sag')
    # 训练数据并构建模型
    lr.fit(train_x, train_y)
    # 预测
    y_pre = lr.predict(test_x)

    # 获取准确率
    score = lr.score(test_x, test_y)

    # 获取回归系数
    # 权重
    weight = lr.coef_
    # 偏置
    bias = lr.intercept_

    print('预测值为：\n', y_pre)
    print('准确率为：\n', score)
    print('权重系数：\n', weight)
    print('偏置系数：\n', bias)

    # 准确率为 98%

    # 一个健康的人--->诊断为癌症 --->后果：复检，对当事人的心情影响比较大
    # 一个患癌症的人--->诊断为正常---->后果：错过最佳治疗时间，最终死亡
    # 两种对应的结果如果重要性程度不同， ---->引入：召回率

    # 如果那个结果影响严重---->该类别必须完全预测准确

    # 混淆矩阵
    # 真正正例预测为正例(真正例)、真正正例预测为反例（伪反例）
    # 真正反例预测为正例（伪正例）、真正反例预测为反例（真反例）

    # 召回率：真实正例中，预测为正例的比例 ---越大越好
    # 精确率：预测为正例的结果中，真实正例的比例
    # F1-score: 模型的稳健型 ---越大越好  ---> 2* 真正例 / (2*真正例 + 伪反例 + 伪正例)

    # 分类评估报告
    # 参数1：真实值
    # 参数2：预测值
    # 参数3：目标值的真实类别
    # 参数4：目标值的名称
    res_report = classification_report(test_y, y_pre, labels=[2, 4], target_names=['良性', '恶性'])
    print('res_report:\n', res_report)

    # 存在
    # 存在100个样本，99个癌症患者（以癌症患者为正例），1为正常  ---->模型：预测全部为癌症患者
    # 此时计算：
    # 模型的准确率为：99%
    # 模型的召回率为：99/99 =100%
    # 模型的精确率为：99%
    # f1-score =2* 真正例 / (2*真正例 + 伪反例 + 伪正例) = 2*99 / (2* 99 + 0 + 1) = 99.5%
    # ---> 模型非常好 --->应用--->效果很差

    # 样本不均衡
    # 评估
    # auc指标
    # roc曲线
    # FPR :真实类别为反例的样本中预测为正例的比例--->伪反例的比例 ---->越小越好
    # TPR：真实类别为正例的样本中，预测为正例的比例-->召回率 --->越大越好

    # 此时，FPR为横轴，TPR为纵轴 --->在不同的阈值下， --->多个FPR和 TPR组合---->多组FPR和TPR组成的曲线--->ROC曲线
    # 如果 在不同阈值下：FPR = TPR ---ROC曲线 ---反对角线
    # 如果 在不同阈值下： FPR < TPR ---ROC曲线 ----上三角区域
    # 如果 在不同阈值下： FPR > TPR  ----ROC曲线 ----下三角区域

    # TPR越大越好，FPR越小越好
    # ----> ROC曲线在上三角区域 ----模型不错
    # ----> ROC曲线在下三角区域 ----模型较差，如果ROC曲线在下三角区域，此时如果正反例互换，  --->ROC曲线就会在上三角区域

    # 存在
    # 存在100个样本，99个癌症患者（以癌症患者为正例），1为正常  ---->模型：预测全部为癌症患者
    # 此时计算：
    # 模型的准确率为：99%
    # 模型的召回率为：99/99 =100%
    # 模型的精确率为：99%
    # f1-score =2* 真正例 / (2*真正例 + 伪反例 + 伪正例) = 2*99 / (2* 99 + 0 + 1) = 99.5%
    # ---> 模型非常好 --->应用--->效果很差
    # TPR= 100%   FPR = 1/1 =100%   ---> TPR=FPR

    # 此时互换 正反例
    # 存在100个样本，99个癌症患者，1为正常（正例） ---->模型：预测全部为癌症患者
    # 此时计算：
    # 准确率：99%  召回率：0  FPR = 0/99 = 0  --> TPR = FPR

    # roc曲线 --->应该上三角区域 或者  反对角线

    # auc指标 ---> [ 0.5,1]之间
    # 当auc指标为0.5时 最差情况
    # 当auc指标为1时，最优的情况 ---理想状态
    # auc指标越大越好， --->roc曲线越靠近左上角， ---> TPR >> FPR
    #  auc指标 --->在样本失衡的情况下，随机选取一个样本，为正例的可能性 是 大于 反例的
    #
    # test_y = np.where(test_y > 3, 1, 0)
    #
    # # 参数1：真实值 只能是0和1
    # # 参数2：预测值 ---只能为0和1
    # auc = roc_auc_score(test_y, lr.predict(test_x))
    # print('auc:\n',auc)
    # auc 只适用于 二分类 ，且非常适合样本失衡的情况。

    # 如果提前发现---样本失衡， ---先将样本扩充为均衡状态----训练

if __name__ == '__main__':
    main()
