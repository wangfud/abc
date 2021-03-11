import pandas as pd

from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier  # 随机森林

# 利用决策树，来查看在哪些特征下，游客存在生存下去的可能


# 1、 加载数据
data = pd.read_csv('./data/titanic.csv')

# 2、筛选数据
# 前3列为特征 --->目标值
data = data.loc[:, ['pclass', 'age', 'sex', 'survived']]
print('data:\n', data)
print('data:\n', data.columns)

# 3、数据处理
# 检测缺失值
res_null = pd.isnull(data).sum()
print('缺失值检测结果为：\n', res_null)

# 填充  ---平均年龄
mean_age = int(data.loc[:, 'age'].mean())
print('mean_age:', mean_age)

data.loc[:, 'age'].fillna(value=mean_age, inplace=True)

print('缺失值检测:\n', pd.isnull(data).sum())

# 数据集拆分
x = data.loc[:, ['pclass', 'age', 'sex']]
print('x:\n', x.dtypes)
y = data.loc[:, 'survived'].values
print('y:\n', y.dtype)

#  需要将特征值转化为 数值型
#  哑变量转化
# 字典特征数据抽取 ---将字典类型的数据转化为数值型特征
# (1) 先将 x --->字典
# 将DataFrame转化为 dict
x = x.to_dict(orient='records')
print('x:\n', x)

# (2)字典特征抽取
# a、实例化对象
dict_vet = DictVectorizer(sparse=False)
# b、转化特征
x = dict_vet.fit_transform(x)
# 获取转化之后的特征名称
feature_names = dict_vet.get_feature_names()
print('feature_names:\n', feature_names)
print('x:\n', x)
print('x:\n', type(x))

# 数据集拆分
# 训练集的特征值、测试集的特征值、训练集的目标值、测试集的目标值
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2, random_state=2)

# （1）实例化对象
rf = RandomForestClassifier(n_estimators=200,  # 随机森林中树的数量
                            criterion='gini',  # CART树，
                            bootstrap=True,  # 采用bootstrap抽样
                            )
# （2）训练数据并构建模型
rf.fit(train_x, train_y)
# （3）预测
y_pre = rf.predict(test_x)
# 获取准确率
score = rf.score(test_x, test_y)
print('预测值：\n', y_pre)
print('准确率为\n', score)
