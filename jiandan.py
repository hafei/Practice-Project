import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import time
import os



def download_img(url):
    fdir = "D:/data/jiandan"
    if not os.path.exists(fdir):
        os.makedirs(fdir)
    try:
        # (p2) = os.path.split(url)
        # (p2, f2) = os.path.split(url)
        f2 = ''.join(map(lambda xx: (hex(ord(xx))[2:]), os.urandom(16)))  # 随机字符串作为文件名字，防止名字重复
        # if os.path.exists(fdir + "/" + f2):
        #    print "fdir is exists"
        if url:
            imgtype = url.split('/')[4].split('.')[1]
            filename, msg = urllib.urlretrieve(url, fdir + "/" + f2 + '.' + imgtype)
            if os.path.getsize(filename) < 100:
                os.remove(filename)
    except Exception as e:
        return "down image error!"


url = 'http://jandan.net/ooxx/page-'
i = 2028
user_agent = {
    'Host': 'jandan.net',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/42.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Referer': 'http://jandan.net/ooxx/',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
}
while i > 0:
    time.sleep(1)
    endurl = url + str(i)
    req = urllib.request.Request(url=endurl, headers=user_agent)
    _content = urllib.request.urlopen(req).read()
    bs = BeautifulSoup(_content)
    imgs = bs.find_all("a", target="_blank", class_="view_img_link")
    for img in imgs:
        if img.get('href') != None:
            print(img.get('href'))
            download_img(img.get('href'))
    i = i + 1

