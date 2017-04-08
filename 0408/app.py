# coding:utf-8

# jandan.com

# count = 2425
url = 'http://jandan.net/ooxx/page-'
import os
import requests
from bs4 import BeautifulSoup
import time
import random

def spider(url, count):
    res = requests.get(url + str(count))
    html = BeautifulSoup(res.text)
    # print(html)
    for index, item in enumerate(html.select('#comments img')):
        # print(item.attrs['src'])
        # print('http://' + item.attrs['src'][2:])
        if (not os.path.exists(str(count))):
            os.mkdir(str(count))
        filename = str(count) + '/{}.jpg'.format(index)
        print(filename)
        with open(filename, 'wb') as jpg:
            jpg.write(requests.get('http://' + item.attrs['src'][2:], stream=True).content)


def run(url, count):
    while count > 0:
        spider(url, count)
        count = count - 1
        time.sleep(random.randint(1,5))


url = 'http://jandan.net/ooxx/page-'
count = 2425

run(url, count)
