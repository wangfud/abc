from torch.utils.data import Dataset
import os
from PIL import Image

rmb_label = {'1': 0, '100': 1}


class RMBDataSet(Dataset):
    """
    用来读取数据的类
    """

    def __init__(self, data_dir, transform=None):
        self.data_info = self.get_img_info(data_dir)
        self.transform = transform  # 数据处理方式

    def __getitem__(self, index):
        """
        根据索引来获取具体的一个样本数据
        :param index: 图片数据的索引
        :return:
        """
        # 获取数据
        img_path, label = self.data_info[index]

        # 读img_path路径所对应的图片数据
        img = Image.open(img_path).convert('RGB')
        # print('img:\n', img)
        # 如果传入 数据处理对象
        if self.transform is not None:
            # 需要对图片数据进行数据处理
            img = self.transform(img)

        return img, label, img_path

    @staticmethod
    def get_img_info(data_dir):
        """
        获取指定的data_dir中图片数据
        :param data_dir: 指定的路径
        :return:
        """
        # 构建一个list来存储指定 data_dir中所有的图片信息
        data_info = []
        # 遍历 data_dir
        for tmp in os.listdir(data_dir):
            # print('tmp:', tmp)  # 1 或者 100
            # 获取所有的图片文件名称
            imgs_path = data_dir + '/' + tmp
            # print('imgs_path:', imgs_path)
            # 获取所有的图片名称
            img_names = os.listdir(imgs_path)
            # 遍历
            for i in range(len(img_names)):
                # i --->图片的下标
                # 获取第i个图片名称
                img_name = img_names[i]
                # 拼接第i个图片的路径 + 名称
                img_path = imgs_path + '/' + img_name
                # print('图片的路径+ 名称：', img_path)

                # 获取第i个图片的目标值
                label = rmb_label[tmp]
                # 将 路径+图片名称 和目标值 组成一个元组
                data_info.append((img_path, label))

        # print('data_info:\n', data_info)

        return data_info

    def __len__(self):

        return len(self.data_info)

# 验证get_img_info
# if __name__ == '__main__':
#     get_img_info('./dataset/rmb_split/train')

# 验证 RMBDataSet
# 实例化对象
# train_dataset = RMBDataSet('./dataset/rmb_split/train')
# # 调用__getitem__方法
# img, label, img_path = train_dataset.__getitem__(0)
# print('img:\n', img)
# print('label:\n', label)
# print('img_path:\n', img_path)
