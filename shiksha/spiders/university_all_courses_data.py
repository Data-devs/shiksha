import scrapy
from .mysql_con import mydb

university_id = 53
a = 1


class UniversityCoursesData(scrapy.Spider):


    name = 'university_courses'



    def start_requests(self):

        mycursor = mydb.cursor()
        mycursor.execute("select courses from university_info where id =53 ")
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
        global a

        courses = list(response.xpath('//*[@class="Styled__AllCourseTuple-sc-1yl1nt-33 kHvhnS"]/@id ').extract())
        couse_size = len(courses)
        print('total size = ',couse_size)
        a = str(1)
        for i in range(couse_size):

            print('_=_+_+_+_+_+_ Start _+_+_+_+_+_+_+_ ')

            div = i+1
            div = str(div)
            print("+++ Div value : ",div)
            # div = str(2)
            # print(type(div))
            # variable of all courses div
            main_div = response.xpath(' (//div[@class="Styled__AllCourseTuple-sc-1yl1nt-33 kHvhnS"])[' + div + '] ')

            course_name = str(main_div.xpath(
                ' (//*[@class="Styled__LinkStyle-sc-19aj422-2 jRTEUB"])[' + div + '] /text() ').extract())

            course_page = str(main_div.xpath(
                '( //*[@class="Styled__LinkStyle-sc-19aj422-2 jRTEUB"]) [' + div + '] /@href ').extract())


            #......................................................
            # course details

            course_duration = str(main_div.xpath(
                '(//*[@class="Styled__AllCourseDetail-sc-1yl1nt-38 gpZxNg"]) [' + a + '] /p/text() ').extract())

            a = int(a)

            print(' > iteration a value is : ', a)
            a += 1

            a = str(a)

            course_fee = str(main_div.xpath(
                '(//*[@class="Styled__AllCourseDetail-sc-1yl1nt-38 gpZxNg"]) [' + a + '] /p/text() ').extract())
            a = int(a)

            print(' > iteration a value is : ', a)
            a += 1
            a = str(a)
            course_ielts = str(main_div.xpath(
                '(//*[@class="Styled__AllCourseDetail-sc-1yl1nt-38 gpZxNg"]) [' + a + ']  /p/text() ').extract())
            a = int(a)

            print(' > iteration a value is : ', a)
            a += 1
            a = str(a)

            # printing all details .......

            print(" :::: Details ::::")
            print(' Couse name : ', course_name)
            print('Course page : ', course_page)
            print('Course duration : ', course_duration)
            print('Course fees : ', course_fee)
            print('Couse iel : ', course_ielts)
            print('University id >>>>>> ', university_id)

            # mycursor = mydb.cursor()
            # sql = ("insert into university_courses (university_id,name,link,duration,1year_fees,exams) values (%s,%s,%s,%s,%s,%s)")
            # val = [university_id,course_name,course_page,course_duration,course_fee,course_ielts]
            # mycursor.execute(sql, val)







        university_id += 1



        print("///////////////// End ????????????????????????")

        mydb.commit()













