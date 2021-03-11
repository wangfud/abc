from my_dataset import *
from torch.utils.data import DataLoader
# 导入图像处理模块
from torchvision.transforms import transforms
#
from lenet import *

import torch.optim as optim

import torch

import cv2

# 定义批次数量
BATCH_SIZE = 16

# 定义学习率
LR = 0.01

# 定义训练的最大论数
MAX_EPOCH = 10

# 图片数据的均值、标准差
# Image-net 大赛中使用的图片的均值、标准差
norm_mean = [0.485, 0.456, 0.406]
norm_std = [0.229, 0.224, 0.225]

# ================================1、数据部分=============================================================================
# （1） 收集数据 ---特征和目标一一对应的关系
# （2） 数据集拆分---拆分为训练集、验证集、测试集
# （3） 数据读取与分批 --需要实现Dataset 和 Dataloder
# （4） 图像数据预处理--- 图像尺寸固定、转化为tensor、归一化处理
# 指定数据集的主路径
split_dir = './dataset/rmb_split/'

# 指定训练集路径
train_dir = os.path.join(split_dir, 'train')

# 指定验证集路径
valid_dir = os.path.join(split_dir, 'valid')

print('train_dir:\n', train_dir)
print('valid_dir:\n', valid_dir)

# 规定图像数据的处理方式
# 参数：列表---列表中放置的是各种图片数据处理方式
# 返回一个数据处理对象
transform = transforms.Compose([
    # 图片尺寸固定
    transforms.Resize((32, 32)),  # 将图片固定为32*32的大小
    # 将数据转化为tensor
    transforms.ToTensor(),  # 转化为 tensor
    # 图片数据的归一化
    # data - mean / std
    transforms.Normalize(mean=norm_mean, std=norm_std),
])

# 实例化DataSet
train_data = RMBDataSet(data_dir=train_dir, transform=transform)
valid_data = RMBDataSet(data_dir=valid_dir, transform=transform)

# 实例化DataLoader
train_loader = DataLoader(
    dataset=train_data,  # 规定的是数据的读取规则
    batch_size=BATCH_SIZE,  # 每批次读取多少个样本
    shuffle=True,  # 打乱顺序
)
valid_loader = DataLoader(
    dataset=valid_data,  # 规定的是数据的读取规则
    batch_size=BATCH_SIZE,  # 每批次读取多少个样本
    shuffle=True,  # 打乱顺序
)

# print('train_loader:\n', train_loader)
# print('valid_loader:\n', valid_loader)

# ================================2、网络部分=============================================================================
#  自定义卷积神经网络
#  a、确定网络的各个层次结构
#  b、正向传播
#  c、初始化网络中的参数--卷积的权重、偏置；fc的权重、偏置
# 实例化网络对象
net = LeNet(classes=2)
# 初始化网络参数
net.initialize_weight()

# ================================3、损失部分=============================================================================
# 交叉熵损失
losses = nn.CrossEntropyLoss()

# ================================4、优化部分=============================================================================
# sgd随机梯度下降优化算法
# 参数params：网络中所有的参数 net.parameters()
# 参数lr: 学习率
# 参数momentum： 表示动量，如果为0，表示在梯度下降过程中，优化所有的参数
# 如果给 momentum 为一个非0值，表示在梯度下降过程中，每一次优化的时候，只优化 1- momentum的参数，
# 保证 momentum 的参数为固定的
# 返回优化器对象
optimizer = optim.SGD(params=net.parameters(), lr=LR, momentum=0.9)

# 指定学习率的变化情况
# 参数optimizer：优化器，指定的是该优化器的学习率变化情况
# 参数step_size：指定每隔多少次训练变化一次学习率
# 参数gamma： 指定学习率如何变化， ===》新的学习率  = 原来的学习率 * gamma
scheduler = optim.lr_scheduler.StepLR(optimizer=optimizer, step_size=10, gamma=0.1)

# # ================================5、训练部分=============================================================================
# # 开始训练   --->保存模型
# # train_loader----加载数据----一个批次----往网络里面输入---正向传播---预测值、loss---反向传播---优化器-梯度下降
# # 一轮训练可能不会出现最优结果---多轮训练
# for epoch in range(MAX_EPOCH):
#     # epoch --> 代表 第 多少轮
#
#     # 总样本个数：
#     total = 0
#     # 预测准确的样本个数
#     correct = 0
#
#     # 每轮的平均损失
#     loss_mean = 0
#
#     # 开始训练
#     net.train()
#
#     # 从数据装载器去获取一个批次数据
#     for i, data in enumerate(train_loader):
#         # i : 批次的下标
#         # data :每批次的数据
#         # data --->loader里面 dataset 里面 __getitem__返回值， ---一次性返回一个批次
#         img, label, img_path = data
#         # print('img:\n', img)
#         # print('label:\n', label)
#         # print('img_path:\n', img_path)
#         # print('*' * 100)
#
#         # 将该批次的特征值输入到卷积神经网络，开始正向传播，得到预测值
#         # output = net(img)  # 注意---> 等同于 net.forward(img)
#         output = net.forward(img)
#         # print('output:\n', output)
#
#         # 计算 交叉熵损失
#         loss = losses(output, label)
#
#         # 需要将网络中的梯度清0
#         net.zero_grad()
#
#         # 反向传播
#         loss.backward()
#
#         # 梯度下降
#         optimizer.step()  # 更新权重和偏置
#
#         # 查看一下预测类别---返回2个值，第一个值为该批次预测大的概率，第二个值为预测值的类别
#         # res = torch.max(output.data, 1)
#         # print('res:\n', res)
#         #  torch.return_types.max(
#         # values=tensor([0.7053, 0.7051, 0.6045, 0.5377, 0.5200, 0.5309, 0.5937, 0.6452, 0.6040,
#         #         0.6102, 0.7168, 0.5782, 0.5971, 0.5765, 0.5640, 0.6896]),
#         # indices=tensor([0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0]))
#         _, predicted = torch.max(output.data, 1)
#         # print('该批次的预测结果为：\n', predicted)
#         # print('该批次的真实结果为：\n', label)
#
#         # 该批次 预测准确的个数
#         # print('预测准确的个数：\n', (predicted == label).sum().numpy())
#         correct += (predicted == label).sum().numpy()
#         # 计算样本总个数
#         total += label.size(0)
#
#         # 查看该批次的损失
#         # print('该批次的损失为：', loss.item())
#         # 加入到loss_mean
#         loss_mean += loss.item()
#
#         # 每10个批次，打印一下训练信息
#         if (i + 1) % 10 == 0:
#             # 计算 这10个批次的平均损失
#             loss_mean = loss_mean / 10
#
#             print('第 %d 轮的 第 %d 批次的训练的准确率为: %f ,平均损失为：%f' % (epoch + 1, i + 1, correct / total, loss_mean))
#
#         # print('*' * 100)
#
#         # 调整学习率 ---注意：训练10个批次再去调整学习率
#         # scheduler.step()
#
#     # 每训练一轮进行验证一次
#     if (epoch + 1) % 1 == 0:
#         # 进行验证
#         # 以下是在验证集上工作
#
#         # 定义一个变量，来储存在验证集上的预测正确的样本个数
#         correct_val = 0
#
#         # 定义一个变量，来存储在验证集上的样本总个数
#         total_val = 0
#
#         # 定义一个变量，来存储验证集上的平均损失
#         loss_mean_val = 0
#
#         # 开始验证
#         net.eval()
#
#         # 不需要反向传播、不需要梯度下降
#         with torch.no_grad():
#             # # 在验证集上获取数据，正向传播得到预测值，与真实值进行比较
#             for j, data in enumerate(valid_loader):
#                 # j: 表示批次的下标
#                 # data --数据
#                 img_val, label_val, img_path_val = data
#
#                 # 正向传播
#                 output_val = net(img_val)
#                 # print('output_val:\n', output_val)
#
#                 # 计算损失
#                 loss_val = losses(output_val, label_val)
#
#                 # 计算预测的类别
#                 _, predicted_val = torch.max(output_val.data, 1)
#
#                 # 对比真实值与 预测类别
#                 # print('该批次预测准确的样本个数:', (label_val == predicted_val).sum().numpy())
#
#                 # 查看 该批次的损失
#                 # print('该批次的损失为：', loss_val.item())
#
#                 #  预测准确的个数
#                 correct_val += (label_val == predicted_val).sum().numpy()
#
#                 # 样本总个数
#                 total_val += label_val.size(0)
#
#                 # 总损失
#                 loss_mean_val += loss_val.item()
#
#             # 查看整个验证集的准确率
#             acc_val = correct_val / total_val
#
#             # 计算 验证集的平均损失
#             loss_mean_val = loss_mean_val / len(valid_loader)
#
#             print('第 %d 轮，在验证集上的准确率为：%f , 平均损失为：%f ' % (epoch + 1, acc_val, loss_mean_val))
#             print('*' * 200)
#
#             # 保存模型
#             # 参数1：网络状态字典
#             # 参数2：路径+名称
#             torch.save(net.state_dict(), 'model.pth')

# ===============================测试、验证部分==========================================================================
# 加载模型  --->测试
# 加载模型
checkpoint = torch.load('./model.pth')
# 从checkpoint 加载网络参数
net.load_state_dict(checkpoint)

# 准备测试数据
test_data = RMBDataSet(data_dir='./dataset/rmb_split/test', transform=transform)

# 准备test_loader
test_loader = DataLoader(
    dataset=test_data,
    batch_size=1
)

# 预测
with torch.no_grad():
    # 加载数据
    for i, data in enumerate(test_loader):
        # i : 测试数据的下标
        # data
        img_test, label_test, img_path_test = data
        # 正向传播
        output = net(img_test)
        # 获取预测类别
        _, pre = torch.max(output.data, 1)

        # print('pre:', pre)
        print('img_path_test:', img_path_test)

        # # 通过预测值来判定是1元还是100元
        rmb = 1 if pre.numpy()[0] == 0 else 100

        print('模型的预测值为：%d 元' % rmb)

        # 利用opencv 去读取图像数据
        # 安装： 先进入虚拟环境 --- pip install opencv-python

        # # 读取图像数据
        img = cv2.imread(img_path_test[0])

        # 缩放图片
        img = cv2.resize(img, (400, 200))

        # 设置该图片的名称
        # print('该图片的名称为：', img_path_test[0].split('/')[-1])

        # 构建要显示的数据
        res = '{0} ----is {1} yuan'.format(str(img_path_test[0].split('/')[-1]), str(rmb))

        # 显示图片
        cv2.imshow(res, img)

        # 设置为0，不会闪退，等待输入任意值
        cv2.waitKey(0)
        # 释放内存
        cv2.destroyWindow(res)
