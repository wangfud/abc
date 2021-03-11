import pandas as pd
# 导包 --绘图模块
from pyecharts.charts import *
# 配置模块
from pyecharts import options as opts

# 加载数据
history_data = pd.read_excel('./data/疫情历史数据.xls', sheet_name=0, index_col=0)
print('history_data:\n', history_data)
print('history_data:\n', history_data.dtypes)
print('*' * 100)

# 准备数据
# 准备横轴
# (1)获取时间并转化为字符串
x_data = history_data.loc[:, '时间'].astype('str')
# (2) 转换顺序，并转化为list
x_data = x_data[::-1].tolist()
print('x_data:\n', x_data)

# 准备纵轴数据
# 准备死亡数据
death_data = history_data.loc[:, '死亡数'][::-1].tolist()
print('死亡数据：\n', death_data)
# 准备确诊数据
ensure_data = history_data.loc[:, '确诊数'][::-1].tolist()
print('确诊数据：\n', ensure_data)
# 准备疑似数据
suspected_data = history_data.loc[:, '疑似数'][::-1].tolist()
print('疑似数据：\n', suspected_data)
# 准备治愈数据
cure_data = history_data.loc[:, '治愈数'][::-1].tolist()
print('治愈数据：\n', cure_data)

# 开始绘图
# 柱状图绘制
# 1、实例化对象
bar = Bar(
    # # 初始化配置
    # init_opts=opts.InitOpts(
    #     theme='dark',  # 主题风格，
    #     page_title='柱状图、折线图组合',
    #     width='100%'
    # )
)
# 2、添加数据
# 添加横轴数据
bar.add_xaxis(
    xaxis_data=x_data,  # 横轴数据
)
# 添加纵轴数据
bar.add_yaxis(
    series_name='死亡数',  # 系列名称
    yaxis_data=death_data,  # 数据
    yaxis_index=1
)

# 添加纵轴数据
bar.add_yaxis(
    series_name='治愈数',  # 系列名称
    yaxis_data=cure_data,  # 数据
    yaxis_index=2
)

# 拓展坐标轴
bar.extend_axis(
    # 添加纵轴 ---死亡数的纵轴
    yaxis=opts.AxisOpts(
        type_='value',  # 数值轴
        name='死亡数',  # 坐标轴名称
        min_=0,  # 坐标轴的最小值
        max_=1300,  # 坐标轴的最大值
        position='right',  # 死亡数的坐标轴在整个X轴的右边
        offset=0,  # 坐标轴偏移量
        # 设置坐标线
        axisline_opts=opts.AxisLineOpts(
            is_show=True,  # 显示坐标线
            # 设置坐标线的风格
            linestyle_opts=opts.LineStyleOpts(
                color='#FDF5E6',  # 坐标线颜色
            )
        ),
        # 设置坐标轴的标签
        axislabel_opts=opts.LabelOpts(
            is_show=True,  # 显示标签
            position='top',  # 标签位置
            formatter='{value}',  # 轴上的数值显示
        )
    )
)

# 添加纵轴 ---治愈数的纵轴
bar.extend_axis(
    # 添加纵轴 ---治愈数的纵轴
    yaxis=opts.AxisOpts(
        type_='value',  # 数值轴
        name='治愈数',  # 坐标轴名称
        min_=0,  # 坐标轴的最小值
        max_=1300,  # 坐标轴的最大值
        position='right',  # 死亡数的坐标轴在整个X轴的右边
        offset=90,  # 坐标轴偏移量
        # 设置坐标线
        axisline_opts=opts.AxisLineOpts(
            is_show=True,  # 显示坐标线
            # 设置坐标线的风格
            linestyle_opts=opts.LineStyleOpts(
                color='#FDF5E6',  # 坐标线颜色
            )
        ),
        # 设置坐标轴的标签
        axislabel_opts=opts.LabelOpts(
            is_show=True,  # 显示标签
            position='top',  # 标签位置
            formatter='{value}',  # 轴上的数值显示
        )
    )
)

bar.extend_axis(
    # 添加纵轴 ---疑似数的纵轴
    yaxis=opts.AxisOpts(
        type_='value',  # 数值轴
        name='疑似数',  # 坐标轴名称
        min_=0,  # 坐标轴的最小值
        max_=30000,  # 坐标轴的最大值
        position='right',  # 死亡数的坐标轴在整个X轴的右边
        offset=180,  # 坐标轴偏移量
        # 设置坐标线
        axisline_opts=opts.AxisLineOpts(
            is_show=True,  # 显示坐标线
            # 设置坐标线的风格
            linestyle_opts=opts.LineStyleOpts(
                color='#FDF5E6',  # 坐标线颜色
            )
        ),
        # 设置坐标轴的标签
        axislabel_opts=opts.LabelOpts(
            is_show=True,  # 显示标签
            position='top',  # 标签位置
            formatter='{value}',  # 轴上的数值显示
        )
    )
)
# 折线图绘制
# 1、实例化对象
line = Line()
# 2、添加数据
# 添加横轴数据
line.add_xaxis(
    xaxis_data=x_data  # 横轴数据
)
# 添加纵轴数据
line.add_yaxis(
    series_name='确诊数',  # 系列名称
    y_axis=ensure_data,  # 数据
    yaxis_index=0
)
# 添加纵轴数据
line.add_yaxis(
    series_name='疑似数',  # 系列名称
    y_axis=suspected_data,  # 数据
    yaxis_index=3
)

# 3、全局配置
bar.set_global_opts(
    # 标题配置
    title_opts=opts.TitleOpts(
        title='中国疫情数据',  # 主标题
        subtitle='广州0624Python全体',  # 子标题
        pos_left='1%',  # 标题的左位置
        pos_top='3%',  # 标题的上位置
        # 设置主标题样式
        title_textstyle_opts=opts.TextStyleOpts(
            font_style='normal',  # 字体风格
            font_weight='normal',  # 字体的粗细
            color='#FDF5E6',  # 字体颜色
            font_size=25,  # 字体大小
        ),
        # 设置子标题样式
        subtitle_textstyle_opts=opts.TextStyleOpts(
            font_style='normal',  # 字体风格
            font_weight='normal',  # 字体的粗细
            color='#FDF5E6',  # 字体颜色
            font_size=20,  # 字体大小
        )
    ),
    # 图例设置
    legend_opts=opts.LegendOpts(
        type_='plain',  # 图例类型 ，plain---普通类型
        is_show=True,  # 显示图例
        pos_left='25%',
        pos_top='5%',
        # # 字体样式  --不设置
        # textstyle_opts=opts.TextStyleOpts(
        #
        # )
    ),
    # 设置纵轴 ---默认的纵轴
    yaxis_opts=opts.AxisOpts(
        type_='value',  # 数值轴
        name='确诊数',  # 坐标轴名称
        min_=0,  # 坐标轴的最小值
        max_=30000,  # 坐标轴的最大值
        position='left',  # 死亡数的坐标轴在整个X轴的左边
        offset=0,  # 坐标轴偏移量
        # 设置坐标线
        axisline_opts=opts.AxisLineOpts(
            is_show=True,  # 显示坐标线
            # 设置坐标线的风格
            linestyle_opts=opts.LineStyleOpts(
                color='#FDF5E6',  # 坐标线颜色
            )
        ),
        # 设置坐标轴的标签
        axislabel_opts=opts.LabelOpts(
            is_show=True,  # 显示标签
            position='top',  # 标签位置
            formatter='{value}',  # 轴上的数值显示
        )
    ),
    # 设置提示框的类型
    tooltip_opts=opts.TooltipOpts(
        trigger='axis',  # 进入坐标轴，就触发提示框
        trigger_on='mousemove|click',  # 点击或者鼠标移动都触发提示
        axis_pointer_type='cross',  # 指示器类型， cross ---十字准星
    ),
    # 文本设置 ---借助原生组件元素设置
    graphic_opts=opts.GraphicGroup(
        # 控制文本相对于整体的位置
        graphic_item=opts.GraphicItem(
            #
            left='80%',
            top='45%'
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
                    scale=[1.3, 1.5],  # [横向缩放的倍数, 纵向缩放的倍数]
                ),
                # 设置文本内容
                graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                    # 文本内容
                    text="""直到{}，\n全国的新冠状病毒的相关信息为：\n死亡数例数为{}列\n治愈数例数为{}例\n疑似数例数为{}例\n确诊数例数为{}例""".format(
                        history_data.loc[0, '时间'], history_data.loc[0, '死亡数'], history_data.loc[0, '治愈数'],
                        history_data.loc[0, '疑似数'], history_data.loc[0, '确诊数']
                    ),
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

# 给line增加系列配置
line.set_series_opts(
    #
    label_opts=opts.LabelOpts(
        is_show=False
    )
)

# 层叠
all_chart = bar.overlap(line)

# 组合柱状图、折线图
# 并行多图
grid = Grid(
    # 初始化设置
    init_opts=opts.InitOpts(
        width='100%',
        height='600px',
        theme='purple-passion',
        page_title='柱状图、折线图组合绘制'
    )
)

grid.add(
    chart=all_chart,  # 子图表
    is_control_axis_index=True,  # grid控制索引
    grid_index=0,  # 索引
    grid_opts=opts.GridOpts(
        pos_top='20%',
        pos_left='5%',
        pos_right='40%'
    )
)

# 生成组合的图像
grid.render('./html/柱状图、折线图组合绘制.html')

# 绘制流程
# 1、绘制柱状图，添加多个纵轴
# 2、绘制折线图
# 3、层叠 柱状图、折线图
# 4、加入到grid
# 5、配置文本
