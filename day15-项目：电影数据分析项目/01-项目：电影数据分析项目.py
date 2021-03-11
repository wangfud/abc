import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
from pyecharts import options as opts
from pyecharts.charts import *

# 加载数据
credits = pd.read_csv('./data/tmdb_5000_credits.csv')
movies = pd.read_csv('./data/tmdb_5000_movies.csv')
# 查看数据
# print('credits:\n', credits.head(5))
# print('credits:\n', credits.shape)
# print('credits:\n', credits.columns)

# print('movies:\n', movies.head(5))
# print('movies:\n', movies.shape)
# print('movies:\n', movies.columns)
# print('*' * 100)

# 需要将 credits 和 movies 进行合并
# 先将 credits 中的 movie_id  ---->id
credits.rename(columns={'movie_id': 'id'}, inplace=True)
# print('credits:\n', credits.head(5))
# print('credits:\n', credits.shape)
# print('credits:\n', credits.columns)
# 按照 电影名称 及 电影id ---主键合并
# outer ---> 可能会造成存在大量缺失值 --->电影都已经上映，如果信息缺失，上网查询具体电影的详细信息
data = pd.merge(left=credits, right=movies, on=['id', 'title'], how='outer')
print('data:\n', data.head())
print('data:\n', data.shape)
print('data:\n', data.columns)
print('*' * 100)

# 需求：
# 1、电影类型和时间的关系
# 获取电影类型  ----genres
# 获取电影的发行时间 --- release_date

# 缺失值检测
res_null = pd.isnull(data).sum()
print('缺失值的检测结果：\n', res_null)
print('*' * 100)

# 获取每列的数据类型
data_dtypes = data.dtypes
print('数据类型为：\n', data_dtypes)
print('*' * 100)

# genres 无缺失值 ，  release_date存在一个缺失值
# 对 release_date 这个缺失值？？？？
# （1）先检测 release_date 缺失的电影名称
mask = data.loc[:, 'release_date'].isnull()
print('mask:\n', mask)

movie_name = data.loc[mask, 'title']
print('缺失发行时间的电影名称为：\n', movie_name)
print('*' * 100)
# （2）查询
# 缺失发行时间的电影名称为：America Is Still the Place  --->上映日期为：2014-06-01
# （3）进行填充
data.loc[mask, 'release_date'] = '2014-06-01'

#  可以查看 电影发行年份 和 电影类型的关系

# 转化为pandas支持的时间序列
data.loc[:, 'release_date'] = pd.to_datetime(data.loc[:, 'release_date'])

# 获取 发行年份
data.loc[:, 'release_year'] = data.loc[:, 'release_date'].dt.year
print('data:\n', data.head(10))
print('*' * 100)

# 电影类型？？？  genres ---？？
# 对 genres 如何处理？？？
# print('电影类型：\n', data.loc[:, 'genres'])
# print('电影类型：\n', type(data.loc[0, 'genres']))  # json字符串

# 将python类型转化为json ---json.dumps
# 将json类型转化为python类型 ---json.loads
data.loc[:, 'genres'] = data.loc[:, 'genres'].transform(json.loads)

# print('电影类型：\n', data.loc[:, 'genres'])
# print('电影类型：\n', type(data.loc[0, 'genres']))

# 所有的电影类型
all_movie_type = set()


# 一个电影存在多个电影类型。
def get_movie_type(val):
    """
    [{""id"": 28, ""name"": ""Action""},
    {""id"": 12, ""name"": ""Adventure""},
    {""id"": 14, ""name"": ""Fantasy""},
    {""id"": 878, ""name"": ""Science Fiction""}]
     获取电影类型
    :param val: 数据
    :return:
    """
    # 存储 各个电影的 所有的电影类型
    movie_type_list = []
    for item in val:
        # 获取 val中每一个字典元素
        if item:
            movie_type = item['name']
            # 将获取到的电影类型添加到 movie_type_list
            movie_type_list.append(movie_type)
            # 在加入到 all_movie_type
            all_movie_type.add(movie_type)

    # 将电影类型 movie_type_list 合并为字符串
    movie_type = ','.join(movie_type_list)

    return movie_type


# 对 genres 获取电影类型
data.loc[:, 'genres'] = data.loc[:, 'genres'].transform(get_movie_type)
print('genres:\n', data.loc[:, 'genres'])

# 获取所有的电影类型
all_movie_type = list(all_movie_type)
print('all_movie_type:\n', all_movie_type)
print('all_movie_type:\n', len(all_movie_type))

# 将 genres 转化为 多列 的 01的数值型数据
for column in all_movie_type:
    # 先增加一列 数据
    data.loc[:, column] = 0
    # 判断
    mask = data.loc[:, 'genres'].str.contains(column)
    # 此时 将 mask 的 column 列 修改为 1
    data.loc[mask, column] = 1

print('data:\n', data)
print('data:\n', data.shape)
# 将电影类型转化之后，进行保存为csv
# data.loc[:, all_movie_type].to_csv('./data/data.csv')

# # 查询 genres 为空的 所对应的电影名称
# mask = data.loc[:, 'genres'] == ''
# # 获取 此时缺失值 电影类型的 电影名称
# movie_name = data.loc[mask, 'title']
# print('缺失电影类型的电影名称为：\n', movie_name)   # 有多个电影类型缺失

# (1)查看各个电影类型随时间的变化趋势
# 按照 release_year 分组， 统计的 各个电影类型 的  sum
res = pd.pivot_table(
    data=data,
    index='release_year',
    values=all_movie_type,
    aggfunc='sum'
)
print('res:\n', res)

# 可视化  ---折线图
# ============需求1========================================================== matplotlib ===================================
# # （1）创建画布
# plt.figure()
# # 默认不支持中文，需要修改参数，让其支持中文
# plt.rcParams['font.sans-serif'] = 'SimHei'  # 雅黑字体
# # 继续修改参数，让其继续支持负号
# plt.rcParams['axes.unicode_minus'] = False
#
# # （2）绘图
# # 横轴 ---序号
# x = np.arange(res.shape[0])
# # 纵轴 ---各列数据
# y = res
#
# # 绘图
# plt.plot(x, res)
#
# # 增加标题
# plt.title('不同类型电影随时间的变化趋势')
#
# # 横轴刻度
# plt.xticks(x[::10], res.index[::10], rotation=45)
#
# # 图例
# plt.legend(res.columns, fontsize=8, loc='upper left')
#
# # 保存
# plt.savefig('./png/不同类型电影随时间的变化趋势.png')
#
# # （3）展示
# plt.show()

# ===============需求1===================================================== pyecharts ===================================
# # 1、实例化对象
# line = Line(
#     # 初始化配置
#     init_opts=opts.InitOpts(
#         width='800px',
#         height='500px',
#         theme='dark',
#         page_title='折线'
#     )
# )
#
# # 2、添加数据
# # 横轴数据
# line.add_xaxis(
#     xaxis_data=[str(tmp) for tmp in res.index]
# )
#
# # 纵轴数据
# for column in res.columns:
#     line.add_yaxis(
#         series_name=column,
#         y_axis=res.loc[:, column].tolist()
#     )
#
# # 3、全局配置
# line.set_global_opts(
#     # 标题
#     title_opts=opts.TitleOpts(
#         title='不同类型电影随时间的变化趋势',
#         pos_left='3%',
#         pos_top='1%'
#     ),
#     # 图例
#     legend_opts=opts.LegendOpts(
#         is_show=True,
#         type_='scroll',
#         # type_='plain',
#         pos_left='center',
#         pos_top='5%'
#     )
# )
#
# # 4、系列配置
# line.set_series_opts(
#     label_opts=opts.LabelOpts(
#         is_show=False
#     )
# )
#
# # 5、生成图像
# line.render('./png/不同类型电影随时间的变化趋势.html')
# ================================================================================================================

# 研究：时间和电影类型
# 整个时间段内 不同电影的 对比
# 在整个时间段 不同电影的对比柱状图
# 计算出 整个时间段内，不同电影的数量
res_sum = res.sum().sort_values(ascending=True)
print('res_sum:\n', res_sum)

# 绘制 对比柱状图
# ============需求1============================================================matplotlib=======================
# # 1、创建画布
# plt.figure()
#
# # 默认不支持中文，需要修改参数，让其支持中文
# plt.rcParams['font.sans-serif'] = 'SimHei'  # 雅黑字体
# # 继续修改参数，让其继续支持负号
# plt.rcParams['axes.unicode_minus'] = False
#
# # 2、绘图
# # 横轴  ---序号
# x = np.arange(res_sum.shape[0])
# # 纵轴
# y = res_sum
#
# # 绘图
# plt.barh(x, y, color='#6495ED', orientation='horizontal')
#
# # 修改刻度
# plt.yticks(x, res_sum.index)
#
# # 重设横轴刻度
# plt.xticks(np.arange(0, 3500, 500))
#
# # 标题
# plt.title('不同类型电影对比柱状图')
#
# # 纵轴名称
# plt.xlabel('数量')
#
# # 标注
# for i, j in zip(y, x):
#     plt.text(i, j, '%d' % i, verticalalignment='center')
#
# # 保存
# plt.savefig('./png/不同类型电影对比柱状图.png')
#
# # 3、图形展示
# plt.show()

# ==========需求1==========================================================pyecharts ==============================================
# # （1）实例化对象
# bar = Bar(
#     init_opts=opts.InitOpts(
#         width='800px',
#         height='500px',
#         theme='dark',
#         page_title='柱状图'
#     )
# )
# # （2）添加数据
# bar.add_xaxis(
#     xaxis_data=[str(tmp) for tmp in res_sum.index]
# )
#
# bar.add_yaxis(
#     series_name='',
#     yaxis_data=res_sum.tolist(),
#     # color='#6495ED'
# )
#
# # （3）全局配置
# bar.set_global_opts(
#     title_opts=opts.TitleOpts(
#         title='不同类型电影对比柱状图',
#         pos_left='center',
#         pos_top='5%'
#     ),
#     legend_opts=opts.LegendOpts(
#         is_show=False
#     )
# )
# # （4）系列配置
# bar.set_series_opts(
#     label_opts=opts.LabelOpts(
#         is_show=True,
#         position='right',
#         # color='#6495ED'
#     )
# )
# # 翻转坐标系
# bar.reversal_axis()
#
# # （5）生成图像
# bar.render('./png/不同类型电影对比柱状图.html')
# ======================================================================================================================
res_sum = pd.DataFrame(data=res_sum.values.reshape((-1, 1)),
                       columns=['数量'],
                       index=res_sum.index).reset_index()
# print('res_sum:\n', res_sum)

#
print('*' * 100)
main = res_sum.tail(13)
# print('main:\n', main)

b = res_sum.head(7)['数量'].sum()
# print('b:\n', b)

other = pd.DataFrame(
    data=[['other', b]],
    columns=['index', '数量'],
)
# print('other:\n', other)

# 合并
all_df = pd.concat((other, main), axis=0, join='outer').sort_values(by='数量')
print('all_df:\n', all_df)

# 研究：不同类型的电影的占比
# ===========================================================matplotlib===================================================
# 1、创建画布
# plt.figure()
# # 默认不支持中文，需要修改参数，让其支持中文
# plt.rcParams['font.sans-serif'] = 'SimHei'  # 雅黑字体
# # 继续修改参数，让其继续支持负号
# plt.rcParams['axes.unicode_minus'] = False
# # 2、绘图
# # 准备数据
# x = all_df['数量']
# # label
# labels = all_df['index']
# plt.pie(x, labels=labels, autopct='%.1f%%', pctdistance=0.6, radius=1)
# # 添加标题
# plt.title('不同类型电影占比')
# # 图例
# # plt.legend(labels)
# # 保存
# plt.savefig('./png/不同类型电影占比.png')
# # 3、展示
# plt.show()

# ======================================================================Pyecharts ======================================
#
# # 准备data_pair
# data_pair = [(k, v) for k, v in zip(all_df.loc[:, 'index'].tolist(), all_df.loc[:, '数量'].tolist())]
#
# # 1、实例化对象
# pie = Pie(
#     init_opts=opts.InitOpts(
#         width='800px',
#         height='500px',
#         theme='dark',
#         page_title='饼图'
#     )
# )
#
# # 2、添加数据
# pie.add(
#     series_name='',
#     data_pair=data_pair,
#     radius=['30%', '70%']
# )
#
# # 3、全局配置
# pie.set_global_opts(
#     title_opts=opts.TitleOpts(
#         title='不同类型电影占比饼图',
#         pos_left='center',
#         pos_top='2%'
#     ),
#     legend_opts=opts.LegendOpts(
#         is_show=False,
#         # pos_left='center',
#         # pos_top='5%',
#         # type_='scroll'
#     )
# )
#
# # 4、系列配置
# pie.set_series_opts(
#     label_opts=opts.LabelOpts(
#         is_show=True,
#         formatter='{b}:{d}%'
#     )
# )
#
# # 5、生成图像
# pie.render('./png/不同类型电影占比饼图.html')
# ======================================================================================================================

# 2、电影类型和利润的关系
# 研究的是电影类型 ---利润
# 计算利润
data.loc[:, 'profit'] = data.loc[:, 'revenue'] - data.loc[:, 'budget']

# 构建一个list，存储各个类型电影的平均利润
all_movie_mean_profit = []

# 计算不同类型电影的平均利润 ---对比
for column in all_movie_type:
    # 获取 column 类型的 电影
    mask = data.loc[:, column] == 1
    # 计算一下 这些电影的平均利润
    mean_profit = data.loc[mask, 'profit'].mean()
    # 将 mean_profit 加入到 all_movie_mean_profit
    all_movie_mean_profit.append(mean_profit)

print('all_movie_type:', all_movie_type)
print('all_movie_mean_profit:', all_movie_mean_profit)
print('*' * 100)

# 构建一个df
res_profit = pd.DataFrame(
    data=np.array(all_movie_mean_profit).reshape((-1, 1)),
    index=all_movie_type,
    columns=['profit']
).reset_index().sort_values(by='profit')
print('res_profit:\n', res_profit)

# 不同类型电影 ---利润的关系
#  对比柱状图
# ====需求2=========================================================================matplotlib ============================

# # 1、创建画布
# plt.figure()
#
# # 默认不支持中文，需要修改参数，让其支持中文
# plt.rcParams['font.sans-serif'] = 'SimHei'  # 雅黑字体
# # 继续修改参数，让其继续支持负号
# plt.rcParams['axes.unicode_minus'] = False
#
# # 2、绘图
# # 横轴  ---序号
# x = np.arange(res_profit.shape[0])
# # 纵轴
# y = res_profit['profit']
#
# # 绘图
# plt.barh(x, y, color='#6495ED', orientation='horizontal')
#
# # 修改刻度
# plt.yticks(x, res_profit['index'])
#
# # 重设横轴刻度
# # plt.xticks(np.arange(-1 * 10 ** 7, 2.4 * 10 ** 8, 1 * 10 ** 7)[::5])
#
# # 标题
# plt.title('不同类型电影利润对比柱状图')
#
# # 纵轴名称
# plt.xlabel('平均利润')
#
# # # 标注
# # for i, j in zip(y, x):
# #     plt.text(i, j, '%d' % i, verticalalignment='center')
#
# # 保存
# plt.savefig('./png/不同类型电影利润对比柱状图.png')
#
# # 3、图形展示
# plt.show()

# ==========需求2==========================================================pyecharts ==============================================
# # （1）实例化对象
# bar = Bar(
#     init_opts=opts.InitOpts(
#         width='800px',
#         height='500px',
#         theme='dark',
#         page_title='柱状图'
#     )
# )
# # （2）添加数据
# bar.add_xaxis(
#     xaxis_data=[str(tmp) for tmp in res_profit['index'].tolist()]
# )
#
# bar.add_yaxis(
#     series_name='',
#     yaxis_data=[float('%.2f' % i) for i in res_profit['profit']],
#     # color='#6495ED'
# )
#
# # （3）全局配置
# bar.set_global_opts(
#     title_opts=opts.TitleOpts(
#         title='不同类型电影利润对比柱状图',
#         pos_left='center',
#         pos_top='5%'
#     ),
#     legend_opts=opts.LegendOpts(
#         is_show=False
#     )
# )
# # （4）系列配置
# bar.set_series_opts(
#     label_opts=opts.LabelOpts(
#         is_show=True,
#         position='right',
#         # color='#6495ED'
#     )
# )
# # 翻转坐标系
# bar.reversal_axis()
#
# # （5）生成图像
# bar.render('./png/不同类型电影利润对比柱状图.html')

# ======================================================================================================================

# 3、Universal 和 Paramount 两家影视公司的对比
# 对比 Universal  和 Paramount 发行的电影数量
# 查看 production_companies 这列数据
print('电影制作公司：\n', data.loc[:, 'production_companies'])  # json字符串
# print('电影制作公司：\n', type(data.loc[0, 'production_companies']))
# [{"name": "Ingenious Film Partners", "id": 289},
# {"name": "Twentieth Century Fox Film Corporation", "id": 306},
# {"name": "Dune Entertainment", "id": 444},
# {"name": "Lightstorm Entertainment", "id": 574}]
# 构建两列数据 分别记录 电影的制作公司
data.loc[:, 'Universal'] = 0
data.loc[:, 'Paramount'] = 0

# 判断 如果电影公司中 有Universal 字眼
mask1 = data.loc[:, 'production_companies'].str.contains('Universal')
# 将 mask1行 Universal列 --->1
data.loc[mask1, 'Universal'] = 1

# 判断 如果电影公司中 有Paramount 字眼
mask2 = data.loc[:, 'production_companies'].str.contains('Paramount')
# 将 mask2行 Paramount列 --->1
data.loc[mask2, 'Paramount'] = 1

# 查看 Universal电影数量 和Paramount电影数量
res_movie_count = data.loc[:, ['Universal', 'Paramount']].sum()

print('两家公司发行的电影数量：\n', res_movie_count)

# 结果可视化
# ====================================================================================matplotlib =======================
# # 1、创建画布
# plt.figure()
# # 默认不支持中文，需要修改参数，让其支持中文
# plt.rcParams['font.sans-serif'] = 'SimHei'  # 雅黑字体
# # 继续修改参数，让其继续支持负号
# plt.rcParams['axes.unicode_minus'] = False
# # 2、绘图
# # 准备数据
# x = res_movie_count
# # label
# labels = res_movie_count.index
# plt.pie(x, labels=labels, autopct='%.1f%%', pctdistance=0.6, radius=1)
# # 添加标题
# plt.title('Universal与Paramount发行电影数量占比')
# # 图例
# # plt.legend(labels)
# # 保存
# plt.savefig('./png/Universal与Paramount发行电影数量占比.png')
# # 3、展示
# plt.show()

# ======================================================================Pyecharts ======================================

# # 准备data_pair
# data_pair = [(k, v) for k, v in zip([str(tmp) for tmp in res_movie_count.index], res_movie_count.tolist())]
#
# # 1、实例化对象
# pie = Pie(
#     init_opts=opts.InitOpts(
#         width='800px',
#         height='500px',
#         theme='dark',
#         page_title='饼图'
#     )
# )
#
# # 2、添加数据
# pie.add(
#     series_name='',
#     data_pair=data_pair,
#     radius=['30%', '70%']
# )
#
# # 3、全局配置
# pie.set_global_opts(
#     title_opts=opts.TitleOpts(
#         title='Universal与Paramount发行电影数量占比',
#         pos_left='center',
#         pos_top='2%'
#     ),
#     legend_opts=opts.LegendOpts(
#         is_show=False,
#         # pos_left='center',
#         # pos_top='5%',
#         # type_='scroll'
#     )
# )
#
# # 4、系列配置
# pie.set_series_opts(
#     label_opts=opts.LabelOpts(
#         is_show=True,
#         formatter='{b}:{d}%'
#     )
# )
#
# # 5、生成图像
# pie.render('./png/Universal与Paramount发行电影数量占比.html')
# ======================================================================================================================
#  研究 Universal与Paramount发行电影数量 随时间的变化趋势
res_ = pd.pivot_table(
    data=data,
    index='release_year',
    values=['Universal', 'Paramount'],
    aggfunc='sum'
)
print('res_:\n', res_)

# ======================================================================================= matplotlib ====================
# # （1）创建画布
# plt.figure()
# # 默认不支持中文，需要修改参数，让其支持中文
# plt.rcParams['font.sans-serif'] = 'SimHei'  # 雅黑字体
# # 继续修改参数，让其继续支持负号
# plt.rcParams['axes.unicode_minus'] = False
#
# # （2）绘图
# # 横轴 ---序号
# x = np.arange(res_.shape[0])
# # 纵轴 ---各列数据
# y = res_
#
# # 绘图
# plt.plot(x, y)
#
# # 增加标题
# plt.title('Universal与Paramount发行电影数量随时间的变化趋势')
#
# # 横轴刻度
# plt.xticks(x[::10], res.index[::10], rotation=45)
#
# # 图例
# plt.legend(res_.columns, loc='upper left')
#
# # 保存
# plt.savefig('./png/Universal与Paramount发行电影数量随时间的变化趋势.png')
#
# # （3）展示
# plt.show()

# ===============需求1===================================================== pyecharts ===================================
# # 1、实例化对象
# line = Line(
#     # 初始化配置
#     init_opts=opts.InitOpts(
#         width='800px',
#         height='500px',
#         theme='dark',
#         page_title='折线'
#     )
# )
#
# # 2、添加数据
# # 横轴数据
# line.add_xaxis(
#     xaxis_data=[str(tmp) for tmp in res_.index]
# )
#
# # 纵轴数据
# for column in res_.columns:
#     line.add_yaxis(
#         series_name=column,
#         y_axis=res_.loc[:, column].tolist()
#     )
#
# # 3、全局配置
# line.set_global_opts(
#     # 标题
#     title_opts=opts.TitleOpts(
#         title='Universal与Paramount发行电影数量随时间的变化趋势',
#         pos_left='center',
#         pos_top='1%'
#     ),
#     # 图例
#     legend_opts=opts.LegendOpts(
#         is_show=True,
#         # type_='scroll',
#         type_='plain',
#         pos_left='center',
#         pos_top='6%'
#     )
# )
#
# # 4、系列配置
# line.set_series_opts(
#     label_opts=opts.LabelOpts(
#         is_show=False
#     )
# )
#
# # 5、生成图像
# line.render('./png/Universal与Paramount发行电影数量随时间的变化趋势.html')
print('*' * 100)

# 4、改编电影和原创电影的对比
# 如何确定哪些是改编电影？ 哪些是 原创电影？
# 可以通过 keywords列进行区别 原创和 改编
# 改编电影 一般都是 通过其他的参考来进行改编的， 存在 based on 这样的字眼
# 原创电影不存在

# 查看keywords
# print('keywords:\n', data.loc[:, 'keywords'])  # json字符串
# print('keywords:\n', type(data.loc[0, 'keywords']))

# 先增加一列数据
data.loc[:, 'not_original'] = 'original'

# 判断 哪些电影 是 改编的？ 如果是改编 ---->not_original列 修改为 not_original
mask = data.loc[:, 'keywords'].str.contains('based on')

# 将mask 行的 not_original列 修改为 not_original
data.loc[mask, 'not_original'] = 'not_original'

# print(data.loc[:, 'not_original'])
# 查看一下 原创与改编的数量
res_counts = pd.value_counts(data.loc[:, 'not_original'])
print('res_counts:\n', res_counts)

#  对比 原创电影 和 改编电影的数量
#  ==============================================================对比柱状图 =============================================
# # 1、创建画布
# plt.figure()
# # 默认不支持中文，需要修改参数，让其支持中文
# plt.rcParams['font.sans-serif'] = 'SimHei'  # 雅黑字体
# # 继续修改参数，让其继续支持负号
# plt.rcParams['axes.unicode_minus'] = False
# # 2、绘图
# x = np.arange(res_counts.shape[0])
# y = res_counts
#
# # 绘制
# plt.bar(x, y, width=0.5, color=['#7FFFD4', '#CDC673'])
#
# # 增加标题
# plt.title('原创电影与改编电影数量对比')
# # 横轴刻度
# plt.xticks(x, res_counts.index)
# # 纵轴名称
# plt.ylabel('数量')
# # 保存
# plt.savefig('./png/原创电影与改编电影数量对比柱状图.png')
#
# # 3、展示
# plt.show()

# =======================================================================对比柱状图--pyecharts ==========================
# 自己完成

# ======================================================================================================================
# 研究：原创电影和改编电影的平均利润、平均收入、平均预算
res_mean_profit_revenue_budget = pd.pivot_table(
    data=data,
    index='not_original',
    values=['profit', 'revenue', 'budget'],
    aggfunc='mean'
)
print('res_mean_profit_revenue_budget:\n', res_mean_profit_revenue_budget)

# 对比柱状图
# ================================================================原创电影和改编电影的收入、利润、预算的对比 ===============
# # 1、实例化对象
# bar = Bar(
#     init_opts=opts.InitOpts(
#         width='800px',
#         height='500px',
#         theme='dark',
#         page_title='原创和改编对比'
#     )
# )
# # 2、添加数据
# bar.add_xaxis(
#     xaxis_data=[str(tmp) for tmp in res_mean_profit_revenue_budget.columns],
# )
#
# # 添加纵轴
# bar.add_yaxis(
#     series_name='not_original',
#     yaxis_data=res_mean_profit_revenue_budget.loc['not_original', :].tolist(),
#     gap='0%'
# )
# #
# bar.add_yaxis(
#     series_name='original',
#     yaxis_data=res_mean_profit_revenue_budget.loc['original', :].tolist(),
#     category_gap='40%'
# )
#
# # 3、全局配置
# bar.set_global_opts(
#     title_opts=opts.TitleOpts(
#         title='原创电影和改编电影收入、利润、预算的对比',
#         pos_left='center',
#         pos_top='2%'
#
#     ),
#     legend_opts=opts.LegendOpts(
#         is_show=True,
#         pos_left='center',
#         pos_top='7%'
#     )
# )
#
# # 4、系列配置
# bar.set_series_opts(
#     label_opts=opts.LabelOpts(
#         is_show=False,
#         # position='top'
#     )
# )
#
# # 5、生成图像
# bar.render('./png/原创电影和改编电影收入、利润、预算的对比.html')

# =====================================================================================================================
# # 1、实例化对象
# bar = Bar(
#     init_opts=opts.InitOpts(
#         width='800px',
#         height='500px',
#         theme='dark',
#         page_title='原创和改编对比'
#     )
# )
# # 2、添加数据
# bar.add_xaxis(
#     xaxis_data=[str(tmp) for tmp in res_mean_profit_revenue_budget.index],
# )
#
# # 添加纵轴
# bar.add_yaxis(
#     series_name='budget',
#     yaxis_data=res_mean_profit_revenue_budget.loc[:, 'budget'].tolist(),
#     gap='0%'
# )
# #
# bar.add_yaxis(
#     series_name='profit',
#     yaxis_data=res_mean_profit_revenue_budget.loc[:, 'profit'].tolist(),
#
# )
#
# bar.add_yaxis(
#     series_name='revenue',
#     yaxis_data=res_mean_profit_revenue_budget.loc[:, 'revenue'].tolist(),
#     category_gap='40%'
# )
#
# # 3、全局配置
# bar.set_global_opts(
#     title_opts=opts.TitleOpts(
#         title='原创电影和改编电影收入、利润、预算的对比',
#         pos_left='center',
#         pos_top='2%'
#
#     ),
#     legend_opts=opts.LegendOpts(
#         is_show=True,
#         pos_left='center',
#         pos_top='7%'
#     )
# )
#
# # 4、系列配置
# bar.set_series_opts(
#     label_opts=opts.LabelOpts(
#         is_show=False,
#         # position='top'
#     )
# )
#
# # 5、生成图像
# bar.render('./png/原创电影和改编电影收入、利润、预算的对比_方式1.html')
# ======================================================================================================================
# # 1、创建画布
# plt.figure()
# # 默认不支持中文，需要修改参数，让其支持中文
# plt.rcParams['font.sans-serif'] = 'SimHei'  # 雅黑字体
# # 继续修改参数，让其继续支持负号
# plt.rcParams['axes.unicode_minus'] = False
#
# # 2、绘图
# # x ---> budget profit revenue
# x = np.arange(res_mean_profit_revenue_budget.shape[1])
#
# #
# y1 = res_mean_profit_revenue_budget.loc['not_original', :]
# y2 = res_mean_profit_revenue_budget.loc['original', :]
#
# # 设置柱子宽度
# width = 0.4
# # 绘制柱状图
# plt.bar(x + width / 2, y1, width=width)
# plt.bar(x - width / 2, y2, width=width)
#
# # 增加标题
# plt.title('原创电影和改编电影收入、利润、预算的对比')
#
# # 增加图例
# plt.legend(['not_original', 'original'], loc='upper left')
#
# # 修改横轴刻度
# plt.xticks(x, res_mean_profit_revenue_budget.columns)
#
# # 保存图片
# plt.savefig('./png/原创电影和改编电影收入、利润、预算的对比.png')
#
# # 3、展示
# plt.show()

# ======================================================================================================================
# 5、电影时长与电影票房及评分的关系
# 电影时长 ---- runtime
# 电影收入 ---- revenue
# 电影评分 ---- vote_average

# 查看数据
print('data:\n', data.loc[:, ['runtime', 'revenue', 'vote_average']])

# 检测缺失值
res_null = pd.isnull(data).sum()
print('res_null:\n', res_null)
print('*' * 100)

#  runtime 存在两个缺失值
#  处理
# 确定 runtime缺失的电影名称
mask = data.loc[:, 'runtime'].isnull()
#
movie_name = data.loc[mask, 'title']

print('movie_name:\n', movie_name)

# Chiamatemi Francesco - Il Papa della gente ---->94
# To Be Frank, Sinatra at 100 ---->81

# 填充
data.loc[data.loc[:, 'title'] == 'Chiamatemi Francesco - Il Papa della gente', 'runtime'] = 94
data.loc[data.loc[:, 'title'] == 'To Be Frank, Sinatra at 100', 'runtime'] = 81

# 研究 电影时长 和票房、评分的关系
# 需要对 电影时长离散化
# 离散化 ： 默认、等宽、等频、自定义
max_runtime = data.loc[:, 'runtime'].max()
min_runtime = data.loc[:, 'runtime'].min()
print('时长的最大值：', max_runtime)
print('时长的最小值：', min_runtime)
print('*' * 100)

# 查找 时长为0 的电影名称
# mask = data.loc[:, 'runtime'] == 0
# movie_name = data.loc[mask, 'title']
# print('movie_name:\n', movie_name)
# ---->一个一个查，填充
# cut
bins = [0, 60, 90, 120, 150, 180, 210, 350]
# 离散化
data.loc[:, 'runtime'] = pd.cut(
    x=data.loc[:, 'runtime'],
    bins=bins,
    include_lowest=True
)
# 查看离散化的结果
print(data.loc[:, 'runtime'])
print('*' * 100)
res_counts = pd.value_counts(data.loc[:, 'runtime'])
print('res_counts:\n', res_counts)
print('*' * 100)

# 可以 按照电影时长分组，统计平均票房和平均评分
res_revenue_vote = pd.pivot_table(
    data=data,
    index='runtime',
    values=['revenue', 'vote_average'],
    aggfunc='mean'
)
print('res_revenue_vote:\n', res_revenue_vote)

# 可视化 查看各个时间段内的平均收入、评分
# ======================================================================================================================
# 1、实例化对象
bar = Bar(
    init_opts=opts.InitOpts(
        width='800px',
        height='500px',
        theme='dark',
        page_title='柱状图'
    )
)
# 2、添加数据
bar.add_xaxis(
    xaxis_data=[str(tmp) for tmp in res_revenue_vote.index]
)

bar.add_yaxis(
    series_name='revenue',
    yaxis_data=res_revenue_vote.loc[:, 'revenue'].tolist(),
    yaxis_index=0,
)

bar.add_yaxis(
    series_name='vote_average',
    yaxis_data=res_revenue_vote.loc[:, 'vote_average'].tolist(),
    gap='0%',
    category_gap='40%',
    yaxis_index=1

)

# 拓展一个纵轴
bar.extend_axis(
    yaxis=opts.AxisOpts(
        type_='value',  # 数值轴
        name='vote_average',  # 坐标轴名称
        position='right',  # 坐标轴位置
        offset=0,  # 偏移
        min_=0,  # 最小值
        max_=10,  # 最大值
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color='#FFFFE0'
            )
        ),
        axislabel_opts=opts.LabelOpts(
            position='top'
        )
    )
)

# 3、全局配置
bar.set_global_opts(
    title_opts=opts.TitleOpts(
        title='不同时长电影的平均收入、评分',
        pos_top='2%',
        pos_left='center'
    ),
    legend_opts=opts.LegendOpts(
        is_show=True,
        pos_top='7%',
        pos_left='center'
    ),
    yaxis_opts=opts.AxisOpts(
        type_='value',  # 数值轴
        name='revenue',  # 坐标轴名称
        position='left',  # 坐标轴位置
        offset=0,  # 偏移
        min_=0,  # 最小值
        max_=2.5e+08,  # 最大值
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color='#FFFFE0'
            )
        ),
        axislabel_opts=opts.LabelOpts(
            position='top'
        )
    )
)

# 4、系列配置
bar.set_series_opts(
    label_opts=opts.LabelOpts(
        is_show=False
    )
)
# 5、生成图像
bar.render('./png/不同时长电影的平均收入、评分对比.html')
