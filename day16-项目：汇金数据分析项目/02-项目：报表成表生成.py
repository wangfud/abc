import pandas as pd

# 所有的数据 都匹配完成
# 构建报表成表的数据 ----val_data

# 可以使用 毛利明细表
maoLi_detail = pd.read_excel('./data/汇金样例.xls', sheet_name='毛利明细表 ')

# 筛选出 真正销售出去的数据---现货销售、临调销售
# 如果 算/不算 列 如果为空白，没有特殊说明--->销售出去
# 构建bool数组
mask = maoLi_detail.loc[:, '算/不算'].isnull()

# 筛选数据
maoLi_detail = maoLi_detail.loc[mask, :]

# 筛选特征
pivot_data = maoLi_detail.loc[:,
             ['价格是否确定', '业务部门-新', '品名-新', '产地-新', '重量', '销售金额-新', '进货金额-新', '利息补差金额', '毛利润', '费用金额', '净利润']]

# 生成报表成表
res = pd.pivot_table(
    data=pivot_data,
    index=['价格是否确定', '业务部门-新', '品名-新', '产地-新'],
    aggfunc='sum'
)
print('res:\n',res)
# 保存
res.to_excel('./data/报表成表.xls')
