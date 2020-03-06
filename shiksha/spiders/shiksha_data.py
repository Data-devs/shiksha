# -*- coding: utf-8 -*-
import scrapy


class ShikshaDataSpider(scrapy.Spider):
    name = 'shiksha_data'
    allowed_domains = ['studyabroad.shiksha.com/canada/universities']
    start_urls = ['http://studyabroad.shiksha.com/canada/universities']

    def parse(self, response):
        link = response.xpath('//*[@class="font-18 number-bg"]/a/text()') #main link
        names = response.xpath('//*[@class="font-18 number-bg"]') #custom selector

