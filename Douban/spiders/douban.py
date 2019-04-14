# -*- coding: utf-8 -*-
import scrapy
import re,os
from bs4 import BeautifulSoup
from scrapy.http import Request
# import time
# from Douban.items import DoubanItem
class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ('https://movie.douban.com/subject/1291546/comments?start=0&limit=20&sort=new_score&status=P',)
    url_1='https://movie.douban.com/subject/1291546/comments?start='
    url_2='&limit=20&sort=new_score&status=P'
    path='C:\Python\Douban\Douban\comment.txt'
    Cookie={'ll': '"118172"',
            'bid': 'RL-Ud9-M8Is',
            '__utmc': '223695111',
            '__yadk_uid': '1zmMhETBDMVis3yMbUOGhNAuDNXvCMfO',
            '_vwo_uuid_v2': 'D028E2287D9969D2E76DEC3EB4593E4C6|6481f784be57b1e49c6e37458118f7ae',
            'push_noty_num': '0',
            'push_doumail_num': '0',
            '__utmv': '30149280.18489',
            'douban-profile-remind': '1',
            'dbcl2': '"184896369:3JzWAGgS7TY"',
            'ck': '76wX',
            '__utmz': '223695111.1555125272.2.2.utmcsr',
            'ap_v': '0,6.0',
            '_pk_ref.100001.4cf6': '%5B%22%22%2C%22%22%2C1555141460%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fcat%3D1002%26q%3D%25E9%259C%25B8%25E7%258E%258B%22%5D',
            '_pk_id.100001.4cf6': '48856d09d3a72324.1555117412.4.1555141460.1555138770.',
            '__utma': '223695111.690157687.1555117412.1555138758.1555141460.4'}
    num=0
    def start_requests(self):
        for i in range(20):
            url=self.url_1+str(self.num)+self.url_2
            self.num = self.num + 20
            yield Request(url,cookies=self.Cookie,callback=self.parse)##返回值，并传递给parse
        # yield Request('',self.parse())
    def parse(self, response):
        if not os.path.exists(self.path):
            soup = BeautifulSoup(response.text, 'lxml')
            comments = soup.find_all('span', {'class': 'short'})
            for cm in comments:
                    # item=DoubanItem()
                    pattern_description = re.compile('<span class="short">([\s\S]+)</span>')
                    list_description = re.findall(pattern_description, str(cm))
                    with open(self.path, 'a+', encoding='utf-8') as f:
                        f.write(list_description[0])
                        f.close()
        # print(time.clock()) #2.2s

