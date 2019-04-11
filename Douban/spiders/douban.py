# -*- coding: utf-8 -*-
import scrapy
import re,os
from bs4 import BeautifulSoup
from scrapy.http import Request
# from Douban.items import DoubanItem
class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ('https://movie.douban.com/subject/1291546/comments?start=0&limit=20&sort=new_score&status=P',)
    url_1='https://movie.douban.com/subject/1291546/comments?start='
    url_2='&limit=20&sort=new_score&status=P'
    path='C:\Python\Douban\Douban\comment.txt'
    num=0
    def start_requests(self):
        for i in range(10):
            url=self.url_1+str(self.num)+self.url_2
            self.num = self.num + 20
            yield Request(url,self.parse)
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


