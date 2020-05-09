# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:01:15 2020
@author: Yenny
"""

import requests  # 获取网页数据
from bs4 import BeautifulSoup  # 解析网页数据
import urllib

url = "https://matplotlib.org/gallery/index.html"

res = requests.get(url)  # requests发起请求，静态网页用get    
soup = BeautifulSoup(res.text, 'html.parser')
items = soup.find_all('img')
for i in items:
    try:
        image = i['src']
        imageUrl = 'https://matplotlib.org/'+image.lstrip('../')
        name = i['alt']
        if image[-1] == 'g':
            SaveName = name.lstrip('../') + '.jpg'
        else:
            SaveName = name.lstrip('../') + '.gif'
        print("![{}]({})".format(name,imageUrl))
        urllib.request.urlretrieve(imageUrl, SaveName)
    except:
        pass