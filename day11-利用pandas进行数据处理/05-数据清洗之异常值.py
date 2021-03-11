# 异常值
# 远离数值的正常范围的错误的值 ---异常值
import pandas as pd


# 判定异常值
# （1）具体业务法
# 根据具体的业务要求，制定数据的阈值，来判断的数据是否为异常值
# 如：销量>0 ,如年龄一般在(0,100]之间，如:身高[30,220]
# def juti_yewu(data):
#     """
#     根据具体业务法剔除异常值 ---身高
#     :param data: Series
#     :return: mask--bool数组
#     """
#     # 上限
#     up = 220
#     # 下限
#     low = 30
#     # 比较
#     mask = (data >= low) & (data <= 220)
#
#     return mask
#
#
# # 创建df
# df = pd.DataFrame(
#     data={
#         'name': ['zs', 'ls', 'ww', 'zl'],
#         'hight': [178, 230, 20, 168],
#     },
#     index=['stu0', 'stu1', 'stu2', 'stu3']
# )
# print('df:\n', df)
#
# # 验证
# mask = juti_yewu(df.loc[:, 'hight'])
# # 筛选
# df = df.loc[mask, :]
# print('剔除身高异常值的结果为：\n', df)

# （2）3sigma原则
# 3sigma原则---正态分布 ---99.73% 都在(u-3a,u+3a)之间 --->剩下的0.27%可以认为是异常的值
def three_sigma(data):
    """
    3sigma原则剔除异常值
    :param data: Series
    :return: mask--bool数组
    """
    # 确定上限
    up = data.mean() + 3 * data.std()
    # 确定下限
    low = data.mean() - 3 * data.std()

    # 比较
    mask = (data > low) & (data < up)

    return mask


# （3）箱线分析法
# 借助四分位数进行异常值的剔除
# 上四分位数 ---75%位置的数 --qu
# 下四分位数 ---25%位置的数 --ql
# 四分位间距---- 上四分位数 - 下四分位数 --->即 qu-ql -->iqr
# 规定：在（qu + 1.5iqr,ql-1.5iqr）正常的值，超过该范围--->异常值
def box_analysis(data):
    """
    箱线分析法来剔除异常值
    :param data: Series
    :return: mask ---bool数组
    """
    # 确定上四分位数
    qu = data.quantile(q=0.75)
    # 确定下四分位数
    ql = data.quantile(q=0.25)
    # 确定四分位间距
    iqr = qu - ql
    # 确定上限
    up = qu + 1.5 * iqr
    # 确定下限
    low = ql - 1.5 * iqr
    # 比较
    mask = (data > low) & (data < up)

    return mask
