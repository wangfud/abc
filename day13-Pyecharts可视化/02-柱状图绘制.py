# 导入柱状图绘制模块
from pyecharts.charts import Bar
# 导入配置模块
from pyecharts import options as opts

# 1、实例化对象
bar = Bar()

# 2、添加数据
# a、添加纵轴数据
bar.add_yaxis(
    series_name='商家A',  # 图例名称
    yaxis_data=[114, 55, 27, 101, 125, 27, 105],  # 纵轴数据
)

# 添加一组纵轴数据
bar.add_yaxis(
    series_name='商家B',
    yaxis_data=[57, 134, 137, 129, 145, 60, 49]
)

# b、添加横轴数据
bar.add_xaxis(
    xaxis_data=['衬衫', '毛衣', '领带', '裤子', '风衣', '高跟鞋', '袜子'],  # 横轴数据
)

# 3、全局配置
# 可以通过 set_global_opts 来设置全局配置
bar.set_global_opts(
    # 标题配置项
    title_opts=opts.TitleOpts(
        title='柱状图绘制',  # 标题名称
    )
)

# 4、系列配置
# 可以通过 set_series_opts 来设置全局配置项
bar.set_series_opts(
    # 标签配置项
    label_opts=opts.LabelOpts(
        is_show=True,  # 显示标签
        position='right', # 设置标签位置
    )
)

# 注意：翻转坐标系
bar.reversal_axis()

# 5、生成图像
bar.render('./html/柱状图绘制.html')
