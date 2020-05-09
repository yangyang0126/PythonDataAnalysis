# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 12:21:43 2020

@author: zhaoy
"""

import geoplotlib
thedata = geoplotlib.utils.read_csv('helloworld.csv')
geoplotlib.dot(thedata)
geoplotlib.show()