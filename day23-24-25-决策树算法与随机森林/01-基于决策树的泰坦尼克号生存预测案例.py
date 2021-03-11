import pandas as pd

from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

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

# 构建模型进行预测
# （1）实例化算法对象
tree = DecisionTreeClassifier(criterion='gini',  # 基尼系数， 如果为：entropy ---信息增益
                              max_depth=6,  # 树的最大深度，可以设置，用于避免过拟合
                              min_samples_split=15,  # 最小的样本划分
                              )
# （2）训练数据并构建模型
tree.fit(train_x, train_y)

# （3）预测
y_pre = tree.predict(test_x)

# 获取准确率
score = tree.score(test_x, test_y)
print('预测值为:\n', y_pre)
print('准确率为：\n', score)

# 将树进行可视化
export_graphviz(decision_tree=tree,  # 决策树对象
                out_file='./data/tree.dot',  # 生成文件
                feature_names=feature_names,  # 特征名称
                )

# 查看 tree.dot
# （1）在线查看  http://www.webgraphviz.com

# （2）将tree.dot  --->tree.png
# 安装graphviz-2.38.msi
# 找到安装路径：E:\Graphviz2.38\bin
# 将该路径添加到系统环境变量
# 进入到 tree.dot 文件夹所在路径
# 执行 dot -Tpng tree.dot -o  tree.png
# 出现tree.png
