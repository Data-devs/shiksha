import mysql.connector


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password',
    database = 'shiksha'
)

print(mysql)
mycursor = mydb.cursor()
sql = "insert into university_info(name) value (%s) "
val = ['heool']
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)