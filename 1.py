#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
import re
url = "http://cl.clus.pw/thread0806.php?fid=2"
response = urllib.request.urlopen(url)
_content = response.read().decode('gbk')
bs = BeautifulSoup(_content)
items = bs.find('body').find('div', id='main').find(name='div', attrs={"class": "t", "style": "margin:3px auto"}).find('table', id='ajaxtable').find('tbody',attrs={"style":"table-layout:fixed;"}).findAll(name="tr",attrs={"class": "tr3 t_one","align":"center"})
for item in items:
    target = item.find(name='td', attrs={"style": "text-align:left;padding-left:8px"}).find('h3').find('a')
    if target.u is None and target.b == None and target.font == None:
        print("http://www.jt116.com/"+target.get('href'))





