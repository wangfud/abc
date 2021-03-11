import numpy as np

# 加载数据
fp = np.load('./data/lol_data.npz')
print('fp:\n', fp)  # <numpy.lib.npyio.NpzFile object at 0x0000000001DBF608>
# 通过遍历的方式来获取key
for tmp in fp:
    print(tmp)
# 通过key来获取保存的数组
columns = fp['columns']
data = fp['data']
print('columns:\n', columns)
# print('data:\n', data)
# print('data:\n', data.shape)
# columns中的各个元素是data中各个列的名称、解释、说明

# 由于数据中存在重复的数据---需要对数据进行去重
data = np.unique(data, axis=0)
print('data:\n', data)
print('data:\n', data.shape)

# (1) 员工的平均薪资为多少？
# # 获取 薪资 数据
# salary = data[:, 4]
# # 修改数据类型
# # salary = np.int32(salary)
# salary = salary.astype(np.int32)
# # 获取平均薪资
# avg_salary = salary.mean()
# print('平均薪资为：\n', avg_salary)

# (2) 公司任职最久的员工是谁？
# # 获取工龄
# work_year = data[:, 5]
# # 修改类型
# work_year = work_year.astype(np.int32)
# # 获取最大工龄
# max_work_year = np.max(work_year)
# # 比较运算，获取最大工龄所对应的bool数组
# mask = data[:, 5] == str(max_work_year)
# # 利用bool数组索引行，并获取员工姓名
# worker_name = data[mask, 1][0]
# print('任职最久的员工姓名为:', worker_name)

# (3) 员工的平均工作年限是多少？
# 获取工龄
work_year = data[:, 5]
# 修改类型
work_year = work_year.astype(np.int32)
# 获取平均工作年限
avg_work_year = work_year.mean()
print('员工的平均工作年限为：', avg_work_year)
# (4)员工总体流失率是多少？
# 流失率 = 流失的员工 / 总数
# 获取员工总数
all_num = data.shape[0]
# bool数组索引
mask = data[:, -1] == '离职'
# 获取离职人数
# out_num = mask.sum()
out_num = data[mask,:].shape[0]
# 获取流失率
print('员工的总体流失率为：', out_num / all_num)

# （5）员工整体满意程度如何？
# 获取满意度
sta = data[:, -2]
# 修改类型
sta = sta.astype(np.int32)
# 计算平均满意度
avg_sta = sta.mean()
print('员工的平均满意度为：', avg_sta)
