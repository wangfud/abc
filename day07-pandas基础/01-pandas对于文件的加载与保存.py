# csv --->逗号分隔的，有序的，序列文本文件。
# excel --->表格文件，以.xls .xlsx .xlsm为结尾的表格文件

import pandas as pd

# # 加载数据 --pd.read_xxx()格式
# # csv数据
# info = pd.read_csv(
#     filepath_or_buffer='./data/meal_order_info.csv',  # 文件路径+ 名称
#     sep=',',  # 分隔符
#     # delimiter=',', # 分隔符
#     encoding='ansi',  # 编码格式
#     # header="infer",  # header="infer",表示加载数据的时候，列索引自动识别，可以指定行下标使得某行作为列索引。
#     # index_col=0,  # 可以指定某列作为行索引
#     # usecols=['info_id', 'emp_id'], # 可以指定只加载某些列
#     # usecols=[0, 1],  # 可以指定只加载某些列
#     # names=['aa','bb'], # 可以指定新的列索引
#     # nrows=10, # 可以指定只加载前n行
#     # skiprows=10,  # 可以跳过前n行，然后加载数据
# )
# print('info:\n', info)
# print('info:\n', type(info))  # <class 'pandas.core.frame.DataFrame'>
#
# # 保存dataframe到csv文件中去
# # 保存：df.to_xxxx()
# info.to_csv(
#     path_or_buf='./data/aaa.csv',  # 保存的路径+ 名称
#     sep=',',  # 分隔符
#     # header=False,  # 默认为True，需要保存列索引，如果为False，则不保存列索引
#     # index=False,  # 默认为True，需要保存行索引，如果为False，则不保存行索引
#     mode='a',  # 默认为写模式，保存时候，会覆盖原内容，如果置为a,则为追加
# )

# 加载excel
# detail = pd.read_excel(
#     io='./data/meal_order_detail.xls',  # 文件路径+名称
#     sheet_name=0,  # 表示加载的excel中的第0个sheet
#     # 其他参数可参考read_csv理解
# )
# print('detail:\n', detail)
# print('detail:\n', type(detail))  # <class 'pandas.core.frame.DataFrame'>

# 加载excel中所有的sheet
fp = pd.read_excel(
    io='./data/meal_order_detail.xls',  # 文件路径+名称
    sheet_name=None,
    # 其他参数可参考read_csv理解
)
# print('fp:\n', fp)
# print('fp:\n', type(fp))  # 字典类型
# 获取字典中的key
print('fp:\n', fp.keys())  # 获取的excel中所有的sheet的名称
# 可以通过映射关系来获取具体的df
meal_order_detail1 = fp['meal_order_detail1']
meal_order_detail2 = fp['meal_order_detail2']
meal_order_detail3 = fp['meal_order_detail3']
print('meal_order_detail1:\n', meal_order_detail1)
print('*' * 100)
print('meal_order_detail2:\n', meal_order_detail2)
print('*' * 100)
print('meal_order_detail3:\n', meal_order_detail3)

# 保存 成 excel
# meal_order_detail1.to_excel(
#     excel_writer='./data/bbb.xls',  # 路径+名称
#     sheet_name='Sheet1',  # 保存的sheet名
# )
# meal_order_detail2.to_excel(
#     excel_writer='./data/bbb.xls',  # 路径+名称
#     sheet_name='Sheet2',  # 保存的sheet名
# )
# meal_order_detail3.to_excel(
#     excel_writer='./data/bbb.xls',  # 路径+名称
#     sheet_name='Sheet3',  # 保存的sheet名
# )
# 以上方式的保存，会覆盖前一次保存的内容

# 如果想要将多个sheet保存到一个excel中
# 借助 ExcelWriter来完成
writer = pd.ExcelWriter(
    path='./data/bbb.xls',  # 路径+ 文件名称
)
# 写入writer
meal_order_detail1.to_excel(
    excel_writer=writer,
    sheet_name='Sheet1'
)
meal_order_detail2.to_excel(
    excel_writer=writer,
    sheet_name='Sheet2'
)
meal_order_detail3.to_excel(
    excel_writer=writer,
    sheet_name='Sheet3'
)
# 保存
writer.save()
# 关闭
writer.close()


