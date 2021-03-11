# 导入流向地图绘制
from pyecharts.charts import Geo
# 导入配置模块
import pyecharts.options as opts

# 1、实例化对象
geo = Geo(
    # 初始化设置
    init_opts=opts.InitOpts(
        #
        width='100%',
        height='900px',
        theme='chalk',  # 主题
        page_title='流向地图',  # 网页名称
    )
)

# 2、添加数据
# 添加类型
geo.add_schema(
    maptype='湖北',  # 地图类型，如果为中国地图--china,  世界---world
    is_roam=True,  # 开启缩放
    # 地图样式
    itemstyle_opts=opts.ItemStyleOpts(
        border_color='#228B22',  # 地图边缘颜色
        area_color='#FF8C00',  # 地图区域颜色
    )

)

# 准备数据
# 构建武汉封城前的出入数据 （湖北省内数据）
# 出--代表从武汉--->该城市
# 入--代表从该城市--->武汉
data_0120_ru = '孝感、黄冈、鄂州、荆州、黄石、襄阳'
data_0120_chu = '孝感、黄冈、荆州、襄阳、黄石、荆门、鄂州、随州、仙桃'
data_0121_ru = '孝感、黄冈、荆州、鄂州、黄石'
data_0121_chu = '孝感、黄冈、荆州、襄阳、荆门、黄石、随州、鄂州、仙桃'
data_0122_ru = '孝感、黄冈、鄂州、荆州、咸宁、黄石'
data_0122_chu = '孝感、黄冈、荆州、襄阳、荆州、随州、宜昌、黄石、鄂州'

# data_pair = [(出,入),(出,入),....]  格式
# 入武汉： [('孝感','武汉'),('黄冈','武汉'),...]
# 出武汉： [('武汉','孝感'),('武汉','黄冈')]
#
data_ru = []
# 处理入武汉
for city_str in (data_0120_ru, data_0121_ru, data_0122_ru):
    # print('city_str:', city_str)  #
    # 对每一个 city_str 再进行处理
    city_list = city_str.split('、')
    # 构建迁徙路线
    for city in city_list:
        data_ru.append((city, '武汉'))

# print('data_ru:\n', data_ru)

#
data_chu = []

for city_str in (data_0120_chu, data_0121_chu, data_0122_chu):
    # print('city_str:', city_str)  #
    # 对每一个 city_str 再进行处理
    city_list = city_str.split('、')
    # 构建迁徙路线
    for city in city_list:
        data_chu.append(('武汉', city))

# print('data_chu:\n', data_chu)

# 组合路线
data_pair_city = data_ru + data_chu

# print('data_pair_city:\n', data_pair_city)
# print('data_pair_city:\n', len(data_pair_city))

#  对 data_pair_city  去重
data_pair_city = list(set(data_pair_city))
print('data_pair_city:\n', data_pair_city)
print('data_pair_city:\n', len(data_pair_city))

# 添加数据
geo.add(
    series_name='',  # 系列名称
    data_pair=data_pair_city,  # 数据项 ----[(k,v),(k,v),....]
    # 迁徙路线的类型
    type_='lines',
    # type_='effectScatter',
    # 涟漪特效
    effect_opts=opts.EffectOpts(
        is_show=True,  # 显示特效
        brush_type='stroke',  # 波纹的绘制方式
        # brush_type='Scatter',  # 波纹的绘制方式
        color='#FFD700',  # 特效颜色
        symbol='arrow',  # 箭头 ---特效图形
        # symbol='pin',  # 圆圈 ---特效图形
        symbol_size=10,  # 特效标记的大小
        # period=4,
        # scale=5,
    ),
    # 线的样式
    linestyle_opts=opts.LineStyleOpts(
        # 线的弯曲程度
        curve=0.3,
        # 线的类型
        type_='dashed',
        # 线的颜色
        color='#A52A2A'
    )

)

# 3、全局配置
geo.set_global_opts(
    # 标题
    title_opts=opts.TitleOpts(
        title='武汉封城前流向地图',
        # subtitle='广州Python0624全体',
        pos_left='center',
        pos_top='5%',
        title_textstyle_opts=opts.TextStyleOpts(
            font_size=40
        )
    ),
    # 图例
    legend_opts=opts.LegendOpts(
        is_show=False
    ),
    # 文本设置 ---借助原生组件元素设置
    graphic_opts=opts.GraphicGroup(
        # 控制文本相对于整体的位置
        graphic_item=opts.GraphicItem(
            #
            left='75%',
            top='5%'
        ),
        # 设置文本
        children=[
            # # 设置文本框
            # opts.GraphicRect(
            #
            # ),
            # 设置文本
            opts.GraphicText(
                # 配置的文本相对于 --->文本框的位置
                graphic_item=opts.GraphicItem(
                    left='center',  # 文本相对于文本框的左位置
                    top='middle',  # 文本相对文本框的上位置
                    z=100,  # 字在文本框的z轴方向100的位置
                    scale=[2.5, 2.5],  # [横向缩放的倍数, 纵向缩放的倍数]
                ),
                # 设置文本内容
                graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                    # 文本内容
                    text="""截止2020-01-22日\n武汉封城前的迁徙路线""",
                    font='13px Microsoft YaHei',  # 字体
                    text_align='left',  # 水平对其方式： 左对齐
                    text_vertical_align='middle',  # 垂直对其方式：居中
                    # 图形化基本设置
                    graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                        fill='#ffdf22'  # 设置颜色
                    )
                )
            )
        ]
    )

)

# 4、系列配置
geo.set_series_opts(
    # 标签设置
    label_opts=opts.LabelOpts(
        is_show=False
    )
)

# 5、生成图像
geo.render('./html/流向地图.html')
