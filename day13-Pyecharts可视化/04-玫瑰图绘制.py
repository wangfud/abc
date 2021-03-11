# 导包 --饼图
from pyecharts.charts import Pie
# 配置
from pyecharts import options as opts

# 导入背景主题模块
from pyecharts.globals import ThemeType

import pandas as pd

# 加载数据
data = pd.read_excel('./data/Python地区分校人数.xls')
print('data:\n', data)

# 准备 data_pair --->[(k1,v1),(k2,v2),...]
data_pair = [(k, v) for k, v in zip(data.loc[:, '分校'].tolist(), data.loc[:, '人数'].tolist())]
print('data_pair:\n', data_pair)

# 1、实例化对象
pie = Pie(
    # 初始化配置
    init_opts=opts.InitOpts(
        width='900px',  # 宽度
        height='600px',  # 高度
        page_title='我是一个饼图',  # 网页名称
        # theme=ThemeType.DARK,  # 背景主题
        theme='dark',  # 背景主题
    )
)
# 2、添加数据
pie.add(
    series_name=data.loc[:, '分校'].tolist(),  # 系列名称
    data_pair=data_pair,  # 数据 --[(k1,v1),(k2,v2),....]
    radius=['30%', '70%'],  # 内外半径
    is_clockwise=True,  # 饼图的各部分顺时针分布
    # rosetype='radius',  # 玫瑰类型，radius --扇区圆心角展现数据的百分比，半径展现数据的大小
    rosetype='area',  # 玫瑰类型，area --所有扇区圆心角相同，仅通过半径展现数据大小
)

# 3、全局配置
pie.set_global_opts(
    # 标题配置项
    title_opts=opts.TitleOpts(
        title='Python分校人数占比饼图',  # 饼图标题
        subtitle='广州Python0624班级全体',  # 子标题
        pos_left='left',  # 标题距离左侧的间距,居左显示
    ),
    # 图例配置项
    legend_opts=opts.LegendOpts(
        type_='plain',  # 图例类型 --普通图例
        # type_='scroll',  # 图例类型 --滚动图例
        is_show=True,  # 显示图例
        pos_left='center',  # 图例居中
        pos_top='top'
    )
)

# 4、系列配置
pie.set_series_opts(
    # 标签设置
    label_opts=opts.LabelOpts(
        is_show=True,  # 显示标签
        font_size=12,  # 标签字体大小
        font_style='italic',  # 字体倾斜
        formatter='{b}:{d}%',  # 显示格式
    )
)

# 5、生成图像
pie.render('./html/玫瑰图绘制.html')
