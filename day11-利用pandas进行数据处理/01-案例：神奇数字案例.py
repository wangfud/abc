import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 加载数据
data = pd.read_csv('./data/anscombe.csv')
print('data:\n', data)
print('*' * 100)

# 根据 dataset列的值将数据拆分为 I II  III IV个df
df1 = data.loc[data.loc[:, 'dataset'] == 'I', :].reset_index().drop(labels=['index', 'dataset'], axis=1, inplace=False)
print('df1:\n', df1)
print('*' * 100)

df2 = data.loc[data.loc[:, 'dataset'] == 'II', :].reset_index().drop(labels=['index', 'dataset'], axis=1, inplace=False)
print('df2:\n', df2)
print('*' * 100)

df3 = data.loc[data.loc[:, 'dataset'] == 'III', :].reset_index().drop(labels=['index', 'dataset'], axis=1,
                                                                      inplace=False)
print('df3:\n', df3)
print('*' * 100)

df4 = data.loc[data.loc[:, 'dataset'] == 'IV', :].reset_index().drop(labels=['index', 'dataset'], axis=1, inplace=False)
print('df4:\n', df4)
print('*' * 100)

# # 合并 --横向堆叠
# all_df = pd.concat(objs=(df1, df2, df3, df4), axis=1, join='inner')
# # 重设列索引
# all_df.columns = ['x_I', 'y_I', 'x_II', 'y_II', 'x_III', 'y_III', 'x_IV', 'y_IV']
#
# print('all_df:\n', all_df)

# 主键合并
# left_index=True, right_index=True ---按照左右两个df的行索引值相同进行拼接合并
df12 = pd.merge(left=df1, right=df2, how='inner', left_index=True, right_index=True, suffixes=['_I', '_II'])
df123 = pd.merge(left=df12, right=df3, how='inner', left_index=True, right_index=True)
all_df = pd.merge(left=df123, right=df4, how='inner', left_index=True, right_index=True, suffixes=['_III', '_IV'])
print('all_df:\n', all_df)
print('*' * 100)

# 统计指标 --describe
res_describe = all_df.describe().loc[:, ['x_I', 'x_II', 'x_III', 'x_IV', 'y_I', 'y_II', 'y_III', 'y_IV']]
print('res_describe:\n', res_describe)

# ---->x的均值、标准差相同， y的均值、标准差相同
# 统计相关性
res_corr = all_df.corr()
print('res_corr:\n', res_corr)

# 各组 xy之间的相关性 也相同

# 查看数据分布
# 绘制散点图
# 1、创建画布
fig = plt.figure()
# 默认不支持中文，需要修改参数，让其支持中文
plt.rcParams['font.sans-serif'] = 'SimHei'  # 雅黑字体
# 继续修改参数，让其继续支持负号
plt.rcParams['axes.unicode_minus'] = False

# 调整子图间距
plt.subplots_adjust(wspace=0.3, hspace=0.3)

# 2、绘图
fig.add_subplot(2, 2, 1)
# 横轴
x = all_df.loc[:, 'x_I'].values
# 纵轴
y = all_df.loc[:, 'y_I'].values
# 绘制散点图
plt.scatter(x, y)
# 增加标题
plt.title('I型数据')

fig.add_subplot(2, 2, 2)
# 横轴
x = all_df.loc[:, 'x_II'].values
# 纵轴
y = all_df.loc[:, 'y_II'].values
# 绘制散点图
plt.scatter(x, y)
# 增加标题
plt.title('II型数据')

fig.add_subplot(2, 2, 3)
# 横轴
x = all_df.loc[:, 'x_III'].values
# 纵轴
y = all_df.loc[:, 'y_III'].values
# 绘制散点图
plt.scatter(x, y)
# 增加标题
plt.title('III型数据')

fig.add_subplot(2, 2, 4)
# 横轴
x = all_df.loc[:, 'x_IV'].values
# 纵轴
y = all_df.loc[:, 'y_IV'].values
# 绘制散点图
plt.scatter(x, y)
# 增加标题
plt.title('IV型数据')

# 保存
plt.savefig('./png/神奇数字的数据分布.png')

# 3、展示
plt.show()
