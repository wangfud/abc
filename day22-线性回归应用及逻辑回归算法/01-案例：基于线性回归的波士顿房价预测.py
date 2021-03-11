from sklearn.datasets import load_boston
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split  # 数据集拆分模块
from sklearn.preprocessing import StandardScaler, MaxAbsScaler, MinMaxScaler
# 导入线性回归
from sklearn.linear_model import LinearRegression  # 基于正规方程求解的线性回归
from sklearn.linear_model import SGDRegressor  # 随机梯度下降优化算法优化的线性回归
from sklearn.linear_model import Ridge  # 岭回归

import matplotlib.pyplot as plt

# 获取数据
boston_data = load_boston()
# print('boston_data:\n', boston_data)
# print('boston_data:\n', type(boston_data))  # 类似于字典

# 获取数据
feature = boston_data['data']
target = boston_data['target']
feature_names = boston_data['feature_names']

print('feature:\n', feature)
print('feature:\n', feature.shape)
print('*' * 100)

print('target:\n', target)
print('target:\n', target.shape)
print('*' * 100)
print('feature_names:\n', feature_names)
print('feature_names:\n', feature_names.shape)
print('feature_names:\n', type(feature_names))
print('*' * 100)

# 数据处理
# 可以将特征值 与目标值 进行 合并---完整的数据集
# 再进行数据处理
all_data = np.concatenate((feature, target.reshape((-1, 1))), axis=1)
print('all_data:\n', all_data)

# 将 特征值名称 和目标值名称 合并
columns = np.concatenate((feature_names, ['MEDV']), axis=0)
# 转化
all_df = pd.DataFrame(
    data=all_data,
    columns=columns,
)
print('all_df:\n', all_df)
print('*' * 100)

# 缺失值
res_null = pd.isnull(all_df).sum()
print('res_null:\n', res_null)
print('*' * 100)
# 异常值 ---无异常值

# 拆分数据集 ---训练集、测试集
# 自定义拆分  r= int(506 * 0.8)  ---train = data.iloc[:r,:]
# 使用 train_test_split 进行数据集拆分
# 参数1：特征值
# 参数2：目标值
# 参数：test_size --测试集的占比
# random_state -->给定非0值来固定数据
# 返回四个值
# 训练集的特征值、测试集的特征值、训练集的目标值、测试集的目标值
train_x, test_x, train_y, test_y = train_test_split(feature, target, test_size=0.2, random_state=1)
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

# 标准化
# 标准差标准化 - sklearn
# 需要标准化----特征值
# 目标值--->如果标准化之后 --->求解回归系数---新的数据---预测--->反过来推算出为标准化之前的房价
# 目标值--->不需要标准化 ---->预测值 ---真实的房价
# (1) 实例化对象
stand = StandardScaler()
# (2) 标准化数据 ---计算指标并转化数据
train_x = stand.fit_transform(train_x)  # --->计算训练集特征值的均值、标准差 --->再去转化train_x
test_x = stand.fit_transform(test_x)  # ---->计算测试集特征值的均值、标准差 --->再去转化test_x
# 把训练集、测试集 当做两部分

# # (1) 实例化对象
# stand = StandardScaler()
# # (2) 标准化数据
# stand.fit(train_x)  # 计算整个特征值的指标（均值、标准差）
# train_x = stand.transform(train_x) # 利用整个特征值的指标再去转化train_x
# test_x = stand.transform(test_x) # 利用整个特征值的指标再去转化test_x
# #把测试集当做是训练集的延伸
print('train_x:\n', train_x)
print('test_x:\n', test_x)

# 线性回归预测
# # LinearRegression ---基于正规方程求解的线性回归
# # 适用于数据量较小、特征较少的情况下
# # (1)实例化对象
# lr = LinearRegression()
# # (2)训练数据并构建模型
# lr.fit(train_x, train_y)
# # (3)预测
# y_pre = lr.predict(test_x)
# # 获取准确率
# score = lr.score(test_x, test_y)
# # 获取回归系数
# # 权重
# weight = lr.coef_
# # 偏置
# bias = lr.intercept_
# print('预测值为：\n', y_pre)
# print('准确率为：\n', score)
# print('权重系数为：\n', weight)
# print('偏置系数为：\n', bias)


# # 随机梯度下降优化算法优化的线性回归
# # (1)实例化对象
# # 参数：loss="squared_loss" --->均方误差损失
# # 参数：penalty="l2" --->l2正则化
# # 参数：alpha=0.0001 --->正则化力度
# # learning_rate：学习率，
# # 如果想要修改学习率， learning_rate = 'constant',再去修改eta0的值
# 适用于大量数据、情况较复杂的情况下。快速优化。
# sgd = SGDRegressor()
# # (2)训练数据并构建模型
# sgd.fit(train_x, train_y)
# # (3)预测
# y_pre = sgd.predict(test_x)
# # 获取准确率
# score = sgd.score(test_x, test_y)
# # 获取回归系数
# # 权重
# weight = sgd.coef_
# # 偏置
# bias = sgd.intercept_
# print('预测值为：\n', y_pre)
# print('准确率为：\n', score)
# print('权重系数为：\n', weight)
# print('偏置系数为：\n', bias)

# Ridge ---岭回归 ---线性回归 + L2正则化
# 基于正规方程求解的线性回归 + L2正则化
# 适用于数据量较小、特征较少的情况下
# (1)实例化对象
#  alpha=1.0 ---正则化力度
rd = Ridge()
# (2)训练数据并构建模型
rd.fit(train_x, train_y)
# (3)预测
y_pre = rd.predict(test_x)
# 获取准确率
score = rd.score(test_x, test_y)
# 获取回归系数
# 权重
weight = rd.coef_
# 偏置
bias = rd.intercept_
print('预测值为：\n', y_pre)
print('准确率为：\n', score)
print('权重系数为：\n', weight)
print('偏置系数为：\n', bias)

# 可视化
# 查看房价真实走势 与预测走势的对比
# 1、创建画布
plt.figure()
# 默认不支持中文，需要修改参数，让其支持中文
plt.rcParams['font.sans-serif'] = 'SimHei'  # 雅黑字体
# 继续修改参数，让其继续支持负号
plt.rcParams['axes.unicode_minus'] = False

# 2、绘图
# 横轴 --序号
x = np.arange(test_y.shape[0])
# 纵轴---真实值、预测值
plt.plot(x, test_y)
plt.plot(x, y_pre)

# 标题
plt.title('真实房价与预测房价走势')

# 纵轴
plt.ylabel('房价')

# 图例
plt.legend(['真实房价', '预测房价'])

# 保存
plt.savefig('./png/真实房价与预测房价走势_Ridge.png')
# 3、展示
plt.show()
