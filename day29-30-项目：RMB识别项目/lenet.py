import torch.nn as nn
import torch.nn.functional as F


class LeNet(nn.Module):
    """
    自定义卷积神经网络
    """

    def __init__(self, classes):
        """
        确定网络的各个层次结构
        :param classes: 分类的类别数目
        """
        # 使用父类来初始化网络结构
        super(LeNet, self).__init__()

        # 搭建网络结构
        # 设计2个卷积、激活、池化 + 3个fc
        # 第一个卷积、激活、池化
        # in_channels 指定输入的通道数---->3通道 ---也同样表示卷积核也为3通道
        # out_channels 指定卷积之后输出的通道数，与卷积核的个数相等 ---表示的卷积核的个数
        # kernel_size 指定卷积核的尺寸大小
        # stride 指定卷积步长
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=6, kernel_size=5, stride=1)
        # 卷积之后 输出结果为 : 28*28*6
        # 激活之后的结果为：28*28*6
        # 池化之后的结果为：池化区域为：2*2， 池化步长为2 --->14*14*6

        # 第二个卷积、激活、池化
        #
        self.conv2 = nn.Conv2d(in_channels=6, out_channels=16, kernel_size=5, stride=1)
        # 卷积之后的结果为：10*10*16
        # 激活之后的结果为：10*10*16
        # 池化之后的结果为：池化区域为：2*2， 池化步长为2 --->5*5*16

        # 第一个fc层
        # in_features 指定输入的特征的数目
        # out_features 指定输出的特征的数目
        self.fc1 = nn.Linear(in_features=5 * 5 * 16, out_features=120)

        # 第二个fc层
        self.fc2 = nn.Linear(in_features=120, out_features=84)

        # 第三个fc层 即 输出层
        self.fc3 = nn.Linear(in_features=84, out_features=classes)

    def forward(self, x):
        """
        正向传播
        :param x: 一个批次的图片特征数据
        :return: 对应的预测值
        """
        # 第一个卷积、激活、池化计算
        out = self.conv1(x)
        # 激活
        out = F.relu(out)
        # 池化
        # input --输入数据
        # kernel_size ---表示池化大小
        # stride ---池化步长
        out = F.max_pool2d(input=out, kernel_size=2, stride=2)
        # batchsize*6*14*14  --->4d张量 --->(批次数量，通道，高，宽)

        # 第二个卷积、激活、池化计算
        out = self.conv2(out)
        # 激活
        out = F.relu(out)
        # 池化
        out = F.max_pool2d(input=out, kernel_size=2, stride=2)
        # batchsize*16*5*5

        # 需要将out展开
        # out ---size  ---(batchsize,16,5,5)
        # 将out 输入到fc --out --batchsize个样本
        out = out.view((out.size(0), -1))

        # 将展开之后的out输入到第一个fc中
        # 第一个fc的线性变换
        out = self.fc1(out)
        # 非线性变换
        out = F.relu(out)

        # 第二个fc
        # 第二个fc的线性变换
        out = self.fc2(out)
        # 非线性变换
        out = F.relu(out)

        # 第三个fc
        # 第三个fc的线性变换
        out = self.fc3(out)
        # 非线性变换
        out = F.softmax(out, dim=1)

        return out

    def initialize_weight(self):
        """
        初始化卷积神经网络参数
        :return: None
        """
        # 遍历神经网络中的参数
        for m in self.modules():
            # m 为卷积神经网络中的参数
            #
            if isinstance(m, nn.Conv2d):
                # 此时，如果满足判断，那么m为卷积参数
                # 卷积参数： 卷积权重 + 卷积偏置
                # 如果为卷积权重 ---正态分布初始化
                nn.init.xavier_normal_(m.weight.data)
                # 如果偏置不为None，0初始化
                if m.bias is not None:
                    m.bias.data.zero_()
            elif isinstance(m, nn.Linear):
                # 此时，如果满足判断，那么m为fc层参数
                nn.init.normal_(m.weight.data, mean=0, std=0.1)
                m.bias.data.zero_()
