import scrapy
from .mysql_con import mydb

class UniversityCoursesData(scrapy.Spider):

    name = 'university_courses'

    def start_requests(self):
        mycursor = mydb.cursor()
        mycursor.execute("select link from university_info where id = 53 ")
        university_page_link = mycursor.fetchall()
        for i in university_page_link:
            # print('unversity: ', i[0])
            #url = i[0]
            url = "https://studyabroad.shiksha.com/canada/universities/university-of-alberta/courses"
            print('url : ', url)
            yield scrapy.Request(url=url, callback=self.parse)





    # main scraping codes in this method

    def parse(self, response):

        courses = list(response.xpath('//*[@class="Styled__AllCourseTuple-sc-1yl1nt-33 kHvhnS"]/@id ').extract())
        couse_size = len(courses)
        print('total size = ',couse_size)
        a = str(1)


        for i in range(couse_size):

            div = str(i+1)
            # div = str(2)
            # print(type(div))

            # variable of all courses div
            main_div = response.xpath(' (//div[@class="Styled__AllCourseTuple-sc-1yl1nt-33 kHvhnS"])[' + div + '] ')

            course_name = main_div.xpath(
                ' (//*[@class="Styled__LinkStyle-sc-19aj422-2 jRTEUB"])[' + div + '] /text() ').extract()

            course_page = main_div.xpath(
                '( //*[@class="Styled__LinkStyle-sc-19aj422-2 jRTEUB"]) [' + div + '] /@href ').extract()

            for x in range(3):
                # course details
                course_duration = main_div.xpath(
                    '(//*[@class="Styled__AllCourseDetail-sc-1yl1nt-38 gpZxNg"]) [' + a + '] /p/text() ').extract()

                a = int(a)
                a +=1
                print('+++++++++ After iteration a value is : ',a)

                a = str(a)

                course_fee = main_div.xpath(
                    '(//*[@class="Styled__AllCourseDetail-sc-1yl1nt-38 gpZxNg"]) [' + a + '] /p/text() ').extract()
                a = int(a)
                a += 1
                print('+++++++++ After iteration a value is : ', a)
                a = str(a)
                course_ielts = main_div.xpath(
                    '(//*[@class="Styled__AllCourseDetail-sc-1yl1nt-38 gpZxNg"]) [' + a + ']  /p/text() ').extract()
                a = int(a)
                a += 1
                print('+++++++++ After iteration a value is : ', a)
                a = str(a)

                # printing all details .......

                print(" >>>>>>>>> :::: Details ::::>>>>>>>>>>>>>>>>>>>")
                print(' Couse name : ', course_name)
                print('Course page : ', course_page)
                print('Course duration : ', course_duration)
                print('Course fees : ', course_fee)
                print('Couse iel : ', course_ielts)



















