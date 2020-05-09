# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:48:02 2020

@author: zhaoy
"""

import pandas
from pyecharts.charts import Sankey
from pyecharts import options as opts

data = pandas.read_excel('D:/Coding/Python/pyecharts/ly.xlsx',sheet_name='1')

nodes = []
for i in set(pandas.concat([data.来源地, data.输入地])):
    d1 = {}
    d1['name'] = i
    nodes.append(d1)

links = []
for x, y, z in zip(data.来源地, data.输入地, data.数量):
    d2 = {}
    d2['source'] = x
    d2['target'] = y
    d2['value'] = z
    links.append(d2)
    
pic = (
    #创角桑基图对象，设置画布大小
    Sankey(init_opts=opts.InitOpts(width="1600px", height="800px")).add(
            '确诊病例', #图例名称
            nodes,    #节点数据
            links,   #边和流量数据
            #设置透明度、弯曲度、颜色
            linestyle_opt=opts.LineStyleOpts(opacity = 0.3, curve = 0.5, color = "source"),
            label_opts=opts.LabelOpts(position="right"), #标签显示位置        
            node_gap = 10 #节点之前的距离
            )
    .set_global_opts(title_opts=opts.TitleOpts(title = 'TOP10境外输入统计'))
)

pic.render('TOP10境外输入统计.html')