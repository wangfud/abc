import random
import os
import shutil


# 完成数据集拆分

def split_rmb_data():
    """
    对RMB数据进行拆分，拆分为训练集、验证集、测试集
    训练集:验证集:测试集 = 8:1:1
    训练集---训练数据
    验证集---每训练一轮，在验证集验证一下训练效果
    测试集---测试保存的模型的好坏
    :return: None
    """
    # 加入随机种子
    random.seed(1)

    # 确定原始主路径
    original_dir = './dataset/RMB_data/'
    # 确定拆分主路径
    split_dir = './dataset/rmb_split/'

    # 确定拆分之后训练集、验证集、测试集的具体的路径
    train_dir = os.path.join(split_dir, 'train')
    valid_dir = os.path.join(split_dir, 'valid')
    test_dir = os.path.join(split_dir, 'test')

    # 确定 训练集、验证集、测试集 的占比
    train_pct = 0.8
    valid_pct = 0.1
    # 剩下的就是测试集的占比

    # 循环遍历原始路径
    for root in os.listdir(original_dir):
        # print('root:', root)  # 1 或者 100
        # 构建图片数据的路径
        imgs_dir = os.path.join(original_dir, root)
        # print('imgs_dir:', imgs_dir)

        # 获取图片数据路径中 所有图片的名称
        img_names = os.listdir(imgs_dir)
        # print('img_names:\n', img_names)
        # print('*' * 100)

        # 筛选过滤 ---筛选文件名称中所有以.jpg为结尾的文件---图片数据文件
        img_names = list(filter(lambda x: x.endswith('.jpg'), img_names))
        # img_names ---->图片数据文件名称列表

        # 打乱图片名称顺序
        random.shuffle(img_names)

        # 该子集中的图片的数量
        all_img_counts = len(img_names)

        # 确定训练集的样本个数
        train_point = int(all_img_counts * train_pct)
        # 确定验证集的样本个数
        valid_point = int(all_img_counts * valid_pct)
        # 剩下的 样本数量 ---->测试集的样本数量
        for i in range(all_img_counts):
            # 在循环内部，判断哪个图片是训练集、哪些图片是验证集、哪些图片是测试集
            # 取前 80% 为训练集
            # 取接下来的10%为验证集
            # 取剩下的10%为测试集
            # i --->图片数据的下标
            if i < train_point:
                out_dir = os.path.join(train_dir, root)
            elif i < (train_point + valid_point):
                out_dir = os.path.join(valid_dir, root)
            else:
                out_dir = os.path.join(test_dir, root)

            # 创建对应的数据子集文件夹
            # 如果对应的文件夹不存在，创建文件夹，如果存在，啥事都不干
            if not os.path.exists(out_dir):
                os.makedirs(out_dir)

            # 将 第i个图片 从原始路径 复制到 拆分文件夹中的各个子集中
            # 确定原始文件
            src_img_name = os.path.join(original_dir, root, img_names[i])

            # 确定目标文件
            target_img_name = os.path.join(out_dir, img_names[i])

            # 复制
            shutil.copy(src_img_name, target_img_name)


if __name__ == '__main__':
    split_rmb_data()
