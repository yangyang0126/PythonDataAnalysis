# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:01:15 2020
@author: Yenny
"""

import requests  # 获取网页数据
from bs4 import BeautifulSoup  # 解析网页数据
import urllib

url = "https://plotly.com/python/"

res = requests.get(url)  # requests发起请求，静态网页用get    
soup = BeautifulSoup(res.text, 'html.parser')
items = soup.find_all('img')
for i in items:
    try:
        image = i['src']
        name = i['alt']
        if image[-1] == 'g':
            SaveName = name + '.jpg'
        else:
            SaveName = name + '.gif'
        print("![{}]({})".format(name,image))
        urllib.request.urlretrieve(image, SaveName)
    except:
        pass