import numpy as np

from xgboost import XGBClassifier  # 分类的xgboost
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# 安装
# pip install xgboost

# 加载数据
data = np.loadtxt('./data/pima-indians-diabetes.csv', delimiter=',', dtype=np.float64)
print('data:\n', data)
print('data:\n', data.shape)
print('*' * 100)

# 前n列为特征值 ，最后一列为目标值
x = data[:, :-1]
y = data[:, -1]

# 数据集拆分
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2, random_state=2)
print('train_x:\n', train_x)
print('train_x:\n', train_x.shape)
print('*' * 100)

print('test_x:\n', test_x)
print('test_x:\n', test_x.shape)
print('*' * 100)

print('train_y:\n', train_y)
print('train_y:\n', train_y.shape)
print('*' * 100)

print('test_y:\n', test_y)
print('test_y:\n', test_y.shape)

# 标准化  --离差标准化
# (1) 实例化对象
min_max_sca = MinMaxScaler()
# (2) 转化数据
train_x = min_max_sca.fit_transform(train_x)
test_x = min_max_sca.fit_transform(test_x)

#
eval_set = [(test_x, test_y)]

# 使用xgboost进行分类
# (1)实例化对象
xgbst = XGBClassifier()
# (2)训练数据并构建模型
xgbst.fit(train_x,
          train_y,
          eval_set=eval_set,  # 边训练，边验证 --->每训练n步，就进行验证一次，如果验证的时候表现好，则退出
          eval_metric='logloss',  # 交叉熵损失 --->可以用来评估多分类的损失
          early_stopping_rounds=10,  # 连续加入n棵树，损失连着early_stopping_rounds次训练损失都一直不变，停止训练，返回模型
          verbose=True,  # 打印错误信息
          )
# (3)预测
y_pre = xgbst.predict(test_x)

# 获取准确率
score = xgbst.score(test_x, test_y)

print('预测值：\n', y_pre)
print('准确率为：\n', score)
