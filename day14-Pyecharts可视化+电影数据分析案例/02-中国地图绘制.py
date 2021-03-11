import pandas as pd
from pyecharts.charts import Map
from pyecharts import options as opts

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
# 5、生成图像
map_china.render('./html/中国地图.html')
