import pandas as pd
import os

# # 先处理一个 垂钓装备
# excel_name = '垂钓装备&抄网.xlsx'
# # 加载数据
# data = pd.read_excel(io='./data/cd_data/' + excel_name, sheet_name=0)
#
# # 计算销售额
# data.loc[:, '销售额'] = data.loc[:, '转化率'] * data.loc[:, '访客数'] * data.loc[:, '客单价']
# print('data:\n', data)
# print('*' * 100)
#
# # 计算各个品牌的 抄网 销售额之和
# # 按照 品牌 进行分组，统计销售额的sum
# df = pd.pivot_table(
#     data=data,
#     index='品牌',
#     values='销售额',
#     aggfunc='sum'
# )
# # 重设索引
# df = df.reset_index()
#
# # 按照销售额 进行排序
# df = df.sort_values(by='销售额', ascending=False)
#
# # 增加类目
# df.loc[:, '类目'] = excel_name.split('.')[0]
#
# print('df:\n', df)

####################################################################################################
# 获取所有的excel文件名称
file_name_list = os.listdir('./data/cd_data/')
print('file_name_list:\n', file_name_list)

# 定义一个空的df
all_df = pd.DataFrame()

# 循环处理每一个文件
for file_name in file_name_list:
    # 加载文件
    data = pd.read_excel('./data/cd_data/' + file_name, sheet_name=0)
    # 计算销售额
    data.loc[:, '销售额'] = data.loc[:, '转化率'] * data.loc[:, '访客数'] * data.loc[:, '客单价']
    # print('data:\n', data)
    # 按照 品牌分组，统计销售额的sum
    df = pd.pivot_table(data=data, index='品牌', values='销售额', aggfunc='sum').reset_index()
    # 增加类目
    df.loc[:, '类目'] = file_name.split('.')[0]
    # print('df:\n', df)
    # print('*' * 100)
    # 将各个子df进行合并到一起
    all_df = pd.concat(objs=(all_df, df), axis=0, join='outer', ignore_index=True)

# 查看总的数据
# 按照品牌分组，统计销售额的sum
all_df = pd.pivot_table(
    data=all_df,
    index='品牌',
    values='销售额',
    aggfunc='sum'
).reset_index().sort_values(by='销售额',
                            ascending=False).head(5)

print('all_df:\n', all_df)
