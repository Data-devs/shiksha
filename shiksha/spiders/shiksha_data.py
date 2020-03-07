# -*- coding: utf-8 -*-
import scrapy
from .mysql_con import mydb

class ShikshaDataSpider(scrapy.Spider):
    name = 'shiksha_data'
    allowed_domains = ['studyabroad.shiksha.com/canada/universities']
    start_urls = ['http://studyabroad.shiksha.com/canada/universities']

    def parse(self, response):

        #main link
        #name = response.xpath('//*[@class="font-18 number-bg"]') #custom selector
        university_link = response.xpath('//*[@class="font-15"]/@href').extract()
        university_name = response.xpath('//*[@class="font-15"]/strong/text()').extract()

        # mysql connection

        # for uname in university_name:
        #     print(uname)
        #     mycursor = mydb.cursor()
        #     sql = "insert into university_info(name) value (%s) "
        #     val = [uname]
        #     mycursor.execute(sql, val)
        #
        #     mydb.commit()

        for i in range(20):

                uname = university_name[i]
                uname_l = university_link[i]
                mycursor = mydb.cursor()
                sql = "insert into university_info(name,link) values (%s,%s) "
                val = [uname,uname_l]
                mycursor.execute(sql, val)

                mydb.commit()




















