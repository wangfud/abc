import pandas as pd

# 加载数据
fp = pd.read_excel('./data/重叠合并数据.xls', sheet_name=None, index_col=0)
# print('fp:\n', fp)

# 获取dataframe
df1 = fp['Sheet1']
df2 = fp['Sheet2']

print('df1:\n',df1)
print('df2:\n',df2)

# df1 和 df2 结构基本相同，只是df1中含有大量缺失值
# 重叠合并
# 利用df2中的数据来填充df1中的对应位置
res = df1.combine_first(df2)
print('res:\n',res)
