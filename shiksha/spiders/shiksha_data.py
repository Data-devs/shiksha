# -*- coding: utf-8 -*-
import scrapy
from .mysql_con import mydb

class ShikshaDataSpider(scrapy.Spider):
    name = 'shiksha_data'
    allowed_domains = ['studyabroad.shiksha.com/canada/universities']
    start_urls = ['https://studyabroad.shiksha.com/canada/universities-6']

    def parse(self, response):


        name = response.xpath('//*[@class="font-18 number-bg"]') #custom selector
        university_link = response.xpath('//*[@class="font-15"]/@href').extract()
        university_name = response.xpath('//*[@class="font-15"]/strong/text()').extract()


        number = len(university_name)
        print(":::::: totall ",number)
        for i in range(number):

                uname = university_name[i]
                uname_l = university_link[i]
                course = uname_l+'/courses' # add course link 
                ucourse = course
                mycursor = mydb.cursor()
                sql = "insert into university_info(name,link,courses) values (%s,%s,%s) "
                val = [uname,uname_l,ucourse]
                mycursor.execute(sql, val)

                mydb.commit()






















