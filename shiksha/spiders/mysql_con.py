import mysql.connector


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password',
    database = 'shiksha'
)

print(mysql)
uname = 'university_name'
mycursor = mydb.cursor()

mycursor.execute("select link from university_info where id = 53 ")
university_page_link = mycursor.fetchall()
for i in university_page_link:

    print(i[0])


#print("university link ::::::::::::::  ", university_page_link)


mydb.commit()
