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

mycursor.execute("desc university_page_data ")
university_page_link = mycursor.fetchall()
for i in university_page_link:

    if i[0] == uname:
        print(' found : ')


#print("university link ::::::::::::::  ", university_page_link)


mydb.commit()
