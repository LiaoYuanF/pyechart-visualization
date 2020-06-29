#!/usr/bin/env python
# coding: utf-8

# In[228]:


from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Pie, Tab
from pyecharts.faker import Faker
from pyecharts import options as opts
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker
from pyecharts.charts import Grid, Liquid
from pyecharts.commons.utils import JsCode
from pyecharts.charts import EffectScatter
import csv


# In[229]:


data = []
with open(r'data.csv', 'r') as f:
    reader1 = csv.reader(f)
    result = list(reader1)


# In[230]:


day_list = [i[0] for i in result]
total_list= [float(i[1]) for i in result]
frequency_list = [float(i[2]) for i in result]


# In[231]:


def line_1() -> Line:
    c = (
        Line()
        .add_xaxis(day_list)
        .add_yaxis(
            "总额",
            total_list,
            is_smooth= True,
            label_opts=opts.LabelOpts(is_show=False),
        )

        .set_global_opts(
        xaxis_opts=opts.AxisOpts(is_scale=True),
        yaxis_opts=opts.AxisOpts(
            is_scale=True,
            splitarea_opts=opts.SplitAreaOpts(
                is_show=False, areastyle_opts=opts.AreaStyleOpts(opacity=1)
            ),
       
        ),
        datazoom_opts=[opts.DataZoomOpts(type_="inside")],
        title_opts=opts.TitleOpts(title="近一个月每日成交总额"),
    )
    )

    return c


# In[232]:


def line_2() -> Line:
    c = (
        Line()
        .add_xaxis(day_list)
        .add_yaxis(
            "次数",
            frequency_list,
            is_smooth= True,
            label_opts=opts.LabelOpts(is_show=False),
        )
        #.set_global_opts(title_opts=opts.TitleOpts(title="line_1"))
        
        .set_global_opts(
        xaxis_opts=opts.AxisOpts(is_scale=True),
        yaxis_opts=opts.AxisOpts(
            is_scale=True,
            splitarea_opts=opts.SplitAreaOpts(
                is_show=False, areastyle_opts=opts.AreaStyleOpts(opacity=1)
            ),
       
        ),
        datazoom_opts=[opts.DataZoomOpts(type_="inside")],
        title_opts=opts.TitleOpts(title="近一个月每日成交次数"),
    )
    )
    return c


# In[233]:


def liquid_0():
    l1 = (
        Liquid()
        #.add("年度交易总额", [0.75], center=["80%", "50%"])
        .add(
        "年度交易总额",
        [2005],
        center=["80%", "50%"],
        label_opts=opts.LabelOpts(
            font_size=30,
            formatter=JsCode(
                """function (param) {
                    return (Math.floor(param.value * 100) / 100) + '亿元';
                }"""
            ),
            position="inside",
        ),
        )
        
        
        .set_global_opts(title_opts=opts.TitleOpts(title="年度关键指标"))
    )

    l2 = Liquid().add(
        "年度交易顾客",
        [247],
        center=["20%", "50%"],
        label_opts=opts.LabelOpts(
            font_size=30,
            formatter=JsCode(
                """function (param) {
                    return (Math.floor(param.value * 100) / 100) + '人';
                }"""
            ),
            position="inside",
        ),
    )
    l3 =  Liquid().add(
        "年度交易次数",
        [5836],
        center=["50%", "50%"],
        label_opts=opts.LabelOpts(
            font_size=30,
            formatter=JsCode(
            """function (param) {
                    return (Math.floor(param.value * 100) / 100) + '万次';
                }"""
            ),
            position="inside",
        ),
    )

    grid = Grid().add(l1, grid_opts=opts.GridOpts()).add(l2, grid_opts=opts.GridOpts()).add(l3, grid_opts=opts.GridOpts())
    return grid


# In[234]:


def pie_3():
    with open(r'type.csv', 'r') as f:
        reader = csv.reader(f)
        result = list(reader)
    x = [x[0] for x in result]
    y = [x[1] for x in result]
    
    columns = x
    #print(columns)
    data1 = y
    c = (
        Pie()
        .add("", [list(z) for z in zip(columns, data1)])
        .set_global_opts(title_opts=opts.TitleOpts(title="各商品交易比例"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c


# In[235]:



def s_4():
    with open(r'pro.csv', 'r') as f:
        reader = csv.reader(f)
        result = list(reader)
    pro_list = [i[0] for i in result]
    total_list= [float(i[1]) for i in result]
    p = (
        EffectScatter(init_opts=opts.InitOpts(width='1200px', height='800px'))
        .add_xaxis(pro_list)
        .add_yaxis("交易额",total_list,label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="本年度交易额省份排名分析"),
            xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
            yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
        )
    )
    return p


# In[236]:


def s_5():
    with open(r'cus.csv', 'r') as f:
        reader = csv.reader(f)
        result = list(reader)

    cus_list = [i[0] for i in result]
    total_list= [float(i[1]) for i in result]
    c = (
        EffectScatter(init_opts=opts.InitOpts(width='1200px', height='800px'))
        .add_xaxis(cus_list)
        .add_yaxis("交易次数",total_list,label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="本年度交易次数顾客排名分析-TOP20"),
            xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
            yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
        )
    )
    return c



tab = Tab()
tab.add(liquid_0(), "年度关键指标")
tab.add(line_1(), "交易总额")
tab.add(line_2(), "交易次数")
tab.add(pie_3(), "交易种类")
tab.add(s_4(), "省份排名分析")
tab.add(s_5(), "顾客排名分析")
tab.render("tab_base.html")


# In[ ]:





