import pandas as pd
import jieba
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.naive_bayes import MultinomialNB  # 多项式朴素贝叶斯


def load_data():
    """
    数据加载
    :return:data
    """
    data = pd.read_csv('./data/data.csv', encoding='ansi')
    print('data:\n', data)
    print('data:\n', data.columns)

    return data


def deal_data(data):
    """
    数据处理
    :param data: 原始数据
    :return:train,test
    """
    # 将文本数据转化为数值特征
    x = data.loc[:, '内容 ']
    # 构建一个列表，存储分词之后数据
    seg_list = []
    # 1、分词
    for tmp in x:
        print('tmp:', tmp)  # 各篇文本
        # 对文本进行分词---精确分词
        seg = jieba.cut(tmp, cut_all=False)
        # 拼接合并
        seg_str = ','.join(seg)
        print('seg_str:', seg_str)
        print('*' * 100)
        # 加入
        seg_list.append(seg_str)
    # seg_list ---分词之后的特征值
    print('seg_list:\n', seg_list)

    # 2、加载处理停止词
    with open('./data/stopwords.txt', 'r', encoding='utf-8') as fp:
        st_words = fp.readlines()
        print('st_words:\n', st_words)
        # 剔除st_words两侧空白字符
        st_words = [tmp.strip() for tmp in st_words]
        # 去重
        st_words = list(set(st_words))

    print('st_words:\n', st_words)
    # 将  '一本', '一遍', '三个' ---加入停止词
    st_words.extend(['一本', '一遍', '三个'])

    # 3、统计词数
    # (1)实例化对象
    con_vet = CountVectorizer(stop_words=st_words)
    # （2）统计词数
    x = con_vet.fit_transform(seg_list).toarray()
    # 统计的词语
    words = con_vet.get_feature_names()
    print('words:\n', words)
    print('x:\n', x)
    print('x:\n', x.dtype)

    # 4、目标值---数值类型
    # 好评为1  差评为0
    data.loc[data.loc[:, '评价'] == '好评', '评价'] = 1
    data.loc[data.loc[:, '评价'] == '差评', '评价'] = 0
    # print('data:\n', data)
    # print('data:\n', data.dtypes)

    # 获取目标值 并将类型修改Wie int64
    y = data.loc[:, '评价'].astype(np.int64).values.reshape((-1, 1))
    print('y:\n', y)
    print('y:\n', y.dtype)
    print('*' * 100)

    # 合并特征值 和目标值
    data = np.concatenate((x, y), axis=1)
    print('data:\n', data)

    # 5、数据集拆分
    # 拆分为训练集、测试集
    train = data[:10, :]
    test = data[10:, :]

    return train, test


def main():
    """
    主函数
    :return:
    """
    # 1、加载数据
    data = load_data()

    # 2、数据处理
    train, test = deal_data(data)

    # 3、构建模型进行预测
    # (1)实例化算法对象
    # alpha ——————>拉普拉斯平滑系数
    nb = MultinomialNB(alpha=1)
    # (2)训练数据并构建模型
    nb.fit(train[:, :-1], train[:, -1])
    # (3)预测
    y_pre = nb.predict(test[:, :-1])
    print('预测值：\n', y_pre)
    # 获取准确率
    score = nb.score(test[:, :-1], test[:, -1])
    print('准确率为：\n', score)

if __name__ == '__main__':
    main()
