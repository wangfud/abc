# 词云： wordcloud
# 安装：pip install wordcloud

import jieba
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def wc_generator():
    """
    词云文本生成
    :return:
    """
    # 1、加载文本
    with open('./data/元尊.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        # print('content:\n', content)

    # 2、分词
    seg = jieba.cut(content, cut_all=False)
    # 拼接为字符串
    seg_str = ','.join(seg)
    print('seg_str:\n', seg_str)

    # 3、加载并处理停止词
    with open('./data/stopwords.txt', 'r', encoding='utf-8') as p:
        st_list = p.readlines()

        # 剔除停止词两侧空白字符
        st_list = [tmp.strip() for tmp in st_list]

        # 去重
        st_list = list(set(st_list))

        print('st_list:\n', st_list)

    # 停止词添加
    # st_list.append('法域')

    # 4、生成词云对象
    wc = WordCloud(
        font_path='./data/simhei.ttf',  # 字体路径
        width=400,  # 宽
        height=200,  # 高
        background_color='white',  # 背景颜色
        stopwords=st_list,  # 停止词
    )

    # 5、生成词云文本
    wc_text = wc.generate(seg_str)

    # 6、展示
    # 展示样式
    #  interpolation='bilinear' ---展示为线性，横平竖直的样式
    plt.imshow(wc_text, interpolation='bilinear')

    # 关闭坐标轴
    plt.axis('off')

    # 展示图片
    plt.show()


def wc_generator_img():
    """
    词云文本生成
    :return:
    """
    # 1、加载文本
    with open('./data/元尊.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        # print('content:\n', content)

    # 2、分词
    seg = jieba.cut(content, cut_all=False)
    # 拼接为字符串
    seg_str = ','.join(seg)
    print('seg_str:\n', seg_str)

    # 3、加载并处理停止词
    with open('./data/stopwords.txt', 'r', encoding='utf-8') as p:
        st_list = p.readlines()

        # 剔除停止词两侧空白字符
        st_list = [tmp.strip() for tmp in st_list]

        # 去重
        st_list = list(set(st_list))

        print('st_list:\n', st_list)

    # 4、加载图片数据
    # 图片：像素值
    # 如果为黑白图片 ---灰度图 --->[0,255]之间的值
    img = np.array(Image.open('./data/girl.jpg'))
    print('img:\n', img)

    # 停止词添加
    # st_list.append('法域')

    # 5、生成词云对象
    wc = WordCloud(
        font_path='./data/simhei.ttf',  # 字体路径
        # width=400,  # 宽
        # height=200,  # 高
        background_color='white',  # 背景颜色
        stopwords=st_list,  # 停止词
        mask=img,  # 可以自定义图片
    )

    # 6、生成词云文本
    wc_text = wc.generate(seg_str)

    # 7、提取背景图片的颜色
    color = ImageColorGenerator(image=img)

    # 8、重设词云文本的颜色
    wc_text.recolor(color_func=color)

    # 9、展示
    # 展示样式
    #  interpolation='bilinear' ---展示为线性，横平竖直的样式
    plt.imshow(wc_text, interpolation='bilinear')

    # 关闭坐标轴
    plt.axis('off')

    # 展示图片
    plt.show()


# wc_generator()
# wc_generator_img()
