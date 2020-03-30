import scrapy
from .mysql_con import mydb

university_id = 53

class University_city(scrapy.Spider):

    name = 'university_city'



    def start_requests(self):

        mycursor = mydb.cursor()
        mycursor.execute("select courses from university_info where id between 53 and 172 ")
        university_page_link = mycursor.fetchall()
        for i in university_page_link:
            # print('unversity: ', i[0])
            url = i[0]
            #url = "https://studyabroad.shiksha.com/canada/universities/university-of-alberta/courses"
            print('url : ', url)


            yield scrapy.Request(url=url, callback=self.parse)



    # main scraping codes in this method


    def parse(self, response):

        global university_id





        # print('-=-==-=-=-=== Spider open')

        # University location table data
        location_table = response.xpath(
            '//*[@class="Styled__TableStyle-sc-10ucg51-0 ihMXxO"]/tbody/tr/td/text() ').extract()
        location_table_wiki = response.xpath('//*[@class="Styled__AnchorStyle-sc-19aj422-1 bKWZUV"]/@href ').extract()

        city = str(location_table[1])
        size_of_city = str(location_table[3])
        population = str(location_table[5])
        wiki = str(location_table_wiki)

        # print('city : ', city)
        # print('size : ', size_of_city)
        # print('pop : ', population)
        # print('wiki: ', wiki)

        mycursor = mydb.cursor()
        sql = "insert into university_city_wiki (university_id,city,size,population,wiki) values (%s,%s,%s,%s,%s)"
        val = [university_id,city,size_of_city,population,wiki]
        mycursor.execute(sql, val)

        # print("///////////////// End ????????????????????????")
        #
        # print('+++++++++++++ Spider closed +++++++++++++++')

        university_id += 1

        mydb.commit()










