# 真实的企业中，数据分析 ----操作不是难点，在于具体业务
# 难点：理解具体的业务逻辑、相关术语、相关概念
# 该公司的主营业务：对钢卷进行采购、加工、售卖
# 收集了很多数据：关于钢卷的财务数据 -----利润
# Python重构项目：利润计算

# 毛利明细表：
# 存在3种表头
# 白色表头： ---从该公司系统直接导出的原始数据
# 绿色表头： ---自己内部员工和 后续的系统导出数据进行 手工匹配的数据
# 蓝色表头： ---计算得到的（纯的excel操作）

# 单据类型中 ----销售实提 ---以钢卷号(N)为关键字段

# 采购类型F
# 自营采购     # ----->真真正正的采购
# 临调采购     # ---->真真正正的采购
# 倒货采购     # ---->公司内部部门之间的采购

# 销售类型G
# 现货销售   # --->直接销售出去
# 临调销售   # ---->直接销售出去
# 倒货销售   # ---->公司内部部门之间的销售

# 钢卷号N
# 单一钢卷的唯一标示，钢卷号为空的条目应用其他逻辑。

# 算/不算单据（BF）
# 不算，倒货销售,二次入库未销售 -----没有销售出去
# 不算，单卷冲减

# 实际补差单价（BI）
# 虚补差单价（BJ）
# 毛利明细表 和 补差报表  根据某些规则计算的

# 唐钢老库存补差单价（BK）
# 毛利明细表 和 唐钢老合同补差表 根据某些规则计算的

# 费用补差单价（BO）
# 毛利明细表和 费用补差表 确定的

# 业务毛利润（净利润/CG）的计算方法
# 销售金额-进货金额-利息补差金额-费用金额=净利润，即业务毛利润。

# 导包
import pandas as pd
import numpy as np

# 加载数据
df = pd.read_excel('./data/汇金样例.xls', sheet_name=None)
# print('df:\n', df.keys())
# 获取不同的dataframe
maoLidetail = df['毛利明细表 ']
ruKuYibiaozhu = df['入库已标注确定与暂估']
buChaBaobiao = df['补差报表']
caiGouBucha = df['采购补差']
feiYongBucha = df['费用补差']
TangGangLaohetong = df['唐钢老合同补差']
GenZongJiesuan = df['跟踪结算价 ']

# print('maoLidetail:\n', maoLidetail.columns)
# print('maoLidetail:\n', maoLidetail.shape)
# print('*' * 100)
print('ruKuYibiaozhu:\n', ruKuYibiaozhu.columns)
print('ruKuYibiaozhu:\n', ruKuYibiaozhu.shape)
print('*' * 100)
print('buChaBaobiao:\n', buChaBaobiao.columns)
print('buChaBaobiao:\n', buChaBaobiao.shape)
print('*' * 100)
print('caiGouBucha:\n', caiGouBucha.columns)
print('caiGouBucha:\n', caiGouBucha.shape)
print('*' * 100)
print('feiYongBucha:\n', feiYongBucha.columns)
print('feiYongBucha:\n', feiYongBucha.shape)
print('*' * 100)
print('TangGangLaohetong:\n', TangGangLaohetong)
print('TangGangLaohetong:\n', TangGangLaohetong.columns)
print('TangGangLaohetong:\n', TangGangLaohetong.shape)
print('*' * 100)
print('GenZongJiesuan:\n', GenZongJiesuan.columns)
print('GenZongJiesuan:\n', GenZongJiesuan.shape)
print('*' * 100)

# 构建毛利明细表中的列索引
columns = ['单据类型', '单据号', '单据类型.1', '日期', '发货日期', '采购类型', '销售类型', '物资属性', '大类',
           '包装类型', '大小卷', '连罩退', '等级', '钢卷号', '卡号', '品种', '品名', '材质', '规格', '产地',
           '数量', '重量', '结算数量', '结算重量', '数量单位', '重量单位', '销售定价', '销售单价', '销售金额',
           '销售费用单价', '销售费用金额', '进货单价', '进货金额', '进货费用单价', '进货费用金额', '承兑加价', '正负溢价',
           '单价差', '毛利', '计量方式', '仓库', '订货合同号', '销售合同号', '库位', '物资备注', '合同号',
           '货权机构', '业务机构', '业务部门', '采购业务员', '业务员', '备注']

# 筛选毛利明细表
maoLidetail = maoLidetail.loc[:, columns]
print('原始的毛利明细表：\n', maoLidetail.columns)
print('原始的毛利明细表：\n', maoLidetail.shape)

print('==' * 100)
# =========================================================数据加载完成 ==================================================

# 1、匹配： 毛利明细表 与 入库已标注确定与暂估 合并
# 利用钢卷号进行合并 ---> 将 入库已标注确定与暂估表中的 价格是否确定、钢卷号 按照钢卷号为键 合并到毛利明细表

# （1）先将 毛利明细表中 钢卷号中的 .去掉
maoLidetail.loc[:, '钢卷号1'] = maoLidetail.loc[:, '钢卷号'].str.split('.')[0]
# （2）合并
maoLi_ruKu = pd.merge(left=maoLidetail, right=ruKuYibiaozhu.loc[:, ['钢卷号', '价格是否确定']], left_on='钢卷号1', right_on='钢卷号',
                      how='left')
# （3）剔除 钢卷号_y
maoLi_ruKu.drop(labels='钢卷号_y', axis=1, inplace=True)
# （4） 将 钢卷号_x 修改为 钢卷号
maoLi_ruKu.rename(columns={'钢卷号_x': '钢卷号'}, inplace=True)

# print('maoLi_ruKu:\n', maoLi_ruKu.columns)

# 2、利用 补差报表 来匹配 毛利_入库表
# （1） 利用 单据号 将  补差报表中的 单据号和 备注J匹配到 毛利_入库
maoLi_ruKu_buCha = pd.merge(left=maoLi_ruKu, right=buChaBaobiao.loc[:, ['单据号', '备注']], on='单据号', how='left')
print('maoLi_ruKu_buCha:\n', maoLi_ruKu_buCha.columns)
print('*' * 100)

# （2）如为齐，则毛利表 BF 备注不算，单卷冲减，净利润 CG 直接修改为 0
mask = maoLi_ruKu_buCha.loc[:, '备注_y'] == '齐'
#
maoLi_ruKu_buCha.loc[mask, '算/不算'] = '不算，单卷冲减'
maoLi_ruKu_buCha.loc[mask, '净利润'] = 0


# （3）如备注 J 为无明细，则利用毛利表备注 AZ，查找跟踪结算价表对应合同号 A，
# 确定该条记录结算价 是否确定 J 内容，并将其匹配至毛利表价格是否确定 BS。
def func(val):
    """
    获取备注中的合同号
    :param val:
    :return:
    """
    if val:
        if str(val) == '质量异议赔款，做余款':
            val = np.nan

        val = str(val).replace('虚', '')
        # 拆分
        res = val.split(' ')
        # 遍历
        for tmp in res:
            if str(tmp).startswith('CGHT'):
                val = tmp

    return val


# a、提取 --- 备注_x 中的合同号
maoLi_ruKu_buCha.loc[:, '备注合同号'] = maoLi_ruKu_buCha.loc[:, '备注_x'].transform(func)
print('备注合同号:\n', maoLi_ruKu_buCha.loc[:, '备注合同号'])

# b、 按照 备注合同号 和 跟踪结算价表 的合同号 进行匹配, 将跟踪结算价表 的合同号 和 结算价是否确定 匹配到毛利表中
maoLi_ruKu_buCha_Genzong = pd.merge(left=maoLi_ruKu_buCha, right=GenZongJiesuan.loc[:, ['合同号', '结算价是否确定']],
                                    left_on='备注合同号', right_on='合同号',
                                    how='left')

# 将 结算价是否确定 的 备注合同号=合同号_y的行 的值 放入 价格是否确定列去
mask = maoLi_ruKu_buCha_Genzong.loc[:, '备注合同号'] == maoLi_ruKu_buCha_Genzong.loc[:, '合同号_y']
# print('mask:\n', mask)

maoLi_ruKu_buCha_Genzong.loc[mask, '价格是否确定'] = maoLi_ruKu_buCha_Genzong.loc[mask, '结算价是否确定']

# 删除 掉 结算价是否确定 ,合同号_y
maoLi_ruKu_buCha_Genzong.drop(labels=['结算价是否确定', '合同号_y'], axis=1, inplace=True)

# 将 合同号_x 修改为 合同号
maoLi_ruKu_buCha_Genzong.rename(columns={'合同号_x': '合同号'}, inplace=True)

print('maoLi_ruKu_buCha_Genzong:\n', maoLi_ruKu_buCha_Genzong.columns)
print('*' * 100)

# 3、与采购补差表进行匹配
# 根据采购补差表钢卷号 F 匹配毛利表钢卷号 N，将采购补差表找补单价I 按照虚拟 M 的类型（空白 为实际补差单价，虚为虚补差单价），
# 匹配至毛利表实际补差单价 BI 与虚补差单价 BJ。
# （1） 将 采购补差表中的 卷号 修改为 钢卷号1
caiGouBucha.rename(columns={'卷号': '钢卷号1'}, inplace=True)
# （2） 虚补差单价 确定
# 确定 哪些行？ 是 虚
xu = caiGouBucha.loc[:, '虚拟'] == '虚'
# 合并
maoLi_ruKu_buCha_Genzong_caiBu = pd.merge(left=maoLi_ruKu_buCha_Genzong, right=caiGouBucha.loc[xu, ['找补单价', '钢卷号1']],
                                          on='钢卷号1', how='left')

# 将 找补单价 修改为 虚补差单价
maoLi_ruKu_buCha_Genzong_caiBu.rename(columns={'找补单价': '虚补差单价'}, inplace=True)

# （3）实补差单价确定
# 确定哪些行 是 空白
shi = caiGouBucha.loc[:, '虚拟'].isnull()
maoLi_ruKu_buCha_Genzong_caiBu = pd.merge(left=maoLi_ruKu_buCha_Genzong_caiBu,
                                          right=caiGouBucha.loc[shi, ['找补单价', '钢卷号1']], on='钢卷号1', how='left')

# 将 找补单价 修改为 实补差单价
maoLi_ruKu_buCha_Genzong_caiBu.rename(columns={'找补单价': '实补差单价'}, inplace=True)
print('maoLi_ruKu_buCha_Genzong_caiBu:\n', maoLi_ruKu_buCha_Genzong_caiBu.columns)

# 4、与费用补差表进行匹配
# 将 费用补差表中 的 钢卷号、找补单价 按照钢卷号 匹配到毛利明细表中 ----->找补单价---->费用补差单价BO
# （1）先将 费用补差表中 的 钢卷号  修改为 钢卷号1
feiYongBucha.rename(columns={'钢卷号': '钢卷号1'}, inplace=True)
# （2）主键拼接
maoLi_ruKu_buCha_Genzong_caiBu_feiyong = pd.merge(left=maoLi_ruKu_buCha_Genzong_caiBu,
                                                  right=feiYongBucha.loc[:, ['钢卷号1', '找补单价']], on='钢卷号1', how='left')

# （3）将 找补单价  修改为 费用补差单价
maoLi_ruKu_buCha_Genzong_caiBu_feiyong.rename(columns={'找补单价': '费用补差单价'}, inplace=True)

# print('maoLi_ruKu_buCha_Genzong_caiBu_feiyong:\n', maoLi_ruKu_buCha_Genzong_caiBu_feiyong.columns)

# 5、与唐钢老合同表进行匹配
# 将唐钢老合同表 中的 钢卷号、找补单价   按照钢卷号 匹配到 毛利明细表中，  找补单价 ---->唐钢老库存补差单价

# # （1）将 唐钢老合同表 钢卷号  改为 钢卷号1
TangGangLaohetong.rename(columns={'钢卷号': '钢卷号1'}, inplace=True)
# # （2）主键拼接
maoLi_ruKu_buCha_Genzong_caiBu_feiyong_TG = pd.merge(left=maoLi_ruKu_buCha_Genzong_caiBu_feiyong,
                                                     right=TangGangLaohetong.loc[:, ['钢卷号1', '找补单价']], on='钢卷号1',
                                                     how='left')
# （3）将找补单价 修改为 唐钢老库存补差单价
maoLi_ruKu_buCha_Genzong_caiBu_feiyong_TG.rename(columns={'找补单价': '唐钢老库存补差单价'}, inplace=True)
#
# print('maoLi_ruKu_buCha_Genzong_caiBu_feiyong_TG:\n', maoLi_ruKu_buCha_Genzong_caiBu_feiyong_TG.columns)

all_data = maoLi_ruKu_buCha_Genzong_caiBu_feiyong_TG
print('all_data:\n', all_data.columns)
print('*' * 100)

# 已知匹配出的列：BF、BI BJ BK BO BS
# 暂时不知的列：BA BB BC BD BE BG BH BL BM BN BP BQ BR BT BU BV  --->如果已知这些列的匹配过程

# 6、计算周期内业务毛利润（净利润/CG）
# 根据公司业务特点，某钢卷自钢厂采购至最终销售终端客户，期间可能经多次公司内部转手，形 成内外部一些列业务毛利润，需要进行加总
# 部分钢卷在采销链条中，并未完成最终销售，不能计入业务毛利润计算，需要进行剔除
# 首先关注毛利表销售类型 G，选择现货销售，代表该钢卷完成采销链条，根据钢卷号 N 锁定的自采购至最终销售的全部相同钢卷号记录，全部计入业务毛利润；
# 销售类型为临调销售，直接计入业务毛利润
# 如销售类型为倒货销售，且同钢卷号（无论是否加“.”）无其他现货销售记录，则该条不计入业 务毛利润
# （1）确定现货销售的数据 --钢卷号
mask = all_data.loc[:, '销售类型'] == '现货销售'
# 现货销售的钢卷号
XianHuo_GJH = all_data.loc[mask, '钢卷号']
# （2）对 XianHuo_GJH 中的带点 和不带点 进行处理
XianHuo_GJH = XianHuo_GJH.str.split('.').str[0]
print('XianHuo_GJH:\n', XianHuo_GJH)
print('*' * 100)

# 判定 所有毛利明细表中的钢卷号 是否都在 XianHuo_GJH中
# 多对多的过程 ---存在先倒货销售到别的部分，最后进行现货销售
# 判定 钢卷号1 所有的钢卷号是否都在 XianHuo_GJH, 如果在，则为True，保留，如果不在，说明 可能未销售出去
mask_XianHuo = all_data.loc[:, '钢卷号'].str.split('.').str[0].isin(XianHuo_GJH)
# 筛选出 现货销售 所有的 数据
XianHuo_data = all_data.loc[mask_XianHuo, :]
print('XianHuo_data:\n', XianHuo_data)

# 存在 倒货销售 --->没有销售 ----剔除
# 拿到所有的倒货销售的数据
mask = all_data.loc[:, '销售类型'] == '倒货销售'

# 拿取到 所有非现货销售的数据
fei_XianHuo_mask = mask_XianHuo.transform(lambda x: not (x))

# 既属于 倒货销售， 又属于 非现货销售  ---->没有销售出去
mask = mask & fei_XianHuo_mask

# 将 没有卖出去的  修改 为不算利润
all_data.loc[mask, '算/不算'] = '不算，倒货销售,二次入库未销售'

# 筛选出临调销售的数据
mask = all_data.loc[:, '销售类型'] == '临调销售'

LinDiao_data = all_data.loc[mask, :]

# 需要将  现货销售的数据 和 临调销售的数据 合并起来 -----真真产生利润的数据
val_data = pd.concat((XianHuo_data, LinDiao_data), axis=0)

# 将 val_data(即计算利润的数据)  和 all_data(Python合并的数据) 进行保存  ----excel
# 构建一个writer
writer = pd.ExcelWriter('./data/all_data.xls')

# 写入writer
val_data.to_excel(excel_writer=writer, sheet_name='val_data')
all_data.to_excel(excel_writer=writer, sheet_name='all_data')

# 保存
writer.save()

# 关闭writer
writer.close()
