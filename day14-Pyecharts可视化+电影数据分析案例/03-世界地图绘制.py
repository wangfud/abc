import pandas as pd
from pyecharts.charts import Map, Page
from pyecharts import options as opts
# 导入翻译模块

from translate import Translator

# ========================================================================================================================中国地图绘制 ================================================
# 加载数据
data = pd.read_excel('./data/截至2月17日22时37分疫情数据.xls')
# print('data:\n', data)
# print('data:\n', data.columns)

# 获取中国各个省的数据
# 构建bool数组
mask = data.loc[:, '城市'] == data.loc[:, '省份']
# 筛选数据
data = data.loc[mask, ['省份', '确诊数']]
print('data:\n', data)

# 准备data_pair
data_pair = [(k, v) for k, v in zip(data.loc[:, '省份'].tolist(), data.loc[:, '确诊数'].tolist())]

print('data_pair:\n', data_pair)
# 绘制中国地图
# 1、实例化对象
map_china = Map(
    # 初始化配置
    init_opts=opts.InitOpts(
        #
        width='800px',
        height='500px',
        theme='chalk',
        page_title='中国地图',
    )
)

# 2、添加数据
map_china.add(
    series_name='截至2月17日22时37分疫情数据',
    data_pair=data_pair,  # [(k,v),(k,v),....]
    maptype='china',  # 地图类型
    is_map_symbol_show=False
)

# 3、全局配置
map_china.set_global_opts(
    # 标题
    title_opts=opts.TitleOpts(
        title='2020年中国疫情数据',
        subtitle='广州Python0624全体',
        pos_top='3%',
        pos_left='5%'
    ),
    # 图例
    legend_opts=opts.LegendOpts(
        is_show=True,
        pos_top='3%',
        pos_left='center'
    ),
    # 视觉映射配置项
    visualmap_opts=opts.VisualMapOpts(
        is_show=True,  # 显示视觉映射配置
        type_='color',  # 类型，使用颜色来区分不同的值
        min_=0,
        max_=60000,
        is_piecewise=True,  # 分段型
        pieces=[
            {"min": 10001, "label": ">10000", "color": "#4b0101"},
            {"max": 10000, "min": 5001, "label": ">5000", "color": "#4a0100"},
            {"max": 5000, "min": 1001, "label": ">1000", "color": "#8A0808"},
            {"max": 1000, "min": 500, "label": "500-1000", "color": "#B40404"},
            {"max": 499, "min": 100, "label": "100-499", "color": "#DF0101"},
            {"max": 99, "min": 10, "label": '10-99', "color": "#F78181"},
            {"max": 9, "min": 1, "label": "1-9", "color": "#F5A9A9"},
            {"max": 0, "min": 0, "label": "0", "color": "#FFFFFF"},
        ],
        # 映射标签的字体设置
        textstyle_opts=opts.TextStyleOpts(
            color='white'
        )
    )
)

# 4、系列配置
map_china.set_series_opts(
    # 标签
    label_opts=opts.LabelOpts(
        is_show=True
    )
)

# ==========================================================================================================================世界地图绘制=====================================
# # 加载数据
# data = pd.read_excel('./data/截至2月17日22时37分疫情数据.xls')
# # print('data:\n', data)
#
# # 获取各个国家的数据
# # 构建bool数组
# mask = data.loc[:, '省份'].str.contains('洲')
# # 筛选数据
# data = data.loc[mask, ['城市', '确诊数']]
#
#
# # print('data:\n', data)
#
#
# # 需要安装翻译模块 translate 模块
# # pip install translate
# def translate_countryname_to_english(country_name):
#     """
#     翻译国家名称
#     :param country_name: 中文国家名称
#     :return: 英文国家名称
#     """
#     # 1、实例化对象
#     translator = Translator(from_lang='chinese', to_lang='english')
#     # 2、进行翻译
#     english_country_name = translator.translate(country_name)
#
#     return english_country_name
#
#
# # # 需要对国家名称进行翻译
# data.loc[:, '城市'] = data.loc[:, '城市'].transform(translate_countryname_to_english)
# print('data:\n', data)
#
# # 准备data_pair
# data_pair = [(k, v) for k, v in zip(data.loc[:, '城市'].tolist(), data.loc[:, '确诊数'].tolist())]
#

data_pair = [('China', 70642), ('Singapore', 77), ('Japan', 519), ('South Korea', 30), ('Thailand', 35),
             ('Malaysia', 22), ('Germany', 16), ('US', 15), ('Vietnam', 16), ('France', 12), ('Canada', 8),
             ('Australia', 15), ('United Arab Emirates', 9), ('Italy', 3), ('Spain', 2), ('Nepal', 1), ('Sri Lanka', 1),
             ('UK', 9), ('Swedish', 1), ('Philippines', 3), ('Egypt', 1), ('Cambodia', 1), ('Finland', 1), ('India', 3),
             ('Russia', 2), ('Belgium', 1)]
print('data_pair:\n', data_pair)

# 1、实例化对象
map_world = Map(
    # 初始化配置
    init_opts=opts.InitOpts(
        #
        width='800px',
        height='500px',
        theme='chalk',
        page_title='世界地图',
    )
)

# 2、添加数据
map_world.add(
    series_name='截至2月17日22时37分疫情数据',
    data_pair=data_pair,
    maptype='world',
    is_map_symbol_show=False
)

# 3、全局配置
map_world.set_global_opts(
    # 标题
    title_opts=opts.TitleOpts(
        title='2020年世界疫情数据',
        subtitle='广州Python0624全体',
        pos_top='3%',
        pos_left='5%'
    ),
    # 图例
    legend_opts=opts.LegendOpts(
        is_show=True,
        pos_top='3%',
        pos_left='center'
    ),
    # 视觉映射配置项
    visualmap_opts=opts.VisualMapOpts(
        is_show=True,  # 显示视觉映射配置
        type_='color',  # 类型，使用颜色来区分不同的值
        min_=0,
        max_=60000,
        is_piecewise=True,  # 分段型
        pieces=[
            {"min": 9999, "label": ">9999", "color": "#4b0101"},
            {"max": 9998, "min": 100, "label": "100-9998", "color": "#4a0100"},
            {"max": 99, "min": 40, "label": "40-99", "color": "#8A0808"},
            {"max": 39, "min": 30, "label": "30-39", "color": "#B40404"},
            {"max": 29, "min": 20, "label": "20-29", "color": "#DF0101"},
            {"max": 19, "min": 10, "label": '10-19', "color": "#F78181"},
            {"max": 9, "min": 1, "label": "1-9", "color": "#F5A9A9"},
            {"max": 0, "min": 0, "label": "0", "color": "#FFFFFF"},
        ],
        # 映射标签的字体设置
        textstyle_opts=opts.TextStyleOpts(
            color='white'
        )
    )
)

# 4、系列配置
map_world.set_series_opts(
    # 标签
    label_opts=opts.LabelOpts(
        is_show=False
    )
)

# 5、生成图像
# map_world.render('./html/世界地图.html')

# ======================================================================================================================组合中国地图、世界地图 =============================================

# 顺序多图 ---Page
# 1、实例化 Page 对象
page = Page(
    page_title='组合中国地图、世界地图',
    interval=1,
    layout=Page.DraggablePageLayout  # 布局
)
# 2、添加数据
page.add(map_china)
page.add(map_world)

# 3、生成图像
page.render('./html/组合中国地图、世界地图.html')
