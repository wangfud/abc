# import pandas as pd
#
# # 加载数据
# credits = pd.read_csv('./data/tmdb_5000_credits.csv')
# movies = pd.read_csv('./data/tmdb_5000_movies.csv')
# # 查看数据
# # print('credits:\n', credits.head(5))
# # print('credits:\n', credits.shape)
# # print('credits:\n', credits.columns)
#
# # print('movies:\n', movies.head(5))
# # print('movies:\n', movies.shape)
# # print('movies:\n', movies.columns)
# # print('*' * 100)
#
# # 需要将 credits 和 movies 进行合并
# # 先将 credits 中的 movie_id  ---->id
# credits.rename(columns={'movie_id': 'id'}, inplace=True)
# # print('credits:\n', credits.head(5))
# # print('credits:\n', credits.shape)
# # print('credits:\n', credits.columns)
# # 按照 电影名称 及 电影id ---主键合并
# # outer ---> 可能会造成存在大量缺失值 --->电影都已经上映，如果信息缺失，上网查询具体电影的详细信息
# data = pd.merge(left=credits, right=movies, on=['id', 'title'], how='outer')
# print('data:\n', data.head())
# print('data:\n', data.shape)
# print('data:\n', data.columns)

# # 需求：
# # 1、电影类型和时间的关系
# # 2、电影类型和利润的关系
# # 3、Universal 和 Paramount 两家影视公司的对比
# # 4、改编电影和原创电影的对比
# # 5、电影时长与电影票房及评分的关系

