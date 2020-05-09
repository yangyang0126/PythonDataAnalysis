# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 21:21:44 2020

@author: zhaoy
"""

from pyecharts import Liquid
liquid =Liquid("水球图示例")
liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_outline_show=False)
liquid.show_config()
liquid.render()