import scrapy
from.mysql_con import mydb



class UniversityPageInfo(scrapy.Spider):
    name = "university"


    for i in range(2):


        def start_requests(self):
            mycursor = mydb.cursor()
            mycursor.execute("select link from university_info where id = 169 ")
            university_page_link = mycursor.fetchall()
            for i in university_page_link:
                #print('unversity: ', i[0])
                url = i[0]
                print('url : ', url)
                yield scrapy.Request(url=url, callback=self.parse)



        def parse(self, response):

            # get university description
            university_description = response.xpath(
                '//*[@class="Styled__WikiWidget-sc-1yl1nt-83 jniITB wiki"]/p/text()').extract()
           # print('University description')
           # print(university_description)
            print()

            # get all courses name
            courses = response.xpath('//*[@class="Styled__WidgetContent-opouq6-2 iJqtXa"] ')
            course = courses.xpath('.//*[@class="Styled__CourseTag-sc-1r3eix0-0 cuhzRO"]/text() ').extract()
            print("Courses :::: ")
            #print(course)
            print()


            # University at glance (Table)
            glance_table =  response.xpath('//*[@class="Styled__TableStyle-sc-10ucg51-0 hfBVJr"]/tbody/tr/td/text() ').extract()

            glance_table_int_website = response.xpath('//*[@class="Styled__TableStyle-sc-10ucg51-0 hfBVJr"]/tbody/tr/td/a/@href ').extract()

            """
            put all values in dictonary from university glance table
            """
            university_glance = {
                "International_Students'" : glance_table[1],
                "UGPG_coourse" :  glance_table[3],
                "Endowments_value":  glance_table[5],
                "No_campuses":  glance_table[7],
                "yearly_hostel_expense":  glance_table[9],
                "international_students_website": glance_table_int_website
            }

            # University ranking table

            rank_name = response.xpath('//*[@class="Styled__RankingDetailBox-sc-132amsi-12 efmkzO"]/label/text() ').extract()
            ranking = list(response.xpath('//*[@class="Styled__RankingDetailBox-sc-132amsi-12 efmkzO" ]/p/strong/text() ').extract())
            print(rank_name)
            #print(ranking)
            # remove '#' from ranking list

            for i in list(ranking):
                if i == '#':
                    ranking.remove(i)
            #print(ranking)
             # Create dic to assign rank name & their ranking
            ranking_dic = {}
            total_rankNames = len(rank_name)
            for i in range(total_rankNames):
                ranking_dic[rank_name[i]] = ranking[i]
            print('Printing  ranking dic >>>>>>>>>>>>>>>>>')
            print(ranking_dic)











